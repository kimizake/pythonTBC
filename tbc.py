#!/usr/local/bin/python3

import os
from src import Compiler
from sys import argv

if __name__ == "__main__":
    compiler = Compiler(os.path.abspath(argv[1]))
