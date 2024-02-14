#
# UNPKG Resolver
#
# return all data needed to download scripts and styles from UNPKG

from pprint import pprint
import yaml
import pathlib
from pathlib import Path

def resolve(package):
    current_directory = Path(__file__)
    pprint(current_directory)
