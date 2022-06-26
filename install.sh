#!/bin/bash

fullpath=$(pwd)
chmod +x xssparams.py
ln -s $fullpath/rxsstester.py /usr/local/bin/rxsstester

chmod +x getparams.py
ln -s $fullpath/getparams.py /usr/local/bin/getparams