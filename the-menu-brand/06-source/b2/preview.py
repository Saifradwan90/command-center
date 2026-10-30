import sys,importlib
from common import *
mods=sys.argv[1].split(',')
pages=[]
for m in mods:pages+=importlib.import_module(m).P
build(pages,'prev.html');print(len(pages))
