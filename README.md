<p>
  <img alt="logo" src="https://github.com/ehne/ERDot/raw/master/logo.png" align="center"/>
</p>
<h1 align="center">
  Welcome to ERDot 👋
</h1>
<p>
  <a href="https://pypi.org/project/ERDot/">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/ERDot?color=blue">
  </a>
  <a href="https://github.com/ehne/ERDot/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/ehne/ERDot" />
  </a>
</p>

> Creates Entity Relationship Diagrams from JSON code.

## Installation
to install ERDot:

```pip install ERDot```

you may also need to [install graphvis](https://graphviz.org/download/) to be able to create images of the dot files generated. If you don't want to install graphviz, you can copy the contents of the generated dot file into an [online grapviz viewer](https://edotor.net).

## CLI Usage
```bash
Usage: erdot INPUTFILE [OPTIONS] 

  ERDot generates graphvis .dot files from the .json file INPUTFILE.

Options:
  -o, --outputFile TEXT  The graphvis dot file to write to (.dot)
  --help                 Show this message and exit.
```

Note that after generating the .dot file, you will still need to output it to your desired format using graphviz. An example of how to do this:

```bash
erdot example.erd.json 

dot example.dot -Tpng -o imageFile.png
```

(You could also copy and paste the contents of the .dot file into an [online graphviz viewer](https://edotor.net))

## ERDJSON format:
```json
{
    "tables":{
        ...
    },
    "relations":[
        ...
    ],
    "rankAdjustments":"...",
    "label":"..."
}   
```

Every single one of these sections are required, however, if you dont need that specific feature (for example label or rankAdjustments), just leave the value blank

### table:
Each table inside of the table section of the ERDJSON document is formated like this:

```json
"TableName": {
      "*PrimaryKey": "Int(10)",
      "+ForeignKey": "Int(10)",
      "RandomData": "Char(70)"
    }
```

the general idea is that the key is the column name, and the value is the type.

you will also notice the `*` and `+` next to the column names, these indicate primary and foriegn keys respectively. You can combine two of these together into a primary foreign key, just by putting both a `*` and a `+` next to the name.

### relations:
each element in the relations array of the ERDJSON document is formatted like this:

```json
"TableOne:PrimaryKey 1--* TableTwo:ForeignKey"
```

There are three elements that make up the relation string, (1) the left hand side, (2) the cardinality indicator, and (3) the right hand side. 

#### Left and Right hand side:
The sides of the relation string consist of two elements, separated by a `:`. the text before the `:` indicates what table it is in, and the text after the `:` indicates what specific column it should use to link. (note how you dont include the `+` or `*` in the specific column text).

#### Cardinality indicator:
Each relationship must have two of these cardinalities in the indicator, separated by `--`:

```
Cardinality    Syntax
0 or 1         ?
exactly 1      1
0 or more      *
1 or more      +
```

So for example, the following defines a relationship between Person's PersonID primary key and BirthPlace's PersonID foreign key that reads "every person has exactly one birth place, linked together using PersonID":

```python
Person:PersonID *--1 BirthPlace:PersonID
```

### rankAdjustments
applies graphvis' rank adjustments to adjust where the tables appear in the final image. (note that it is only one string)

```js
{ rank=min; TableOne Tabletwo }; // sets TableOne and TableTwo to be in the minimum rank (left)
{ rank=same; TableThree TableFour }; // sets TableThree and TableFour to be in the same rank
{ rank=max; TableFive }; // sets TableFive to be in the maximum rank (right)
```

### Label
a string that sets what label will be drawn on top of the ERD, think of it like the title of the ERD.

## Example ERDJSON:
```json
{
    "tables":{
        "Person":{
            "*name":"char()",
            "height":"int()",
            "weight":"int()",
            "birthDate":"date()",
            "+birthPlaceID":"int()"
        },
        "BirthPlace":{
            "*id":"int()",
            "birthCity":"char()",
            "birthState":"char()",
            "birthCountry":"char()"
        }
    },
    "relations":[
        "Person:birthPlaceID *--1 BirthPlace:id"
    ],
    "rankAdjustments":"",
    "label":""
}
```

which then creates this image:

<img alt="logo" src="https://github.com/ehne/ERDot/raw/master/example/example.png" align="center"/>


## Author

👤 **ehne**

* Github: [@ehne](https://github.com/ehne)

## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
