from funcs import weights_calc
from chu_liu import *
import re


class Inference:

    def __init__(self, w, sentences, feats):
        self.sentences = sentences
        for sentence in sentences:
            weights = weights_calc(w, sentence, feats)
            print(weights)
            all_successors = sentence.sentence_fc()
            graph = Digraph(all_successors, lambda u, v: weights[u][v])
            # print(weights)
            graphh = graph.mst()
            print(graphh.successors)
            sentence.word_children_inf = graph.successors

    def tag_text(self, filename):
        with open(filename, 'w') as file:
            for sentence in self.sentences:
                for idx in sentence.idx_word:
                    if idx != '*':
                        # print(sentence.word_children_inf)
                        for parent in sentence.word_children_inf:
                            if sentence.idx_word[idx] in sentence.word_children_inf[parent]:
                                paridx = sentence.word_idx[parent]
                                file.write(idx + "	" + sentence.idx_word[idx][:-len(idx)] + "	_	" + # index and word
                                       sentence.word_pos[sentence.idx_word[idx]] + "	_	_	" + #POS
                                       paridx + "	_	_	_\n") #token head

                file.write("\n")







