#!/usr/bin/python3

from parsers.protocols.Protocol import Protocol


class icmp(Protocol):
    """
    ICMP protocol parser.
    """

    name = "icmp"

    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        """
        pass
