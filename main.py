from Features import *
from Parser import *
from Perceptron import *
from time import time

def main():
    # d = Parser("train.labeled")
    d = Parser("dum")
    f = Features(d.sentences)
    w = np.zeros(f.f_len)
    # tt = time()
    for i in range(10):
        Perceptron(d.sentences,w,f)
    # print(time()-tt)
    print("w:\n",w)


if __name__ == "__main__":
    main()