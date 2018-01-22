# from BasicFeatures import *
from ComplexFeatures import *
from Parser import *
from Perceptron import *
from time import time
import pickle
import utils
from Inference import *
from funcs import evaluate

def main():
    d = Parser(utils.TRAIN)
    # d = Parser(utils.DUM)
    f = CFeatures(d.sentences)
    # f = BFeatures(d.sentences)
    print("num of feats: ",f.f_len)
    # print("feats:", f.f_dict)
    w = np.zeros(f.f_len)
    tt = time()
    print("Training model for {} iterations...".format(utils.ITER))

    for i in range(utils.ITER):
        Perceptron(d.sentences,w,f,utils.MODE)
    print("time in seconds: {}".format(time()-tt))
    # print("w:\n",w)
    # pickle.dump(w, open(utils.W_VEC, 'wb'))
    return w

def infer(w):
    t = Parser(utils.TEST)
    d = Parser(utils.TRAIN)
    # d = Parser("dum")
    # f = BFeatures(d.sentences)
    f = CFeatures(d.sentences)
    print("num of feats: ",f.f_len)
    # w = pickle.load(open(utils.W_VEC, 'rb'))
    inf = Inference(w, t.sentences, f,utils.MODE)
    inf.tag_text(utils.TEST_R)
    evaluate(utils.TEST, utils.TEST_R)

if __name__ == "__main__":
    w = main()
    infer(w)