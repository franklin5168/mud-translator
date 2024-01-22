#!/usr/bin/python3

from xml.dom import minidom
from parsers.MudParser import MudParser


class XmlParser(MudParser):
    """
    XML-format MUD file parser.
    """

    def read_input(self) -> dict:
        """
        Read the input MUD file as a dictionary.

        :return: dictionary containing data read from the input MUD file
        """
        # TODO
        pass
