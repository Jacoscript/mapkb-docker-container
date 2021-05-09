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
PRODUCTION = "production"
DEVELOPMENT = "development"
MASTER = "master"


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
    if args.interactive:
        interactive_mode()
    print(docker.DockerClient().version())


def _argument_is_default(arg_check: Callable[[], bool]):
    global incorrect_arguments

    if incorrect_arguments:
        return True
    return arg_check()


def _set_interactive_bool() -> bool:
    response = stdin.read()
    return response == "yes" or response == "y" or response == "YES" or response == "Y"


def _set_interactive_string(is_valid: Callable[[str], bool] = lambda x: True) -> str:
    response = stdin.read()
    if is_valid(response):
        return response
    else:
        print("This response is not valid, please try again")
        return


def interactive_mode():
    terminate = False
    while not terminate:
        if _argument_is_default(lambda: args.doi is False):
            print("Is this computer inside the Department of Interior network? "
                  "(This includes servers, workstations and DOI issued laptops)")
            args.doi = _set_interactive_bool()




if __name__ == "__main__":
    main()
