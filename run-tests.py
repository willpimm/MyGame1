#!bin/python3

'''
This script sets up the path to the package to be tested
and then invokes pytest on the "tests" directory. This allows
application code and tests to be maintained in separate directory
trees, so that it's easier to build the final application for
deployment
'''

# Set up python path to include src directory

import sys
sys.path.insert(1, "src/");

import pytest
pytest.main(["tests"], None)
