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
    results = open("result","w")
    # for idxs in (3,4):
    #     for jdx in (1,2,4,6,8,10):
    idxs = 3
    jdx = 20
    d = Parser(utils.TRAIN)
    # d = Parser(utils.DUM)
    f = CFeatures(d.sentences, idxs)
    # f = BFeatures(d.sentences)
    # print("num of feats: ",f.f_len)
    w = np.zeros(f.f_len)
    tt = time()
    results.write("Training model for {} iterations with threshold {}...\n".format(jdx,idxs))
    perc = Perceptron(d.sentences, w, f, utils.MODE)
    for i in range(jdx):
        perc.train()
    w = perc.getW()
    results.write("time in seconds: {}\n".format(time() - tt))
    t = Parser(utils.TEST)
    inf = Inference(w, t.sentences, f,utils.MODE)
    inf.tag_text(utils.TEST_R)
    res = evaluate(utils.TEST, utils.TEST_R)
    results.write("correct: {}\n\n\n".format(res))

if __name__ == "__main__":
    w = main()
