from Features import *
from Parser import *
from Perceptron import *
from time import time
import pickle
import utils

def main():
    d = Parser(utils.TRAIN)
    # d = Parser(utils.DUM)
    f = Features(d.sentences)
    # w = np.zeros(f.f_len)
    w = np.random.rand(f.f_len)
    tt = time()
    print("Training model for {} iterations...".format(utils.ITER))
    for i in range(utils.ITER):
        Perceptron(d.sentences,w,f)
    print(time()-tt)
    print("w:\n",w)
    pickle.dump(w, open(utils.W_VEC, 'wb'))


if __name__ == "__main__":
    main()