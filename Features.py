import numpy as np
from copy import copy

class Features:

    def __init__(self, sentences):
        idx = 0
        self.f1, idx = self.f_parent_posp(sentences,idx)
        self.f2, idx = self.f_parent(sentences,idx)
        self.f3, idx = self.f_posp(sentences, idx)
        self.f4, idx = self.f_child_posc(sentences,idx)
        self.f5, idx = self.f_child(sentences,idx)
        self.f6, idx = self.f_posc(sentences,idx)
        self.f8, idx = self.f_parent_child_posc(sentences,idx)
        self.f10, idx = self.f_parent_posp_posc(sentences,idx)
        self.f13, idx = self.f_posp_posc(sentences,idx)

        self.f_len = idx-1 #length of feature vector
        print(idx)
        self.f_dict = {}
        for d in (self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f8, self.f10, self.f13):
            self.f_dict.update(d)

        self.f_v_stats = self.stats(sentences, copy(self.f_dict))
        print(self.f_v_stats)

    #feature1: parent word + pos(parent)
    def f_parent_posp(self,sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                for pos in sentence.word_pos[parent]:
                    if parent+pos not in dic:
                        dic.update({parent+pos:num})
                        num += 1
        return dic, num

    #feature2: parent word
    def f_parent(self,sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent not in dic:
                    dic.update({parent:num})
                    num += 1
        return dic, num

    # feature3: POS of parent word
    def f_posp(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                for pos in sentence.word_pos[parent]:
                    if pos not in dic:
                        dic.update({pos: num})
                        num += 1
        return dic, num

    # feature4: child word + pos(parent)
    def f_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent,children in sentence.word_children.items():
                for child in children:
                    for pos in sentence.word_pos[child]:
                        if child + pos not in dic:
                            dic.update({child + pos: num})
                            num += 1
        return dic, num

    # feature5: child word
    def f_child(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child not in dic:
                        dic.update({child: num})
                        num += 1
        return dic, num

    # feature6: POS of child word
    def f_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    for pos in sentence.word_pos[child]:
                        if pos not in dic:
                            dic.update({pos: num})
                            num += 1
        return dic, num

    # feature8: parent word + child word + POS of child
    def f_parent_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    for posc in sentence.word_pos[child]:
                        if parent+child+posc not in dic:
                            dic.update({parent+child+posc: num})
                        num += 1
        return dic, num

    # feature10: parent word + POS of parent + POS of child
    def f_parent_posp_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    for posp in sentence.word_pos[parent]:
                        for posc in sentence.word_pos[child]:
                            if parent + posp + posc not in dic:
                                dic.update({parent + posp + posc: num})
                                num += 1
        return dic, num

    # feature13: POS of parent + POS of child
    def f_posp_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    for posp in sentence.word_pos[parent]:
                        for posc in sentence.word_pos[child]:
                            if posp + posc not in dic:
                                dic.update({posp + posc: num})
                                num += 1
        return dic, num

    def stats(self,sentences, dict):
        dic = dict
        for tag in dict:
            dic[tag] = 0

        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for posp in sentence.word_pos[parent]:
                    dic[parent+posp] += 1
                    dic[posp] += 1
                dic[parent] += 1
                for child in children:
                    dic[child] += 1
                    for posc in sentence.word_pos[child]:
                        dic[child + posc] += 1
                        dic[posc] += 1
                        dic[parent + child + posc] += 1
                        for posp in sentence.word_pos[parent]:
                            dic[parent + posp + posc] += 1
                            dic[posp + posc] += 1

        return dic


    def f_xy(self,sentence):
        index_vec = []

        for parent, children in sentence.word_children.items():
            index_vec.append(self.f_dict[parent + sentence.word_pos[parent]])
            index_vec.append(self.f_dict[parent])
            index_vec.append(self.f_dict[sentence.word_pos[parent]])
            for child in children:
                index_vec.append(self.f_dict[child + sentence.word_pos[child]])
                index_vec.append(self.f_dict[child])
                index_vec.append(self.f_dict[sentence.word_pos[child]])
                index_vec.append(self.f_dict[parent + child + sentence.word_pos[child]])
                index_vec.append(self.f_dict[parent + sentence.word_pos[parent] + sentence.word_pos[child]])
                index_vec.append(self.f_dict[sentence.word_pos[parent] + sentence.word_pos[child]])

        return index_vec

    def w_f_xy(self,w,f_xy):
        num = 0.0
        num = sum([w[x] for x in f_xy])
        return num

