from Features import *
from Parser import *
from Perceotron import *

def main():
    # d = Parser("train.labeled")
    d = Parser("dum")
    for s in d.sentences:
        print(s.slen)
    f = Features(d.sentences)
    w = np.zeros(f.f_len)
    Perceptron(d.sentences,w,f.f_dict)


if __name__ == "__main__":
    main()