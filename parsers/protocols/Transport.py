#!/usr/bin/python3

from parsers.protocols.Protocol import Protocol


class Transport(Protocol):
    """
    Transport layer (TCP or UDP) protocol parser.
    """

    # Supported fields
    fields = [
        "source-port",
        "destination-port",
        "direction-initiated"
    ]

    # Supported operators on port numbers
    operators = {
        "lte": "<=",  # less than or equal to
        "gte": ">=",  # greater than or equal to
        "eq":  "",     # equal to
        "neq": "!="   # not equal to
    }


    def parse_port(self, port_match: dict) -> str:
        """
        Parse a protocol port match.

        :param port_match: dict of protocol port match
        :return: string of protocol port match for the YAML profile
        :raises ValueError: if the protocol port match is invalid
        """
        # Verify operator
        op = port_match.get("operator", None)
        if op not in self.operators:
            raise ValueError(f"Invalid operator '{op}' for source port")
        # Verify port number
        port = port_match.get("port", None)
        if port < 0 or port > 65535:
            raise ValueError(f"Invalid port number '{port}' for source port")
        
        # Port match is valid
        if op == "eq":
            return port
        else:
            return f"{self.operators[op]} {port}"


    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        :raises ValueError: if the protocol matches are invalid
        """
        # Initialize result dict
        proto_dict = {}

        # Parse source port
        src_port_match = matches.get("source-port", None)
        if src_port_match is not None:
            proto_dict["src-port"] = self.parse_port(src_port_match)

        # Parse destination port
        dst_port_match = matches.get("destination-port", None)
        if dst_port_match is not None:
            proto_dict["dst-port"] = self.parse_port(dst_port_match)

        # TODO: direction-initiated

        return proto_dict

