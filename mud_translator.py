#!/usr/bin/python3

"""
Translate a MUD profile (JSON/XML) into a YAML extended profile.
"""

# Libraries
import sys
from enum import Enum
import argparse
# Custom modules
import parsers.mud_json as mud_json
import parsers.mud_xml as mud_xml


class format(Enum):
    """
    Enumerate the different types of MUD profiles.
    """
    JSON = 1
    XML = 2


def parse_mud_file(input: str, output: str, format: format):
    """
    Parse a MUD file with the corresponding parser.
    """
    if format == format.JSON:
        mud_json.parse_mud_file(input, output)
    elif format == format.XML:
        mud_xml.parse_mud_file(input, output)


##### MAIN #####
if __name__ == "__main__":

    mud_file_format = None
    
    ## Parse command line arguments
    parser = argparse.ArgumentParser(description="Translate a MUD profile (JSON/XML) into a YAML extended profile.")
    # Input file
    parser.add_argument("input", type=str, help="Input MUD file (JSON or XML)")
    # Output file
    parser.add_argument("-o", "--output", type=str, help="Output YAML file")
    # Parse arguments
    args = parser.parse_args()

    # Get MUD file format
    if args.input.endswith(".json"):
        mud_file_format = format.JSON
    elif args.input.endswith(".xml"):
        mud_file_format = format.XML
    else:
        print("Error: Unrecognized MUD file format", file=sys.stderr)
        exit(1)

    # Set output file if not specified
    if args.output is None:
        if mud_file_format == format.JSON:
            args.output = args.input.replace(".json", ".yaml")
        elif mud_file_format == format.XML:
            args.output = args.input.replace(".xml", ".yaml")
    
    # Parse input file
    parse_mud_file(args.input, args.output, mud_file_format)
