#!/usr/bin/python3

from __future__ import annotations
import importlib


class Protocol:
    """
    Default Protocol parser.
    """

    layer_3_protocols = ["ipv4", "ipv6"]
    layer_4_protocols = ["tcp", "udp"]


    @classmethod
    def init_protocol(c, protocol_name: str) -> Protocol:
        """
        Initialize the protocol parser.

        :param protocol_name: name of the protocol
        """
        if protocol_name in c.layer_3_protocols:
            module = importlib.import_module(f"parsers.protocols.Network")
            cls = getattr(module, "Network")
        elif protocol_name in c.layer_4_protocols:
            module = importlib.import_module(f"parsers.protocols.Transport")
            cls = getattr(module, "Transport")
        else:
            module = importlib.import_module(f"parsers.protocols.{protocol_name}")    
            cls = getattr(module, protocol_name)
        return cls(protocol_name)
    

    def __init__(self, protocol_name: str) -> None:
        """
        Constructor for the Protocol class.

        :param protocol_name: name of the protocol
        """
        self.name = protocol_name
    

    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        :raises NotImplementedError: concrete protocol subclass must implement the parse method
        """
        raise NotImplementedError("Concrete protocol subclass must implement the parse method")
