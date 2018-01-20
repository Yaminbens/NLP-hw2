import numpy as np
from copy import copy
import utils

class CFeatures:

    def __init__(self, sentences):
        idx = 0
        self.f1, idx = self.f_parent_posp(sentences,idx)
        self.f2, idx = self.f_parent(sentences,idx)
        self.f3, idx = self.f_posp(sentences, idx)
        self.f4, idx = self.f_child_posc(sentences,idx)
        self.f5, idx = self.f_child(sentences,idx)
        self.f6, idx = self.f_posc(sentences,idx)
        self.f8, idx = self.f_posp_posc_child(sentences,idx)
        self.f10, idx = self.f_parent_posp_posc(sentences,idx)
        self.f13, idx = self.f_posp_posc(sentences,idx)
        self.fc1, idx = self.f_posp_posbp_posc_posbc(sentences,idx)
        self.fc2, idx = self.f_posp_posap_posc_posbc(sentences, idx)
        self.fc3, idx = self.f_posp_posbp_posc_posac(sentences, idx)
        self.fc4, idx = self.f_posp_posap_posc_posac(sentences, idx)
        self.fc5, idx = self.f_posp_posm_posc(sentences, idx)
        self.fc6, idx = self.f_parent_middle_child(sentences, idx)
        self.fc7, idx = self.f_parent_bparent_child_bchild(sentences, idx)
        self.fc8, idx = self.f_parent_aparent_child_bchild(sentences, idx)
        self.fc9, idx = self.f_parent_bparent_child_achild(sentences, idx)
        self.fc10, idx = self.f_parent_aparent_child_achild(sentences, idx)
        self.fc11, idx = self.f_indices_distance(sentences, idx)
        self.fc12, idx = self.f_direction(sentences, idx)
        self.fc13, idx = self.f_parent_posp_child_posc(sentences, idx) # basic 7
        self.fc14, idx = self.f_parent_child_posc(sentences, idx)      # basic 9
        self.fc15, idx = self.f_parent_posp_child(sentences, idx)      # basic 11
        self.fc16, idx = self.f_parent_child(sentences, idx)           # baisc 12
        # self.fc17, idx = self.f_posg_posp_posc(sentences, idx)
        # self.fc18, idx = self.f_grandpa_parent_child(sentences, idx)
        # self.fc19, idx = self.f_posgg_posg_posp_posc(sentences, idx)
        # self.fc20, idx = self.f_grandgrandpa_grandpa_parent_child(sentences, idx)


        print("len:",len(self.fc1))
        print("len:",len(self.fc2))

        print("len:",len(self.fc3))
        print("len:",len(self.fc4))
        #
        # # print(self.fc1)
        # # print(self.fc2)
        # # print("")
        # print(self.fc3)
        # print(self.fc4)




        # print(len(self.f1))
        # # print(len(self.f2))
        # print(len(self.fc13))
        # print(len(self.fc14))
        # print(len(self.fc15))
        # print(len(self.fc16))
        # # print(len(self.f8))
        # print(len(self.f10))
        # print(len(self.f13))

        self.f_len = idx #length of feature vector
        print(self.f_len)
        self.f_dict = {}
        for d in (self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f8, self.f10, self.f13,
                  self.fc1, self.fc2, self.fc3, self.fc4, self.fc5, self.fc6, self.fc7, self.fc8,
                  self.fc9, self.fc10, self.fc11,self.fc12, self.fc13, self.fc14,
                  self.fc15, self.fc16 ): #,self.fc17, self.fc18):

            self.f_dict.update(d)

        # self.f_v_stats = self.stats(sentences, copy(self.f_dict))
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
        dic = {}
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
        dic = {}
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent[:-len(sentence.word_idx[parent])] not in dic:
                    dic.update({parent[:-len(sentence.word_idx[parent])]:num})
                    num += 1
        return dic, num

    # feature3: POS of parent word
    def f_posp(self, sentences, idx):
        dic = {}
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
        dic = {}
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
        dic = {}
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
        dic = {}
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
    def f_posp_posc_child(self, sentences, idx):
        dic = {}
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
        dic = {}
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
        dic = {}
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

    # feature c1: POS of parent + POS preceding of parent + POS of child + POS preceding of child
    def f_posp_posbp_posc_posbc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        # if int(sentence.word_idx[parent])-1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child])-1 != int(sentence.word_idx[parent]):
                            posp = sentence.word_pos[parent]
                            posc = sentence.word_pos[child]
                            posbp_idx = int(sentence.word_idx[parent]) - 1
                            if posbp_idx > 0:
                                posbp = sentence.word_pos[sentence.idx_word[str(posbp_idx)]]
                            posbc_idx = int(sentence.word_idx[child]) - 1
                            if posbc_idx > 0:
                                posbc = sentence.word_pos[sentence.idx_word[str(posbc_idx)]]
                            try:
                                if posbp!= "ROOT" and posbc!= "ROOT":

                                    if posp + posbp + posc + posbc not in dic:
                                        dic.update({posp + posbp + posc + posbc: num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c2: POS of parent + POS following of parent + POS of child + POS preceding of child
    def f_posp_posap_posc_posbc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        # if int(sentence.word_idx[parent]) - 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) - 1 != int(sentence.word_idx[parent])\
                        #         and int(sentence.word_idx[parent]) + 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) + 1 != int(sentence.word_idx[parent]):
                            posp = sentence.word_pos[parent]
                            posc = sentence.word_pos[child]

                            posap_idx = int(sentence.word_idx[parent]) + 1
                            if posap_idx < sentence.slen:
                                posap = sentence.word_pos[sentence.idx_word[str(posap_idx)]]
                            posbc_idx = int(sentence.word_idx[child]) - 1
                            if posbc_idx > 0:
                                posbc = sentence.word_pos[sentence.idx_word[str(posbc_idx)]]
                            try:
                                if posap != "ROOT" and posbc != "ROOT":
                                    if posp + posap + posc + posbc not in dic:
                                        dic.update({posp + posap + posc + posbc: num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c3: POS of parent + POS preceding of parent + POS of child + POS following of child
    def f_posp_posbp_posc_posac(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        posp = sentence.word_pos[parent]
                        posc = sentence.word_pos[child]

                        posbp_idx = int(sentence.word_idx[parent]) - 1
                        if posbp_idx >0:
                            posbp = sentence.word_pos[sentence.idx_word[str(posbp_idx)]]
                        posac_idx = int(sentence.word_idx[child]) + 1
                        if posac_idx < sentence.slen:
                            posac = sentence.word_pos[sentence.idx_word[str(posac_idx)]]
                        try:
                            if posbp != "ROOT" and posac != "ROOT":
                                if posp + posbp + posc + posac not in dic:
                                    dic.update({posp + posbp + posc + posac: num})
                                    num += 1
                        except:
                            pass
        return dic, num

    # feature c4: POS of parent + POS following of parent + POS of child + POS following of child
    def f_posp_posap_posc_posac(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0" and child:
                        posp = sentence.word_pos[parent]
                        posc = sentence.word_pos[child]
                        posap_idx = int(sentence.word_idx[parent]) + 1
                        if posap_idx < sentence.slen:
                            posap = sentence.word_pos[sentence.idx_word[str(posap_idx)]]
                        posac_idx = int(sentence.word_idx[child]) + 1
                        if posac_idx < sentence.slen:
                            posac = sentence.word_pos[sentence.idx_word[str(posac_idx)]]
                        try:
                            if posap != "ROOT" and posac != "ROOT":
                                if posp + posap + posc + posac not in dic:
                                    dic.update({posp + posap + posc + posac: num})
                                    num += 1
                        except:
                            pass
        return dic, num

    # feature c5: POS of parent + POS of middle word + POS of child
    def f_posp_posm_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        posp = sentence.word_pos[parent]
                        posc = sentence.word_pos[child]
                        start_idx = min(int(sentence.word_idx[parent]),int(sentence.word_idx[child]))
                        end_idx = max(int(sentence.word_idx[parent]),int(sentence.word_idx[child]))
                        for idx in range(start_idx+1,end_idx):
                            posm = sentence.word_pos[sentence.idx_word[str(idx)]]
                            if posp + posm + posc not in dic:
                                dic.update({posp + posm + posc: num})
                                num += 1
        return dic, num

    # feature c6: parent + middle word + child
    def f_parent_middle_child(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        start_idx = min(int(sentence.word_idx[parent]), int(sentence.word_idx[child]))
                        end_idx = max(int(sentence.word_idx[parent]), int(sentence.word_idx[child]))
                        for idx in range(start_idx + 1, end_idx):
                            middle = sentence.idx_word[str(idx)]
                            if parent[:-len(sentence.word_idx[parent])] + middle[:-len(sentence.word_idx[middle])] \
                                    + child[:-len(sentence.word_idx[child])] not in dic:
                                    dic.update({parent[:-len(sentence.word_idx[parent])] +
                                                            middle[:-len(sentence.word_idx[middle])] +
                                                            child[:-len(sentence.word_idx[child])]: num})
                                    num += 1
        return dic, num

    # feature c7: parent + preceding of parent + child +preceding of child
    def f_parent_bparent_child_bchild(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        bparent_idx = int(sentence.word_idx[parent]) - 1
                        if bparent_idx > 0:
                            bparent = sentence.idx_word[str(bparent_idx)]
                        bchild_idx = int(sentence.word_idx[child]) - 1
                        if bchild_idx > 0:
                            bchild = sentence.idx_word[str(bchild_idx)]
                        try:
                            if parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                    + child[:-len(sentence.word_idx[child])] + bchild[:-len(sentence.word_idx[bchild])] not in dic:
                                dic.update({parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                    + child[:-len(sentence.word_idx[child])] + bchild[:-len(sentence.word_idx[bchild])]: num})
                                num += 1
                        except:
                            pass
        return dic, num

    # feature c8:  parent + following of parent + child + preceding of child
    def f_parent_aparent_child_bchild(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        aparent_idx = int(sentence.word_idx[parent]) + 1
                        if aparent_idx < sentence.slen:
                            aparent = sentence.idx_word[str(aparent_idx)]
                        bchild_idx = int(sentence.word_idx[child]) - 1
                        if bchild_idx > 0:
                            bchild = sentence.idx_word[str(bchild_idx)]
                        try:
                            if parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                    + child[:-len(sentence.word_idx[child])] + bchild[
                                                                               :-len(sentence.word_idx[bchild])] not in dic:
                                dic.update(
                                    {parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                     + child[:-len(sentence.word_idx[child])] + bchild[
                                                                                :-len(sentence.word_idx[bchild])]: num})
                                num += 1
                        except:
                            pass
        return dic, num

    # feature c9: parent + preceding of parent + child + following of child
    def f_parent_bparent_child_achild(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    bparent_idx = int(sentence.word_idx[parent]) - 1
                    if bparent_idx > 0:
                        bparent = sentence.idx_word[str(bparent_idx)]
                    achild_idx = int(sentence.word_idx[child]) + 1
                    if achild_idx < sentence.slen:
                        achild = sentence.idx_word[str(achild_idx)]
                    try:
                        if parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                + child[:-len(sentence.word_idx[child])] + achild[
                                                                           :-len(sentence.word_idx[
                                                                                     achild])] not in dic:
                            dic.update(
                                {parent[:-len(sentence.word_idx[parent])] + bparent[
                                                                            :-len(sentence.word_idx[bparent])] \
                                 + child[:-len(sentence.word_idx[child])] + achild[
                                                                            :-len(sentence.word_idx[achild])]: num})
                            num += 1
                    except:
                        pass
        return dic, num

    # feature c10:  parent + following of parent + child + following of child
    def f_parent_aparent_child_achild(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        aparent_idx = int(sentence.word_idx[parent]) + 1
                        if aparent_idx < sentence.slen:
                            aparent = sentence.idx_word[str(aparent_idx)]
                        achild_idx = int(sentence.word_idx[child]) + 1
                        if achild_idx < sentence.slen:
                            achild = sentence.idx_word[str(achild_idx)]
                        try:
                            if parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                    + child[:-len(sentence.word_idx[child])] + achild[
                                                                               :-len(sentence.word_idx[
                                                                                         achild])] not in dic:
                                dic.update(
                                    {parent[:-len(sentence.word_idx[parent])] + aparent[
                                                                                :-len(sentence.word_idx[aparent])] \
                                     + child[:-len(sentence.word_idx[child])] + achild[
                                                                                :-len(sentence.word_idx[achild])]: num})
                                num += 1
                        except:
                            pass
        return dic, num

    # feature c11:  distance from parent to child
    def f_indices_distance(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    parent_idx = int(sentence.word_idx[parent])
                    child_idx = int(sentence.word_idx[child])
                    if abs(parent_idx - child_idx) not in dic:
                        dic.update({abs(parent_idx - child_idx): num})
                        num += 1
        return dic, num

    # feature c12:  edge direction from parent to child
    def f_direction(self, sentences, idx):
        dic = {}
        num = idx
        dic.update({"RRRR": num})
        num += 1
        dic.update({"LLLL": num})
        num += 1

        return dic, num


    # feature13:  parent word + POS of parent + child word + POS of child
    def f_parent_posp_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
                    if parent[:-len(sentence.word_idx[parent])] + posp +\
                            child[:-len(sentence.word_idx[child])] + posc not in dic:
                        dic.update({parent[:-len(sentence.word_idx[parent])] + posp +
                                    child[:-len(sentence.word_idx[child])] + posc: num})
                        num += 1
        return dic, num

    # feature14:  parent word + child word + POS of child
    def f_parent_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posc = sentence.word_pos[child]
                    if parent[:-len(sentence.word_idx[parent])] + \
                            child[:-len(sentence.word_idx[child])] + posc not in dic:
                        dic.update({parent[:-len(sentence.word_idx[parent])] +
                                    child[:-len(sentence.word_idx[child])] + posc: num})
                        num += 1
        return dic, num

    # feature15:  parent word + POS of parent + child word
    def f_parent_posp_child(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    if parent[:-len(sentence.word_idx[parent])] + posp + \
                            child[:-len(sentence.word_idx[child])] not in dic:
                        dic.update({parent[:-len(sentence.word_idx[parent])] + posp +
                                    child[:-len(sentence.word_idx[child])]: num})
                        num += 1
        return dic, num

    # feature16:  parent word  + child word
    def f_parent_child(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent[:-len(sentence.word_idx[parent])] + \
                            child[:-len(sentence.word_idx[child])] not in dic:
                        dic.update({parent[:-len(sentence.word_idx[parent])] +
                                    child[:-len(sentence.word_idx[child])]: num})
                        num += 1
        return dic, num

    # feature17: POS of father + POS of child + POS of grandson
    def f_posg_posp_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            posp = sentence.word_pos[parent]
                            posc = sentence.word_pos[child]
                            posg = sentence.word_pos[grandson]
                            if posp + posc + posg not in dic:
                                dic.update({posp + posc + posg: num})
                                num += 1
        return dic, num

    # feature18: father + child + grandson
    def f_grandpa_parent_child(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            son = child[:-len(sentence.word_idx[child])]
                            pap = parent[:-len(sentence.word_idx[parent])]
                            gran = grandson[:-len(sentence.word_idx[grandson])]
                            if pap + son + gran not in dic:
                                dic.update({pap + son + gran: num})
                                num += 1
        return dic, num

    # # feature19: POS of grandgrandpa + POS of grandpa + POS of father + POS of child
    # def f_posgg_posg_posp_posc(self, sentences, idx):
    #     dic = {}
    #     num = idx
    #     for sentence in sentences:
    #         for parent, children in sentence.word_children.items():
    #             for child in children:
    #                 if child in sentence.word_children:
    #                     for grandson in sentence.word_children[child]:
    #                         for grandgrandson in sentence.word_children[grandson]:
    #                             posp = sentence.word_pos[parent]
    #                             posc = sentence.word_pos[child]
    #                             posg = sentence.word_pos[grandson]
    #                             posgg = sentence.word_pos[grandgrandson]
    #                             if posp + posc + posg not in dic:
    #                                 dic.update({posp + posc + posg + posgg: num})
    #                                 num += 1
    #     return dic, num
    #
    # # feature20: grandgrandpa + grandpa + father + child
    # def f_grandgrandpa_grandpa_parent_child(self, sentences, idx):
    #     dic = {}
    #     num = idx
    #     for sentence in sentences:
    #         for parent, children in sentence.word_children.items():
    #             for child in children:
    #                 if child in sentence.word_children:
    #                     for grandson in sentence.word_children[child]:
    #                         for grandgrandson in sentence.word_children[grandson]:
    #                             granpa = child[:-len(sentence.word_idx[child])]
    #                             grangran = parent[:-len(sentence.word_idx[parent])]
    #                             pap = grandson[:-len(sentence.word_idx[grandson])]
    #                             son = grandgrandson[:-len(sentence.word_idx[grandgrandson])]
    #                             if grangran + granpa + pap + son not in dic:
    #                                 dic.update({grangran + granpa + pap + son: num})
    #                                 num += 1
    #     return dic, num

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
                try:
                    #f13: posp + posc
                    index_vec[self.f_dict[posp + posc]] += 1
                except:
                    pass

                if mode == "C":
                    posbp_idx = int(word_idx[parent]) - 1
                    if posbp_idx > 0:
                        bparent = idx_word[str(posbp_idx)][:-len(str(posbp_idx))]
                        posbp = word_pos[idx_word[str(posbp_idx)]]
                    posbc_idx = int(word_idx[child]) - 1
                    if posbc_idx > 0:
                        bchild = idx_word[str(posbc_idx)][:-len(str(posbc_idx))]
                        posbc = word_pos[idx_word[str(posbc_idx)]]
                    posap_idx = int(word_idx[parent]) + 1
                    if posap_idx <slen:
                        aparent = idx_word[str(posap_idx)][:-len(str(posap_idx))]
                        posap = word_pos[idx_word[str(posap_idx)]]
                    posac_idx = int(word_idx[child]) + 1
                    if posac_idx <slen:
                        achild = idx_word[str(posac_idx)][:-len(str(posac_idx))]
                        posac = word_pos[idx_word[str(posac_idx)]]

                    try:
                        # fc1: posp + posbp + posc + posbc
                        index_vec[self.f_dict[posp + posbp + posc + posbc]] += 1
                    except:
                        pass

                    try:
                        # fc2: posp + posap + posc + posbc
                        index_vec[self.f_dict[posp + posap + posc + posbc]] += 1
                    except:
                        pass

                    try:
                        # fc3: posp + posbp + posc + posac
                        index_vec[self.f_dict[posp + posbp + posc + posac]] += 1
                    except:
                        pass

                    try:
                        # fc4: posp + posap + posc + posac
                        index_vec[self.f_dict[posp + posap + posc + posac]] += 1
                    except:
                        pass

                    start_idx = min(int(word_idx[parent]), int(word_idx[child]))
                    end_idx = max(int(word_idx[parent]), int(word_idx[child]))
                    for idx in range(start_idx + 1, end_idx):
                        middle = idx_word[str(idx)]
                        posm = word_pos[middle]
                        try:
                            # fc5: posp + posm + posc
                            index_vec[self.f_dict[posp + posm + posc]] += 1
                        except:
                            pass
                        try:
                            # fc6: parent + middle + child
                            index_vec[self.f_dict[parent[:-len(word_idx[parent])]+
                                                  middle[:-len(word_idx[middle])] +
                                                  child[:-len(word_idx[child])]]] += 1
                        except:
                            pass


                    try:
                        # fc7: parent + bparent + child + bchild
                        index_vec[self.f_dict[parent + bparent + child + bchild]] += 1
                    except:
                        pass

                    try:
                        # fc8: parent + aparent + child + bchild
                        index_vec[self.f_dict[parent + aparent + child + bchild]] += 1
                    except:
                        pass

                    try:
                        # fc9: parent + bparent + child + achild
                        index_vec[self.f_dict[parent + bparent + child + achild]] += 1
                    except:
                        pass

                    try:
                        # fc10: parent + aparent + child + achild
                        index_vec[self.f_dict[parent + aparent + child + achild]] += 1
                    except:
                        pass

                    distance = (int(word_idx[parent]) - int(word_idx[child]))
                    try:
                        # fc11: distance
                        index_vec[self.f_dict[abs(distance)]] += 1
                    except:
                        pass

                    direction = "LLLL" if distance > 0 else "RRRR"
                    try:
                        # fc12: direction
                        index_vec[self.f_dict[direction]] += 1
                    except:
                        pass


                    try:
                        # fc13: parent + posp + child + posc
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp +
                                              child[:-len(word_idx[child])] + posc]] += 1
                    except:
                        pass

                    try:
                        # fc14: parent  + child + posc
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                              child[:-len(word_idx[child])] + posc]] += 1
                    except:
                        pass

                    try:
                        # fc15: parent + posp + child
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp +
                                              child[:-len(word_idx[child])]]] += 1
                    except:
                        pass

                    try:
                        # fc16: parent + child
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                              child[:-len(word_idx[child])]]] += 1
                    except:
                        pass

                    try:
                        grandsons = word_children[child]
                        for grandson in grandsons:
                            posg = word_pos[grandson]
                            try:
                                # fc17: posg + posp + posc
                                index_vec[self.f_dict[posp + posc + posg]] += 1
                            except:
                                pass

                            try:
                                # fc18: parent + child + grandson
                                index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                                      child[:-len(word_idx[child])] +
                                                      grandson[:-len(word_idx[grandson])]]] += 1
                            except:
                                pass
                    except:
                        pass






        return index_vec
