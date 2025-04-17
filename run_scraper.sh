#!/bin/bash

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the scraper
python scraper.py

# Deactivate virtual environment
deactivate
