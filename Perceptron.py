import numpy as np
from chu_liu import *
from funcs import f_uv,w_f,weights_calc

class Perceptron:

    def __init__(self, sentences, w, feats):
        '''
        one iteration of perceptron on all sentences in corpus
        '''
        for sentence in sentences:
            # sentence_i = deepcopy(sentence)
            weights = weights_calc(w, sentence, feats)
            all_successors = sentence.sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v])
            graph = graph.mst()
            # print(graph.successors)
            w += feats.f_xy(sentence.word_children, sentence.word_pos, sentence.word_idx) - \
                 feats.f_xy(graph.successors, sentence.word_pos,sentence.word_idx)






