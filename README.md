[![Build Status](https://travis-ci.org/ncf-ds/chloroform.svg?branch=master)](https://travis-ci.org/ncf-ds/chloroform)

# chloroform

Chloroform is a survey generation system intended to allow generic reporting by defining questions using templates and pre-defined keywords.

# Running

Copy `cfg/settings.py.sample` to `cfg/settings.py` and edit the database connect string as appropriate, then run:

    python -m chloroform

This should start the flask server in debug mode (which will automatically restart whenever source code is changed).
