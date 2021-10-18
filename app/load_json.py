import sys
import json

def load(file):
    """Open json & return dictionary"""
    try:
        file_open = open(file)
        data = json.load(file_open)
        return data
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)