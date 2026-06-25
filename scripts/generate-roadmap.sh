#!/bin/bash

virtualenv venv
source venv/bin/activate

python3 -m pip show Pillow >> /dev/null
test "$?" = 0 || pip install Pillow

python3 generate-roadmap.py

deactivate
