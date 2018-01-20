from BasicFeatures import *
from Parser import *
from Perceptron import *
from time import time
import pickle
import utils


d = Parser(utils.TRAIN)
# d = Parser(utils.DUM)
f = Features(d.sentences)
num = 0
feats = 0
for feat,val in f.f_v_stats.items():
    if val > utils.THRESHOLD-1:
        num += 1
    feats += 1
print("num: ",num)

f.refine(utils.THRESHOLD)

print(f.f_dict)
