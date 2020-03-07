mypath = __path__[0]
# print(type(mypath), mypath)
from os import listdir
from os.path import isfile, join
# get all file names in directory that are python and not magic
__all__ = [f[:-3] for f in listdir(mypath) if isfile(join(mypath, f)) and f[0] != '_' and f[-3:] == '.py']

del listdir, isfile, join, mypath

from . import *