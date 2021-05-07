#!/usr/bin/python3

from argparse import ArgumentParser
import os
from sys import stderr
from sys import platform
import site

try:
    import docker
except ImportError:
    os.system('pip install docker')
    if platform == "win32":
        os.system(f"python {site.getsitepackages()[0]}\\Script\\pywin32_postinstall.py -install")
    print("The Docker python module has been installed, continuing...", file=stderr)
    import docker

args = None
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
    args = parser.parse_args()


def main():
    _parse_args()
    if args.interactive:
        interactive_mode()
    print(docker.DockerClient().version())


def interactive_mode():
    pass


if __name__ == "__main__":
    main()
