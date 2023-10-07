"""
Scyblaster-Data main analysis program.

This script routes to the different programs below.
"""
from argparse import ArgumentParser
from src.formats import get_json_structures

MODULES = {"format": get_json_structures}

parser = ArgumentParser()
parser.add_argument("module", choices=MODULES.keys())

args = parser.parse_known_args()[0]
MODULES[args.module](parser)
