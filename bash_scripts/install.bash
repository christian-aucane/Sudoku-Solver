#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 src/generate_grids.py
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
    python src/generate_grids.py
else
    echo "Système d'exploitation non pris en charge."
    exit 1
fi

deactivate
