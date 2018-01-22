import numpy as np
from copy import copy
import utils
import collections

class BFeatures:

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

        # print(len(self.f1))
        # print(len(self.f2))
        # print(len(self.f3))
        # print(len(self.f4))
        # print(len(self.f5))
        # print(len(self.f6))
        # print(len(self.f8))
        # print(len(self.f10))
        # print(len(self.f13))

        self.f_len = idx #length of feature vector
        print(self.f_len)
        self.f_dict = collections.OrderedDict()
        for d in (self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f8, self.f10, self.f13):
            self.f_dict.update(d)

        self.f_v_stats = self.stats(sentences, copy(self.f_dict))
        # print(self.f_v_stats)
        # self.refine(utils.THRESHOLD)

    # def refine(self, threshold):
    #     for feat in self.f_v_stats.keys():
    #         if self.f_v_stats[feat] < threshold:
    #             del self.f_dict[feat]
    #     idx = 0
    #     for feat in self.f_dict:
    #         self.f_dict[feat] = idx
    #         idx += 1
    #     self.f_len = idx



    #feature1: parent word + pos(parent)
    def f_parent_posp(self,sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                pos = sentence.word_pos[parent]
                if parent[:-len(sentence.word_idx[parent])]+pos not in dic:
                    dic.update({parent[:-len(sentence.word_idx[parent])]+pos:num})
                    num += 1
        return dic, num

    #feature2: parent word
    def f_parent(self,sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent[:-len(sentence.word_idx[parent])] not in dic:
                    dic.update({parent[:-len(sentence.word_idx[parent])]:num})
                    num += 1
        return dic, num

    # feature3: POS of parent word
    def f_posp(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                pos = sentence.word_pos[parent]
                if pos not in dic:
                    dic.update({pos: num})
                    num += 1

        return dic, num

    # feature4: child word + pos(parent)
    def f_child_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent,children in sentence.word_children.items():
                for child in children:
                    pos = sentence.word_pos[child]
                    if child[:-len(sentence.word_idx[child])] + pos not in dic:
                        dic.update({child[:-len(sentence.word_idx[child])] + pos: num})
                        num += 1
        return dic, num

    # feature5: child word
    def f_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child[:-len(sentence.word_idx[child])] not in dic:
                        dic.update({child[:-len(sentence.word_idx[child])]: num})
                        num += 1
        return dic, num

    # feature6: POS of child word
    def f_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    pos = sentence.word_pos[child]
                    if pos not in dic:
                        dic.update({pos: num})
                        num += 1
        return dic, num

    # feature8:  POS of parent + POS of child + child word
    def f_parent_child_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
                    if posp+posc+child[:-len(sentence.word_idx[child])] not in dic:
                        dic.update({posp+posc+child[:-len(sentence.word_idx[child])]: num})
                        num += 1
        return dic, num

    # feature10:  POS of parent + POS of child + parent word
    def f_parent_posp_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
                    if posp + posc + parent[:-len(sentence.word_idx[parent])] not in dic:
                        dic.update({posp + posc + parent[:-len(sentence.word_idx[parent])]: num})
                        num += 1
        return dic, num

    # feature13: POS of parent + POS of child
    def f_posp_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
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
                posp = sentence.word_pos[parent]
                dic[parent[:-len(sentence.word_idx[parent])]+posp] += 1
                dic[posp] += 1
                dic[parent[:-len(sentence.word_idx[parent])]] += 1
                for child in children:
                    dic[child[:-len(sentence.word_idx[child])]] += 1
                    posc = sentence.word_pos[child]
                    dic[child[:-len(sentence.word_idx[child])] + posc] += 1
                    dic[posc] += 1
                    dic[posp + posc + child[:-len(sentence.word_idx[child])]] += 1
                    dic[posp + posc + parent[:-len(sentence.word_idx[parent])]] += 1
                    dic[posp + posc] += 1

        return dic

    def f_xy(self,word_children, word_pos, word_idx, idx_word,slen,mode):
        index_vec = np.zeros(self.f_len)

        for parent, children in word_children.items():
            for child in children:
                posp = word_pos[parent]
                try:
                    #f1: parent +posp
                    index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp]] += 1
                except:
                    pass
                try:
                    #f3: posp
                    index_vec[self.f_dict[posp]] += 1
                except:
                    pass
                try:
                    #f2: parent
                    index_vec[self.f_dict[parent[:-len(word_idx[parent])]]] += 1
                except:
                    pass
                try:
                    #f5 child
                    index_vec[self.f_dict[child[:-len(word_idx[child])]]] += 1
                except:
                    pass
                posc = word_pos[child]
                try:
                    #f4: child +posc
                    index_vec[self.f_dict[child[:-len(word_idx[child])] + posc]] += 1
                except:
                    pass
                try:
                    #f6: posc
                    index_vec[self.f_dict[posc]] += 1
                except:
                    pass
                try:
                    #f8: posp + posc + child
                    index_vec[self.f_dict[posp + posc + child[:-len(word_idx[child])]]] += 1
                except:
                    pass
                try:
                    #f10: posp + posc + parent
                    index_vec[self.f_dict[posp + posc+ parent[:-len(word_idx[parent])]]] += 1
                except:
                    pass
                try:
                    #f13: posp + posc
                    index_vec[self.f_dict[posp + posc]] += 1
                except:
                    pass

        return index_vec





