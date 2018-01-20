import numpy as np
from chu_liu import *
from funcs import weights_calc

class Perceptron:

    def __init__(self, sentences, w, feats,mode):
        '''
        one iteration of perceptron on all sentences in corpus
        '''
        for sentence in sentences:
            # sentence_i = deepcopy(sentence)
            weights = weights_calc(w, sentence, feats,mode)
            all_successors = sentence.sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v])
            graph = graph.mst()
            # print(graph.successors)
            w += feats.f_xy(sentence.word_children, sentence.word_pos, sentence.word_idx, sentence.idx_word, sentence.slen,mode) - \
                 feats.f_xy(graph.successors, sentence.word_pos,sentence.word_idx, sentence.idx_word,sentence.slen,mode)






