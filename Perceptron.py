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

        # reorder sentences
        idxlist = [i for i in range(len(sentences))]
        # shuffle(idxlist)




        for i in idxlist:
            weights = weights_calc(w, sentences[i], feats,mode)

            all_successors = sentences[i].sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v])
            graph = graph.mst()
            # print(graph.successors)
            fxy = feats.f_xy(collections.OrderedDict(sentences[i].word_children), sentences[i].word_pos, sentences[i].word_idx, sentences[i].idx_word, sentences[i].slen,mode)
            fxy_tag = feats.f_xy(collections.OrderedDict(graph.successors), sentences[i].word_pos,sentences[i].word_idx, sentences[i].idx_word,sentences[i].slen,mode)


            w += np.subtract(fxy, fxy_tag)








