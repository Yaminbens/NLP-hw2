from chu_liu import *
import numpy as np
from copy import copy
import pickle
import utils

w1 = pickle.load(open("weights_vec/comp_w_" + str(utils.ITER) + "a", 'rb'))
w2 = pickle.load(open("weights_vec/comp_w_" + str(utils.ITER) + "b", 'rb'))

# for wa,wb
