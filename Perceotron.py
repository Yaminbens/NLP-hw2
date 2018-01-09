import numpy as np
from chu_liu import *
from funcs import f_uv,w_f

class Perceptron:

    def __init__(self, sentences, w, feats):
        '''
        one iteration of perceptron on all sentences in corpus
        '''
        for sentence in sentences:
            # sentence_i = deepcopy(sentence)
            weights = self.weights_calc(sentence,w, feats)
            all_successors = sentence.sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v]).greedy()
            w += feats.f_xy(sentence.word_children, sentence.word_pos) - feats.f_xy(graph.successors, sentence.word_pos)



    # def ffff(self,sentence, y):

    def weights_calc(self,w,sentence, feats):
        self.weights = np.zeros(shape=(sentence.slen,sentence.slen))
        for i in range(sentence.slen): #includes root
            for j in range(sentence.slen):
                if i != j :
                    self.weights[i][j] = w_f(w,f_uv(feats,sentence,i,j))


