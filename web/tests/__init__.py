from inspect import getsourcefile
import os.path
import sys

try:
    PATH = sys.path[:]
    current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    sys.path.insert(0, current_dir)
    import echo
finally:
    sys.path = PATH

__all__ = [
    echo
]
