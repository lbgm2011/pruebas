__author__ = 'armonge'

from settings import *

try:
    from local import *
except ImportError:
    pass


try:
    from secrets import *
except ImportError:
    pass
