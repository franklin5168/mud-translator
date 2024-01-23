#!/usr/bin/python3

from parsers.protocols.Protocol import Protocol


class ipv6(Protocol):
    """
    IPv6 protocol parser.
    """

    # Protocol name
    name = "ipv6"


    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        """
        pass
