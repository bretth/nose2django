import argparse
import nose2
import sys
from django.conf import settings

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--settings')
    args = parser.parse_args(sys.argv[1:])
    print(args)
    #nose2.discover()