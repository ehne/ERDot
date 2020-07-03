import sys
from .b import SimpleTemplate as t
from .dTemplate import dTemp
import json
import click
import os

@click.command()
@click.argument(
    "inputfile", type=click.Path(exists=True)
)
@click.option(
    "-o",
    "--outputFile",
    "o",
    required=True,
    help="The graphvis dot file to write to (.dot)",
    default= ""
)
def main(inputfile, o):
    i = inputfile
    # loads input json
    jsonLoaded = ""
    with click.open_file(i) as f:
        jsonLoaded = json.load(f)
    print(f"loaded {i}!")
    
    # figure out the output file name
    outFileName = ""
    if o == "":
        outFileName = f"{i.replace('.erd', '').replace('.json', '')}.dot"
    else:
        outFileName = o
    # opens the file to write to
    outputFile = click.open_file(outFileName, "w+")

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
    print(f"saved graphvis dot code to {outFileName}!")

if __name__ == "__main__":
    main()
