import sys
from .b import template as t
import json
import click

@click.command()
@click.option("-i", "--inputFile",required=True, help="The input ERDJSON file (.json)")
@click.option("-o", "--outputFile",required=True, help="The graphvis dot file to write to (.dot)")
def main(i, o):
    print(i, o)

if __name__ == '__main__':
    main()