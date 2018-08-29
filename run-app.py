#!bin/python3

'''
This script sets up the path to the package to be run, then executes it
'''

# Set up python path to include src directory
import sys
sys.path.insert(1, "src/");
import MyGame1
MyGame1.__main__()
