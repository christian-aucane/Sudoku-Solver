#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate
    cd src
    python3 app.py
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    source venv/Scripts/activate
    cd src
    python app.py
else
    echo "Système d'exploitation non pris en charge."
    exit 1
fi

deactivate
