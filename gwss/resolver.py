#
# UNPKG Resolver
#
# return all data needed to download scripts and styles from UNPKG
import sys
from pprint import pprint
import yaml
import pathlib
from pathlib import Path
from resolver_config import projects

def resolve_pkg(package: str):
    package_dict = {}
    try:
        package_dict = projects[package]
    except KeyError:
        pass
    if package_dict == {} or package_dict is None:
        sys.exit(1)

