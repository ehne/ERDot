import sys
from .b import SimpleTemplate as t
from .dTemplate import dTemp
import json
import click
import os

@click.command()
@click.option(
    "-i", "--inputFile", "i", required=True, help="The input ERDJSON file (.json)"
)
@click.option(
    "-o",
    "--outputFile",
    "o",
    required=True,
    help="The graphvis dot file to write to (.dot)",
    default="ERDotOutput.dot",
)
def main(i, o):
    # loads input json
    jsonLoaded = ""
    with click.open_file(i) as f:
        jsonLoaded = json.load(f)
    print(f"loaded {i} !")

    # opens the file to write to
    outputFile = click.open_file(o, "w+")

    # splits json into chunks
    try:
        tables = jsonLoaded["tables"]
        relations = jsonLoaded["relations"]
        rankAdjustments = jsonLoaded["rankAdjustments"]
        label = jsonLoaded["label"]
    except:
        print("You are missing some information from your json file!")
        exit()

    # generates the dot code
    tpl = t(dTemp)
    stringGen = tpl.render(tables=tables,
        relations=relations,
        ra=rankAdjustments,
        gs="",
        lbl=label)
    print("created graphvis dot code!")
    
    # write dot code to output file
    outputFile.write(stringGen)
    print(f"saved graphvis dot code to {o} !")

if __name__ == "__main__":
    main()
