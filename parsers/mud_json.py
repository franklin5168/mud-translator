#!/usr/bin/python3

import json
import yaml

"""
Parse a MUD profile in JSON format.
"""

def parse_mud_file(input: str, output: str) -> None:
    """
    Parse the input MUD file in JSON format,
    translate it to the YAML format,
    and write the output to the given output file.

    :param input: input MUD file in JSON format
    :param output: output YAML file
    """
    with open(input, "r") as mud_file:
        data = json.load(mud_file)

        

        with open(output, "w") as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
