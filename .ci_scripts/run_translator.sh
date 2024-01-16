#!/bin/bash

# Run MUD translator over example MUD files.

# JSON MUD files
python3 $GITHUB_WORKSPACE/mud_translator.py $GITHUB_WORKSPACE/examples/json/TPLink-Plug-Mudgee.json
python3 $GITHUB_WORKSPACE/mud_translator.py $GITHUB_WORKSPACE/examples/json/TPLink-Plug-UNSW-MUD.json

# XML MUD files
# TODO
