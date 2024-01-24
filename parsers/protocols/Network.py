#!/usr/bin/python3

import re
import ipaddress
from parsers.protocols.Protocol import Protocol


class Network(Protocol):
    """
    Network layer (IPv4 or v6) protocol parser.
    """

    # Mapping between supported MUD fields
    # and corresponding YAML profile fields
    fields = {
        "source-network": "src",
        "ietf-acldns:src-dnsname": "src",
        "destination-network": "dst",
        "ietf-acldns:dst-dnsname": "dst"
    }

    # Regex for domain name validation
    dns_regex = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9\.\-]{1,253}[a-zA-Z0-9]$")


    def parse_network(self, mud_field: str, network_match: dict) -> str:
        """
        Parse a network match.

        :param mud_field: name of the MUD field
        :param network_match: dict of network match
        :return: string of network match for the YAML profile
        :raises ValueError: if the network match is invalid
        """
        # If field is domain name, check if it is valid
        if "ietf-acldns" in mud_field:
            if not self.dns_regex.match(network_match):
                raise ValueError(f"Invalid domain name '{network_match}'")
            # Domain name is valid
            return network_match
        
        # Field is IP network, check if it is valid
        try:
            ipaddress.ip_network(network_match)
        except ValueError:
            raise ValueError(f"Invalid network '{network_match}'")
        
        # Network is valid
        return str(network_match)


    def parse(self, matches: dict) -> dict:
        """
        Parse the protocol matches.

        :param matches: dict of protocol matches read from the MUD file
        :return: dict of protocol matches for the YAML profile
        :raises ValueError: if the protocol matches are invalid
        """
        # Initialize result dict
        result_dict = {self.name: {}}
        proto_dict = result_dict[self.name]

        # Parse fields
        for mud_field, yaml_field in self.fields.items():
            net_match = matches.get(mud_field, None)
            if net_match is not None:
                proto_dict[yaml_field] = self.parse_network(mud_field, net_match)

        return result_dict
