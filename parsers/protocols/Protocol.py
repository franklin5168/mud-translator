#!/usr/bin/python3

from __future__ import annotations
import importlib


class Protocol:
    """
    Default Protocol parser.
    """

    @classmethod
    def init_protocol(c, protocol_name: str) -> Protocol:
        """
        Initialize the protocol parser.

        :param protocol_name: name of the protocol
        """
        module = importlib.import_module(f"parsers.protocols.{protocol_name}")
        cls = getattr(module, protocol_name)
        return cls()
    

    def __init__(self) -> None:
        """
        Constructor for the Protocol class.

        :param protocol_name: name of the protocol
        """
        pass
    

    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        :raises NotImplementedError: concrete protocol subclass must implement the parse method
        """
        raise NotImplementedError("Concrete protocol subclass must implement the parse method")
