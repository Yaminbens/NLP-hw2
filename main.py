from Features import *
from Parser import *
from Perceptron import *
from time import time
import pickle

def main():
    d = Parser("train.labeled")
    # d = Parser("dum")
    f = Features(d.sentences)
    # w = np.zeros(f.f_len)
    w = np.random.rand(f.f_len)
    ITER = 50
    tt = time()
    for i in range(ITER):
        Perceptron(d.sentences,w,f)
    print(time()-tt)
    print("w:\n",w)
    pickle.dump(w, open("weights_vec/" + "w" + str(ITER)+"_Rand", 'wb'))


if __name__ == "__main__":
    main()