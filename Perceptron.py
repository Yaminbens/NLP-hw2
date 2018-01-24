import numpy as np
from chu_liu import *
from funcs import weights_calc
import collections
from random import shuffle

class Perceptron:

    def __init__(self, sentences, w, feats,mode):
        '''
        one iteration of perceptron on all sentences in corpus
        '''
        self.sentences =sentences
        self.w = w
        self.feats = feats
        self.mode = mode
        # reorder sentences
        self.idxlist = [i for i in range(len(sentences))]
        # shuffle(idxlist)




    def train(self):
        for i in self.idxlist:
            weights = weights_calc(self.w, self.sentences[i], self.feats, self.mode)

            all_successors = self.sentences[i].sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v])
            graph = graph.mst()
            # print(graph.successors)
            fxy = self.feats.f_xy(collections.OrderedDict(self.sentences[i].word_children), self.sentences[i].word_pos,
                                  self.sentences[i].word_idx, self.sentences[i].idx_word, self.sentences[i].slen,self.mode)
            fxy_tag = self.feats.f_xy(collections.OrderedDict(graph.successors), self.sentences[i].word_pos,
                                      self.sentences[i].word_idx, self.sentences[i].idx_word,self.sentences[i].slen,self.mode)

            self.w += np.subtract(fxy, fxy_tag)

    def getW(self):
        return self.w








