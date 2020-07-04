import sys
from .b import SimpleTemplate as t
from .dTemplate import dTemp
import json
import click
import os
import time

def loadJson(_inputFile):
    with click.open_file(_inputFile) as f:
        jsonLoaded = json.load(f)
    return(jsonLoaded)

def figureOutOutputFileName(_inputFile,_outputFile):
    outFileName = ""
    if _outputFile == "":
        outFileName = f"{_inputFile.replace('.erd', '').replace('.json', '')}.dot"
    else:
        outFileName = _outputFile
    return(outFileName)

def splitJSONIntoChuncks(_inJSON):
    try:
        tables = _inJSON["tables"]
        relations = _inJSON["relations"]
        rankAdjustments = _inJSON["rankAdjustments"]
        label = _inJSON["label"]
    except:
        print("You are missing some information from your json file!")
        exit()
    return([tables,relations,rankAdjustments,label])

def generateDotCode(_chunkedJSON):
    tpl = t(dTemp)
    stringGen = tpl.render(tables=_chunkedJSON[0],
        relations=_chunkedJSON[1],
        ra=_chunkedJSON[2],
        gs="",
        lbl=_chunkedJSON[3])
    return(stringGen)

@click.command()
@click.argument(
    "inputfile", type=click.Path(exists=True)
)
@click.option(
    "-o",
    "--outputFile",
    "o",
    help="The graphvis dot file to write to (.dot)",
    default= ""
)
def main(inputfile, o):
    """ERDot generates graphvis .dot files from the .json file INPUTFILE."""
    with click.progressbar(length=6, label='Geneating .dot file') as bar:
        i = inputfile
        # loads input json
        jsonLoaded = loadJson(i)
        bar.update(1)
        # figure out the output file name
        outFileName = figureOutOutputFileName(i,o)
        bar.update(1)
        # opens the file to write to
        outputFile = click.open_file(outFileName, "w+")
        bar.update(1)
        # splits json into chunks
        chunkedJSON = splitJSONIntoChuncks(jsonLoaded)
        bar.update(1)
        # generates the dot code
        stringGen = generateDotCode(chunkedJSON)
        bar.update(1)
        # write dot code to output file
        outputFile.write(stringGen)
        bar.update(1)
        #print(f"saved graphvis dot code to {outFileName}!")



if __name__ == "__main__":
    main()
