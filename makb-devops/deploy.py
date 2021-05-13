#!/usr/bin/python3

from typing import Callable
from argparse import ArgumentParser
import os
from sys import stderr
from sys import stdin
from sys import platform
import site

try:
    import docker
except ImportError:
    os.system('pip3 install docker')
    if platform == "win32":
        os.system(f"python {site.getsitepackages()[0]}\\Scripts\\pywin32_postinstall.py -install")
    print("The Docker python module has been installed, please run this script again.", file=stderr)
    exit(1)

args = None
incorrect_arguments = False
# makb_assets_built = False
PRODUCTION = "production"
DEVELOPMENT = "development"
MASTER = "master"
MAKB_ASSETS = "makb-assets:latest"
MAKB_VIRTUOSO_CONTAINER = "makb-virtuoso-container"
MAXIMUM_RETRY_COUNT = 5


def _parse_args():
    global args
    parser = ArgumentParser(description="Deploy MapKB")
    parser.add_argument("--branch", action="store", default=MASTER,
                        help="Specify source Branch for MapKB source code")
    parser.add_argument("--deployment_mode", action="store", default=PRODUCTION, help="Specify deployment mode")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--doi", action="store_true", help="Deploying inside Department of the Interior")
    parser.add_argument("--source_path", action="store", default="",
                        help="Source location for MapKB project in development mode")
    parser.add_argument("--reset", action="store_true", help="Remove containers and all images associated with MapKB")
    args = parser.parse_args()


def main():
    _parse_args()
    if not _check_for_docker():
        return
    if args.reset:
        _reset_all()
        return
    if args.interactive:
        interactive_mode()
    _build_makb_assets()
    _build_makb_tomcat()
    _build_makb_virtuoso()
    container_name = _deploy_makb_virtuoso()
    print(f"To stop this container type `docker stop {container_name}`")
    print(f"To restart it later type `docker start {container_name}`")
    print(f"To remove it type `docker rm {container_name}` and rerun this script to recreate it")
    print(f"To reset MapKB and return to a default state type `python deploy.py --reset`")


def _argument_is_default(arg_check: Callable[[], bool]):
    global incorrect_arguments

    if incorrect_arguments:
        return True
    return arg_check()


def _set_interactive_bool() -> bool:
    response = stdin.readline()
    return response == "yes" or response == "y" or response == "YES" or response == "Y"


def _set_interactive_string(is_valid: Callable[[str], bool] = lambda x: True) -> str:
    response = stdin.readline()
    if is_valid(response):
        return response
    else:
        print("This response is not valid, please try again")
        return _set_interactive_string(is_valid)


def interactive_mode():
    terminate = False
    while not terminate:
        if _argument_is_default(lambda: args.doi is False):
            print("Is this computer inside the Department of Interior network? "
                  "(This includes servers, workstations and DOI issued laptops)")
            args.doi = _set_interactive_bool()

            if _argument_is_default(lambda: args.deployment_mode == PRODUCTION):
                print("Would you like to deploy MapKB in development mode?")
                if _set_interactive_bool():
                    args.deployment_mode = DEVELOPMENT
                else:
                    args.deployment_mode = PRODUCTION

            if args.deployment_mode == DEVELOPMENT and _argument_is_default(lambda: args.source_path == ""):
                print("Please enter the path to the MapKB source code, or leave blank to use an SSH tunnel.")
                args.source_path = _set_interactive_string()
            elif args.deployment_mode == PRODUCTION and _argument_is_default(lambda: args.branch == MASTER):
                print("What branch of MapKB would you like to use?  (Leave blank for master)")
                args.branch = _set_interactive_string()

            # if _argument_is_default(lambda: args.rebuild_assets is False) and makb_assets_built:
            #   print("MAKB Assets has already been built, would you like to rebuild it?")
            #    args.rebuild_assets = _set_interactive_bool()
        _print_interactive_settings()


def _print_interactive_settings():
    global incorrect_arguments
    print("MapKB will be configured with the following settings.\n")
    print(f"Deploying at DOI: {args.doi}")
    print(f"Deployment mode: {args.deployment_mode}")
    if args.deployment_mode == PRODUCTION:
        print(f"Branch: {args.branch}")
    else:
        print(f"MapKB source code location: {args.source_path}")
    # print(f"Rebuild MapKB Assets image: {args.rebuild_assets}")

    print("Are these settings correct?")
    incorrect_arguments = not _set_interactive_bool()


def _check_makb_assets() -> None:
    client = _create_docker_client()
    images = client.images.list()
    print("Checking for makb-assets image.")
    for i in images:
        for j in i.tags:
            if j == MAKB_ASSETS:
                makb_assets_built = True
                return
    makb_assets_built = False


def _build_makb_tomcat() -> None:
    path = "../makb-tomcat/Dockerbuild"
    tag = "makb-tomcat"
    print("Building makb-tomcat image")
    if args.deployment_mode == DEVELOPMENT:
        buildargs = {
            "ENV": "dev"
        }
        _build_image(path, tag, buildargs)
    else:
        _build_image(path, tag)


def _build_makb_assets() -> None:
    print("Building makb-assets image")
    _build_image("../makb-assets/Dockerbuild", MAKB_ASSETS)


def _build_makb_virtuoso() -> None:
    path = "../makb-virtuoso/Dockerbuild"
    tag = "makb-virtuoso"
    print("Building makb-virtuoso image")
    if args.doi:
        buildargs = {
            "doi": "1"
        }
        _build_image(path, tag, buildargs)
    else:
        _build_image(path, tag)


def _build_environment() -> dict:
    env: dict = {}
    if args.deployment_mode == DEVELOPMENT:
        env["ENV"] = "dev"
    elif args.deployment_mode == PRODUCTION:
        env["BRANCH"] = args.branch

    return env


def _build_volumes() -> dict:
    volumes: dict = {}
    if args.deployment_mode == DEVELOPMENT and not _argument_is_default(lambda: args.source_path == ""):
        volumes[args.source_path] = _create_ro_binding("/var/www/html")
    return volumes


def _build_ports() -> dict:
    ports = {
        "8080/tcp": 8080,
        "8890/tcp": 8890
    }

    if args.doi:
        ports["443/tcp"] = 443
    else:
        ports["80/tcp"] = 80

    if args.deployment_mode == DEVELOPMENT and _argument_is_default(lambda: args.source_path == ""):
        ports["22/tcp"] = 2222
    return ports


def _create_ro_binding(path: str) -> dict:
    return {"bind": path, "mode": "ro"}


def _deploy_makb_virtuoso() -> str:
    print("Deploying makb-virtuoso image")
    client = _create_docker_client()
    container = client.containers.run("makb-virtuoso", name=MAKB_VIRTUOSO_CONTAINER, volumes=_build_volumes(),
                                      ports=_build_ports(), detach=True, restart_policy={"Name": "always"})
    return container.name


def _build_image(path: str, tag: str, buildargs: dict = None) -> None:
    if buildargs is None:
        buildargs = {}
    client = _create_docker_client()
    client.images.build(path=path, tag=tag, buildargs=buildargs, rm=True)


def _check_for_docker() -> bool:
    result: int

    result = os.system(_fmt_path("docker"))
    if result != 0:
        print("Please install Docker or Docker Desktop", file=stderr)
        return False
    # result = os.system(_fmt_path("docker-compose"))
    # if result != 0:
    #    print("Please install Docker Compose", file=stderr)
    #    return False
    return True


def _fmt_path(path: str) -> str:
    if platform == "win32":
        path = path.replace("/", "\\")
    return path


def _create_docker_client() -> docker.DockerClient:
    return docker.from_env()


def _reset_all() -> None:
    tags = ['makb-virtuoso', "makb-tomcat", MAKB_ASSETS]
    client = _create_docker_client()
    for i in client.containers.list(all=True):
        if MAKB_VIRTUOSO_CONTAINER in i.name:
            print(f"Stopping {i.name}")
            i.stop()
            print(f"Removing {i.name}")
            i.remove()

    for i in tags:
        client.images.remove(i)


if __name__ == "__main__":
    main()
