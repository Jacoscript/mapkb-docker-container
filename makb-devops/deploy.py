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
makb_assets_built = False
PRODUCTION = "production"
DEVELOPMENT = "development"
MASTER = "master"
MAKB_ASSETS = "makb-assets:latest"


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
    parser.add_argument("--rebuild_assets", action="store_true", help="Rebuild the makb-assets image, if it exists")
    args = parser.parse_args()


def main():
    _parse_args()
    _check_makb_assets()
    if args.interactive:
        interactive_mode()
    print(docker.DockerClient().version())


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

            if _argument_is_default(lambda: args.rebuild_assets is False) and makb_assets_built:
                print("MAKB Assets has already been built, would you like to rebuild it?")
                args.rebuild_assets = _set_interactive_bool()
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
    print(f"Rebuild MapKB Assets image: {args.rebuild_assets}")

    print("Are these settings correct?")
    incorrect_arguments = not _set_interactive_bool()


def _check_makb_assets() -> None:
    global makb_assets_built
    client = docker.DockerClient()
    images = client.images.list()
    for i in images:
        for j in i.tags:
            if j == MAKB_ASSETS:
                makb_assets_built = True
                return
    makb_assets_built = False


def _build_makb_tomcat() -> None:
    path = "../makb-tomcat/Dockerbuild"
    tag = "makb-tomcat"
    if args.deployment_mode == DEVELOPMENT:
        buildargs = {
            "ENV": "dev"
        }
        _build_image(path, tag, buildargs)
    else:
        _build_image(path, tag)


def _build_makb_assets() -> None:
    _build_image("../makb-assets/Dockerbuild", MAKB_ASSETS)


def _build_makb_virtuoso() -> None:
    path = "../makb-virtuoso/Dockerbuild"
    tag = "makb-virtuoso"
    if args.doi:
        buildargs = {
            "DOI": "1"
        }
        _build_image(path, tag, buildargs)
    else:
        _build_image(path, tag)


def _deploy_makb_virtuoso() -> None:
    if args.source_path != "":
        os.system("docker-compose ../../docker-compose.volume.yml")
    else:
        os.system("docker-compose ../../docker-compose.yml")


def _build_image(path: str, tag: str, buildargs: dict = None) -> None:
    if buildargs is None:
        buildargs = {}
    client = docker.DockerClient()
    client.images.build(path=path, tag=tag, buildargs=buildargs)


if __name__ == "__main__":
    main()
