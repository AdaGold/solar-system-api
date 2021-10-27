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
        # return error to user instead of crashing, use abort?
        # maybe don't catch error here, send IOError in the route?

        