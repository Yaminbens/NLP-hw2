from chu_liu import *
import numpy as np
from copy import copy

sucs = {'a':['b','c'],'b':['c'],'c':['b']}
w = {'a': {'a': 1, 'b':2, 'c': 1}, 'b': {'b':1,'c':2}, 'c':{'a':2,'b':1,'c':1}}
g = Digraph((sucs),lambda u,v: -w[u][v])
print(g.successors)
for x,y in g.iteredges():
    print(x,y)

print("after greedy:")
print(g.greedy().successors)

g = g.mst()
print("after MST:")
print(g.successors)
print(sucs)
