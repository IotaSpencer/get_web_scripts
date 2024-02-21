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
from unpkg import Unpkg
def resolve_pkg(package: str) -> dict:
    # TODO: Also grab version from 'lastversion' to append to project render
    package_dict = {}
    try:
        package_dict = projects[package]
        return package_dict
    except KeyError:
        pass
    if package_dict == {} or package_dict is None:
        sys.exit(1)
    for script_name, script_file in package_dict['scripts'].items():
        # TODO add more
        single_unpkg_file_obj = Unpkg(package, version='', name=script_name, s_or_s='script', dest_dir='', filename=script_file)


    for style_name, style_file in package_dict['styles'].items():
        # TODO add more
        single_unpkg_file_obj = Unpkg(package, version='', name=style_name, s_or_s='style', dest_dir='', filename=style_file)
