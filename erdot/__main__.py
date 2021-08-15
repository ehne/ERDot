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
    return jsonLoaded


def figureOutOutputFileName(_inputFile, _outputFile):
    outFileName = ""
    if _outputFile == "":
        outFileName = f"{_inputFile.replace('.erd', '').replace('.json', '').replace('.yml', '').replace('.yaml', '')}.dot"
    else:
        outFileName = _outputFile
    return outFileName


def splitJSONIntoChuncks(_inJSON):
    try:
        tables = _inJSON["tables"]
        relations = _inJSON["relations"]
        rankAdjustments = _inJSON["rankAdjustments"]
        label = _inJSON["label"]
    except:
        print("You are missing some information from your json file!")
        exit()
    return [tables, relations, rankAdjustments, label]


def generateDotCode(_chunkedJSON):
    tpl = t(dTemp)
    stringGen = tpl.render(
        tables=_chunkedJSON[0],
        relations=_chunkedJSON[1],
        ra=_chunkedJSON[2],
        gs="",
        lbl=_chunkedJSON[3],
    )
    return stringGen


@click.command()
@click.argument("inputfile", type=click.Path(exists=True))
@click.option(
    "-o",
    "--outputFile",
    "o",
    help="The graphvis dot file to write to (.dot)",
    default="",
)
@click.option("-q", "--quiet", "q", help="Suppresses program information messages.", is_flag=True)
def main(inputfile, o, q):
    """ERDot generates graphvis .dot files from the .json/.yml file INPUTFILE."""
    
    # custom print function with quiet
    def qprint(msg):
        if not q:
            print(msg)
    i = inputfile
    if os.path.splitext(i)[1] in ('.yml', '.yaml'):
        try:
            from ruamel.yaml import YAML
        except ModuleNotFoundError:
            print("YAML support requires ruamel.yaml\nInstall it via pypi (https://pypi.org/project/ruamel.yaml/)")
            quit()
        yaml = YAML()
        jsonLoaded = json.loads(json.dumps(yaml.load(open(i))))
    else:
        # loads input json
        jsonLoaded = loadJson(i)
    qprint(f"loaded {i}")
    # figure out the output file name
    outFileName = figureOutOutputFileName(i, o)

    # opens the file to write to
    outputFile = click.open_file(outFileName, "w+")
    # splits json into chunks
    chunkedJSON = splitJSONIntoChuncks(jsonLoaded)
    # generates the dot code
    stringGen = generateDotCode(chunkedJSON)
    qprint(f"generated .dot code")
    # write dot code to output file
    outputFile.write(stringGen)
    qprint(f"saved graphvis dot code to {outFileName}!")


if __name__ == "__main__":
    main()
