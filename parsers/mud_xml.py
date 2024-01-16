#!/usr/bin/python3

from xml.dom import minidom
import yaml

"""
Parse a MUD profile in XML format.
"""


def parse_mud_file(input: str, output: str) -> None:
    """
    Parse the input MUD file in XML format,
    translate it to the YAML format,
    and write the output to the given output file.

    :param input: input MUD file in XML format
    :param output: output YAML file
    """
    pass