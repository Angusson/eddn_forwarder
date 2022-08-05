#!/usr/bin/bash

source ./.venv/bin/activate

python3 src/main.py > /dev/null 2>&1 &
