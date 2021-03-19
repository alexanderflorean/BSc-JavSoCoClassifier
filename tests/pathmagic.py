import os
import sys


class context:
    """Path hack to make tests work."""
    def __init__(self):
        self.script_folder = 'script'

    def __enter__(self):
        bp = os.path.dirname(os.path.realpath('.')).split(os.sep)
        modpath = os.sep.join(bp + [self.script_folder])
        sys.path.insert(0, modpath)

    def __exit__(self, *args):
        pass
