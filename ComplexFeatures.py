import numpy as np
from copy import copy
import utils
import collections
from main import  *

class CFeatures:

    def __init__(self, sentences):

        #preprocessing
        self.wordcounts = collections.OrderedDict()
        self.countwords(sentences)
        # print(self.wordcounts)
        self.filtered = []
        self.filterwords()
        print(self.filtered)


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
        self.fc17, idx = self.f_posg_posp_posc(sentences, idx)
        self.fc18, idx = self.f_grandpa_parent_child(sentences, idx)
        self.fc19, idx = self.f_posgg_posg_posp_posc(sentences, idx)
        self.fc20, idx = self.f_grandgrandpa_grandpa_parent_child(sentences, idx)
        self.fc21, idx = self.f_posp_posc1_posc2(sentences, idx)
        self.fc22, idx = self.f_parent_posp_posc1_posc2(sentences, idx)
        self.fc23, idx = self.f_posp_posc1_posc2_child(sentences, idx)

        self.f_len = idx #length of feature vector
        # print(self.f_len)
        self.f_dict = collections.OrderedDict()
        feat_list = []
        for d in (self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f8, self.f10, self.f13,
                  self.fc1, self.fc2, self.fc3, self.fc4, self.fc5, self.fc6,
                  self.fc7, self.fc8, self.fc9, self.fc10, self.fc11,self.fc12,
                  self.fc13, self.fc14, self.fc15, self.fc16 ,
                  self.fc17, self.fc18, self.fc19, self.fc20,
                  self.fc21, self.fc22, self.fc23):

            self.f_dict.update(d)

        # # print(self.f_dict)
        # with open("aaa", 'w') as file:
        #     for d in self.f_dict:
        #         file.write(d+": "+str(self.f_dict[d])+"\n")

        # self.f_v_stats = self.stats(sentences, copy(self.f_dict))
        # print(self.f_v_stats)
        # self.refine(utils.THRESHOLD)

    def countwords(self, sentences):

        for sentence in sentences:
            for i,word in sentence.idx_word.items():
                if word[:-len(sentence.word_idx[word])] not in self.wordcounts:
                    self.wordcounts.update({word[:-len(sentence.word_idx[word])]:1})
                else:
                    self.wordcounts[word[:-len(sentence.word_idx[word])]] +=1

    def filterwords(self):
        for word,val in self.wordcounts.items():
            if val >= utils.THRESHOLD :
                self.filtered.append(word)






    #feature1: parent word + pos(parent)
    def f_parent_posp(self,sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent != "ROOT0":
                    pos = sentence.word_pos[parent]
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered:
                        if parent[:-len(sentence.word_idx[parent])]+pos + "f1" not in dic:
                            dic.update({parent[:-len(sentence.word_idx[parent])]+pos + "f1":num})
                            num += 1
        return dic, num

    #feature2: parent word
    def f_parent(self,sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent[:-len(sentence.word_idx[parent])] in self.filtered:
                    if parent[:-len(sentence.word_idx[parent])] + "f2" not in dic:
                        dic.update({parent[:-len(sentence.word_idx[parent])] + "f2":num})
                        num += 1
        return dic, num

    # feature3: POS of parent word
    def f_posp(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                pos = sentence.word_pos[parent]
                if pos + "f3"not in dic:
                    dic.update({pos + "f3": num})
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
                    if child[:-len(sentence.word_idx[child])] in self.filtered:
                        if child[:-len(sentence.word_idx[child])] + pos + "f4" not in dic:
                            dic.update({child[:-len(sentence.word_idx[child])] + pos + "f4": num})
                            num += 1
        return dic, num

    # feature5: child word
    def f_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child[:-len(sentence.word_idx[child])] in self.filtered:
                        if child[:-len(sentence.word_idx[child])] + "f5" not in dic:
                            dic.update({child[:-len(sentence.word_idx[child])] + "f5": num})
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
                    if pos + "f6" not in dic:
                        dic.update({pos + "f6": num})
                        num += 1
        return dic, num

    # feature8:  POS of parent + POS of child + child word
    def f_posp_posc_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
                    if child[:-len(sentence.word_idx[child])] in self.filtered:
                        if posp+posc+child[:-len(sentence.word_idx[child])] + "f8" not in dic:
                            dic.update({posp+posc+child[:-len(sentence.word_idx[child])] + "f8": num})
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
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered:
                        if posp + posc + parent[:-len(sentence.word_idx[parent])] + "f10" not in dic:
                            dic.update({posp + posc + parent[:-len(sentence.word_idx[parent])] + "f10": num})
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
                    if posp + posc + "f13"not in dic:
                        dic.update({posp + posc + "f13": num})
                        num += 1
        return dic, num

    # feature c1: POS of parent + POS preceding of parent + POS of child + POS preceding of child
    def f_posp_posbp_posc_posbc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        # if int(sentence.word_idx[parent]) - 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) - 1 != int(sentence.word_idx[parent]) \
                        #         and int(sentence.word_idx[parent]) + 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) + 1 != int(sentence.word_idx[parent]):
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

                                    if posp + posbp + posc + posbc + "c1" not in dic:
                                        dic.update({posp + posbp + posc + posbc + "c1": num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c2: POS of parent + POS following of parent + POS of child + POS preceding of child
    def f_posp_posap_posc_posbc(self, sentences, idx):
        dic = collections.OrderedDict()
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
                                    if posp + posap + posc + posbc + "c2" not in dic:
                                        dic.update({posp + posap + posc + posbc + "c2" : num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c3: POS of parent + POS preceding of parent + POS of child + POS following of child
    def f_posp_posbp_posc_posac(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        # if int(sentence.word_idx[parent]) - 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) - 1 != int(sentence.word_idx[parent]) \
                        #         and int(sentence.word_idx[parent]) + 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) + 1 != int(sentence.word_idx[parent]):
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
                                    if posp + posbp + posc + posac + "c3" not in dic:
                                        dic.update({posp + posbp + posc + posac+ "c3" : num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c4: POS of parent + POS following of parent + POS of child + POS following of child
    def f_posp_posap_posc_posac(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0" and child:
                        # if int(sentence.word_idx[parent]) - 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) - 1 != int(sentence.word_idx[parent]) \
                        #         and int(sentence.word_idx[parent]) + 1 != int(sentence.word_idx[child]) \
                        #         and int(sentence.word_idx[child]) + 1 != int(sentence.word_idx[parent]):
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
                                    if posp + posap + posc + posac + "c4" not in dic:
                                        dic.update({posp + posap + posc + posac+ "c4" : num})
                                        num += 1
                            except:
                                pass
        return dic, num

    # feature c5: POS of parent + POS of middle word + POS of child
    def f_posp_posm_posc(self, sentences, idx):
        dic = collections.OrderedDict()
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
                            if posp + posm + posc + "c5" not in dic:
                                dic.update({posp + posm + posc+ "c5" : num})
                                num += 1
        return dic, num

    # feature c6: parent + middle word + child
    def f_parent_middle_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent != "ROOT0":
                        start_idx = min(int(sentence.word_idx[parent]), int(sentence.word_idx[child]))
                        end_idx = max(int(sentence.word_idx[parent]), int(sentence.word_idx[child]))
                        for idx in range(start_idx + 1, end_idx):
                            middle = sentence.idx_word[str(idx)]
                            if parent[:-len(sentence.word_idx[parent])] in self.filtered and\
                                            middle[:-len(sentence.word_idx[middle])] in self.filtered and\
                                            child[:-len(sentence.word_idx[child])] in self.filtered:
                                if parent[:-len(sentence.word_idx[parent])] + middle[:-len(sentence.word_idx[middle])] \
                                        + child[:-len(sentence.word_idx[child])] + "c6"  not in dic:
                                        dic.update({parent[:-len(sentence.word_idx[parent])] +
                                                                middle[:-len(sentence.word_idx[middle])] +
                                                                child[:-len(sentence.word_idx[child])] + "c6" : num})
                                        num += 1
        return dic, num

    # feature c7: parent + preceding of parent + child +preceding of child
    def f_parent_bparent_child_bchild(self, sentences, idx):
        dic = collections.OrderedDict()
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
                            if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                            bparent[:-len(sentence.word_idx[bparent])]in self.filtered and \
                                            child[:-len(sentence.word_idx[child])] in self.filtered and \
                                            bchild[:-len(sentence.word_idx[bchild])]  in self.filtered:
                                if parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                        + child[:-len(sentence.word_idx[child])] + bchild[:-len(sentence.word_idx[bchild])] + "c7" not in dic:
                                    dic.update({parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                        + child[:-len(sentence.word_idx[child])] + bchild[:-len(sentence.word_idx[bchild])] + "c7" : num})
                                    num += 1
                        except:
                            pass
        return dic, num

    # feature c8:  parent + following of parent + child + preceding of child
    def f_parent_aparent_child_bchild(self, sentences, idx):
        dic = collections.OrderedDict()
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
                            if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                            aparent[:-len(sentence.word_idx[aparent])] in self.filtered and \
                                            child[:-len(sentence.word_idx[child])] in self.filtered and \
                                            bchild[:-len(sentence.word_idx[bchild])] in self.filtered:
                                if parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                        + child[:-len(sentence.word_idx[child])] + bchild[
                                                                                   :-len(sentence.word_idx[bchild])] + "c8"  not in dic:
                                    dic.update(
                                        {parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                         + child[:-len(sentence.word_idx[child])] + bchild[
                                                                                    :-len(sentence.word_idx[bchild])] + "c8" : num})
                                    num += 1
                        except:
                            pass
        return dic, num

    # feature c9: parent + preceding of parent + child + following of child
    def f_parent_bparent_child_achild(self, sentences, idx):
        dic = collections.OrderedDict()
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
                        if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                        bparent[:-len(sentence.word_idx[bparent])] in self.filtered and \
                                        child[:-len(sentence.word_idx[child])] in self.filtered and \
                                        achild[:-len(sentence.word_idx[achild])] in self.filtered:
                            if parent[:-len(sentence.word_idx[parent])] + bparent[:-len(sentence.word_idx[bparent])] \
                                    + child[:-len(sentence.word_idx[child])] + achild[
                                                                               :-len(sentence.word_idx[
                                                                                         achild])] + "c9" not in dic:
                                dic.update(
                                    {parent[:-len(sentence.word_idx[parent])] + bparent[
                                                                                :-len(sentence.word_idx[bparent])] \
                                     + child[:-len(sentence.word_idx[child])] + achild[
                                                                                :-len(sentence.word_idx[achild])]+ "c9" : num})
                                num += 1
                    except:
                        pass
        return dic, num

    # feature c10:  parent + following of parent + child + following of child
    def f_parent_aparent_child_achild(self, sentences, idx):
        dic = collections.OrderedDict()
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
                            if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                            aparent[:-len(sentence.word_idx[aparent])] in self.filtered and \
                                            child[:-len(sentence.word_idx[child])] in self.filtered and \
                                            achild[:-len(sentence.word_idx[achild])] in self.filtered:
                                if parent[:-len(sentence.word_idx[parent])] + aparent[:-len(sentence.word_idx[aparent])] \
                                        + child[:-len(sentence.word_idx[child])] + achild[
                                                                                   :-len(sentence.word_idx[
                                                                                             achild])] + "c10" not in dic:
                                    dic.update(
                                        {parent[:-len(sentence.word_idx[parent])] + aparent[
                                                                                    :-len(sentence.word_idx[aparent])] \
                                         + child[:-len(sentence.word_idx[child])] + achild[
                                                                                    :-len(sentence.word_idx[achild])]+ "c10" : num})
                                    num += 1
                        except:
                            pass
        return dic, num

    # feature c11:  distance from parent to child
    def f_indices_distance(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    parent_idx = int(sentence.word_idx[parent])
                    child_idx = int(sentence.word_idx[child])
                    if str(abs(parent_idx - child_idx)) + "c11" not in dic:
                        dic.update({str(abs(parent_idx - child_idx)) + "c11" : num})
                        num += 1
        return dic, num

    # feature c12:  edge direction from parent to child
    def f_direction(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        dic.update({"RRRR": num})
        num += 1
        dic.update({"LLLL": num})
        num += 1

        return dic, num


    # feature13:  parent word + POS of parent + child word + POS of child
    def f_parent_posp_child_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    posc = sentence.word_pos[child]
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                    child[:-len(sentence.word_idx[child])] in self.filtered:
                        if parent[:-len(sentence.word_idx[parent])] + posp +\
                                child[:-len(sentence.word_idx[child])] + posc + "c13" not in dic:
                            dic.update({parent[:-len(sentence.word_idx[parent])] + posp +
                                        child[:-len(sentence.word_idx[child])] + posc + "c13" : num})
                            num += 1
        return dic, num

    # feature14:  parent word + child word + POS of child
    def f_parent_child_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posc = sentence.word_pos[child]
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                    child[:-len(sentence.word_idx[child])] in self.filtered:
                        if parent[:-len(sentence.word_idx[parent])] + \
                                child[:-len(sentence.word_idx[child])] + posc+ "c14"  not in dic:
                            dic.update({parent[:-len(sentence.word_idx[parent])] +
                                        child[:-len(sentence.word_idx[child])] + posc + "c14" : num})
                            num += 1
        return dic, num

    # feature15:  parent word + POS of parent + child word
    def f_parent_posp_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    posp = sentence.word_pos[parent]
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                    child[:-len(sentence.word_idx[child])] in self.filtered:
                        if parent[:-len(sentence.word_idx[parent])] + posp + \
                                child[:-len(sentence.word_idx[child])] + "c15"  not in dic:
                            dic.update({parent[:-len(sentence.word_idx[parent])] + posp +
                                        child[:-len(sentence.word_idx[child])] + "c15" : num})
                            num += 1
        return dic, num

    # feature16:  parent word  + child word
    def f_parent_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent[:-len(sentence.word_idx[parent])] in self.filtered and \
                                    child[:-len(sentence.word_idx[child])] in self.filtered:
                        if parent[:-len(sentence.word_idx[parent])] + \
                                child[:-len(sentence.word_idx[child])] + "c16"  not in dic:
                            dic.update({parent[:-len(sentence.word_idx[parent])] +
                                        child[:-len(sentence.word_idx[child])] + "c16" : num})
                            num += 1
        return dic, num

    # feature17: POS of father + POS of child + POS of grandson
    def f_posg_posp_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            posp = sentence.word_pos[parent]
                            posc = sentence.word_pos[child]
                            posg = sentence.word_pos[grandson]
                            if posp + posc + posg + "c17" not in dic:
                                dic.update({posp + posc + posg + "c17" : num})
                                num += 1
        return dic, num

    # feature18: father + child + grandson
    def f_grandpa_parent_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            son = child[:-len(sentence.word_idx[child])]
                            pap = parent[:-len(sentence.word_idx[parent])]
                            gran = grandson[:-len(sentence.word_idx[grandson])]
                            if pap in self.filtered and \
                                    son in self.filtered and \
                                    gran in self.filtered:
                                if pap + son + gran + "c18" not in dic:
                                    dic.update({pap + son + gran + "c18": num})
                                    num += 1
        return dic, num

    # feature19: POS of grandgrandpa + POS of grandpa + POS of father + POS of child
    def f_posgg_posg_posp_posc(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            if grandson in sentence.word_children:
                                for grandgrandson in sentence.word_children[grandson]:
                                    posp = sentence.word_pos[parent]
                                    posc = sentence.word_pos[child]
                                    posg = sentence.word_pos[grandson]
                                    posgg = sentence.word_pos[grandgrandson]
                                    if posp + posc + posg + posgg + "c19" not in dic:
                                        dic.update({posp + posc + posg + posgg + "c19": num})
                                        num += 1
        return dic, num

    # feature20: grandgrandpa + grandpa + father + child
    def f_grandgrandpa_grandpa_parent_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if child in sentence.word_children:
                        for grandson in sentence.word_children[child]:
                            if grandson in sentence.word_children:
                                for grandgrandson in sentence.word_children[grandson]:
                                    son = child[:-len(sentence.word_idx[child])]
                                    pap = parent[:-len(sentence.word_idx[parent])]
                                    gran = grandson[:-len(sentence.word_idx[grandson])]
                                    grangran = grandgrandson[:-len(sentence.word_idx[grandgrandson])]
                                    if pap in self.filtered and \
                                                    son in self.filtered and \
                                                    gran in self.filtered and \
                                                    grangran in self.filtered:
                                        if pap + son + gran + grangran+ "c20" not in dic:
                                            dic.update({pap + son + gran +grangran + "c20": num})
                                            num += 1
        return dic, num

    # feature21: POS of parent + POS of child1 + POS of child2
    def f_posp_posc1_posc2(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child1 in children:
                    for child2 in children:
                        posp = sentence.word_pos[parent]
                        if sentence.word_idx[child1] != sentence.word_idx[child2]:
                            posc1 = sentence.word_pos[child1]
                            posc2 = sentence.word_pos[child2]
                            if posp + posc1 + posc2 + "f21" not in dic:
                                dic.update({posp + posc1 + posc2 + "f21": num})
                                num += 1
        return dic, num

    # feature22: parent + POS of parent + POS of child1 + POS of child2
    def f_parent_posp_posc1_posc2(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child1 in children:
                    for child2 in children:
                        posp = sentence.word_pos[parent]
                        if sentence.word_idx[child1] != sentence.word_idx[child2]:
                            posc1 = sentence.word_pos[child1]
                            posc2 = sentence.word_pos[child2]
                            pap = parent[:-len(sentence.word_idx[parent])]
                            if pap in self.filtered:
                                if pap + posp + posc1 + posc2 + "f22" not in dic:
                                    dic.update({pap + posp + posc1 + posc2 + "f22": num})
                                    num += 1
        return dic, num

    # feature23: POS of parent + POS of child1 + POS of child2 + child1
    def f_posp_posc1_posc2_child(self, sentences, idx):
        dic = collections.OrderedDict()
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child1 in children:
                    for child2 in children:
                        posp = sentence.word_pos[parent]
                        if sentence.word_idx[child1] != sentence.word_idx[child2]:
                            posc1 = sentence.word_pos[child1]
                            posc2 = sentence.word_pos[child2]
                            son = child2[:-len(sentence.word_idx[child2])]
                            if son in self.filtered:
                                if posp + posc1 + posc2 + son + "f23" not in dic:
                                    dic.update({posp + posc1 + posc2 + son + "f23": num})
                                    num += 1
        return dic, num

    # # feature24: POS of parent + POS of child1 + POS of child2 + POS of child3
    # def f_posp_posc1_posc2_posc3(self, sentences, idx):
    #     dic = collections.OrderedDict()
    #     num = idx
    #     for sentence in sentences:
    #         for parent, children in sentence.word_children.items():
    #             for child1 in children:
    #                 for child2 in children:
    #                     for
    #                     posp = sentence.word_pos[parent]
    #                     if sentence.word_idx[child1] != sentence.word_idx[child2]:
    #                         posc1 = sentence.word_pos[child1]
    #                         posc2 = sentence.word_pos[child2]
    #                         if posp + posc1 + posc2 + "f21" not in dic:
    #                             dic.update({posp + posc1 + posc2 + "f21": num})
    #                             num += 1
    #     return dic, num
    #
    # # feature25: parent + POS of parent + POS of child1 + POS of child2
    # def f_parent_posp_posc1_posc2(self, sentences, idx):
    #     dic = collections.OrderedDict()
    #     num = idx
    #     for sentence in sentences:
    #         for parent, children in sentence.word_children.items():
    #             for child1 in children:
    #                 for child2 in children:
    #                     posp = sentence.word_pos[parent]
    #                     if sentence.word_idx[child1] != sentence.word_idx[child2]:
    #                         posc1 = sentence.word_pos[child1]
    #                         posc2 = sentence.word_pos[child2]
    #                         pap = parent[:-len(sentence.word_idx[parent])]
    #                         if pap in self.filtered:
    #                             if pap + posp + posc1 + posc2 + "f22" not in dic:
    #                                 dic.update({pap + posp + posc1 + posc2 + "f22": num})
    #                                 num += 1
    #     return dic, num
    #
    # # feature26: POS of parent + POS of child1 + POS of child2 + child1
    # def f_posp_posc1_posc2_child(self, sentences, idx):
    #     dic = collections.OrderedDict()
    #     num = idx
    #     for sentence in sentences:
    #         for parent, children in sentence.word_children.items():
    #             for child1 in children:
    #                 for child2 in children:
    #                     posp = sentence.word_pos[parent]
    #                     if sentence.word_idx[child1] != sentence.word_idx[child2]:
    #                         posc1 = sentence.word_pos[child1]
    #                         posc2 = sentence.word_pos[child2]
    #                         son = child2[:-len(sentence.word_idx[child2])]
    #                         if son in self.filtered:
    #                             if posp + posc1 + posc2 + son + "f23" not in dic:
    #                                 dic.update({posp + posc1 + posc2 + son + "f23": num})
    #                                 num += 1
    #     return dic, num


    def f_xy(self,word_children, word_pos, word_idx, idx_word,slen,mode):
        index_vec = np.zeros(self.f_len)

        for parent, children in word_children.items():
            for child in children:

                posp = word_pos[parent]
                try:
                    #f1: parent +posp
                    index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp + "f1"]] += 1
                except:
                    pass
                try:
                    #f3: posp
                    index_vec[self.f_dict[posp+ "f3"]] += 1
                except:
                    pass
                try:
                    #f2: parent
                    index_vec[self.f_dict[parent[:-len(word_idx[parent])]+ "f2"]] += 1
                except:
                    pass
                try:
                    #f5 child
                    index_vec[self.f_dict[child[:-len(word_idx[child])]+ "f5"]] += 1
                except:
                    pass
                posc = word_pos[child]
                try:
                    #f4: child +posc
                    index_vec[self.f_dict[child[:-len(word_idx[child])] + posc]+ "f4"] += 1
                except:
                    pass
                try:
                    #f6: posc
                    index_vec[self.f_dict[posc+ "f6"]] += 1
                except:
                    pass
                try:
                    #f8: posp + posc + child
                    index_vec[self.f_dict[posp + posc + child[:-len(word_idx[child])]+ "f8"]] += 1
                except:
                    pass
                try:
                    #f10: posp + posc + parent
                    index_vec[self.f_dict[posp + posc+ parent[:-len(word_idx[parent])]]+ "f10"] += 1
                except:
                    pass
                try:
                    #f13: posp + posc
                    index_vec[self.f_dict[posp + posc+ "f13"]] += 1
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
                        index_vec[self.f_dict[posp + posbp + posc + posbc + "c1"]] += 1
                    except:
                        pass

                    try:
                        # fc2: posp + posap + posc + posbc
                        index_vec[self.f_dict[posp + posap + posc + posbc+ "c2"]] += 1
                    except:
                        pass

                    try:
                        # fc3: posp + posbp + posc + posac
                        index_vec[self.f_dict[posp + posbp + posc + posac+ "c3"]] += 1
                    except:
                        pass

                    try:
                        # fc4: posp + posap + posc + posac
                        index_vec[self.f_dict[posp + posap + posc + posac+ "c4"]] += 1
                    except:
                        pass

                    start_idx = min(int(word_idx[parent]), int(word_idx[child]))
                    end_idx = max(int(word_idx[parent]), int(word_idx[child]))
                    for idx in range(start_idx + 1, end_idx):
                        middle = idx_word[str(idx)]
                        posm = word_pos[middle]
                        try:
                            # fc5: posp + posm + posc
                            index_vec[self.f_dict[posp + posm + posc+ "c5"]] += 1
                        except:
                            pass
                        try:
                            # fc6: parent + middle + child
                            index_vec[self.f_dict[parent[:-len(word_idx[parent])]+
                                                  middle[:-len(word_idx[middle])] +
                                                  child[:-len(word_idx[child])]+ "c6"]] += 1
                        except:
                            pass


                    try:
                        # fc7: parent + bparent + child + bchild
                        index_vec[self.f_dict[parent + bparent + child + bchild+ "c7"]] += 1
                    except:
                        pass

                    try:
                        # fc8: parent + aparent + child + bchild
                        index_vec[self.f_dict[parent + aparent + child + bchild+ "c8"]] += 1
                    except:
                        pass

                    try:
                        # fc9: parent + bparent + child + achild
                        index_vec[self.f_dict[parent + bparent + child + achild+ "c9"]] += 1
                    except:
                        pass

                    try:
                        # fc10: parent + aparent + child + achild
                        index_vec[self.f_dict[parent + aparent + child + achild+ "c10"]] += 1
                    except:
                        pass

                    distance = (int(word_idx[parent]) - int(word_idx[child]))
                    try:
                        # fc11: distance
                        index_vec[self.f_dict[str(abs(distance))+ "c11"]] += 1
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
                                              child[:-len(word_idx[child])] + posc]+ "c13"] += 1
                    except:
                        pass

                    try:
                        # fc14: parent  + child + posc
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                              child[:-len(word_idx[child])] + posc+ "c14"]] += 1
                    except:
                        pass

                    try:
                        # fc15: parent + posp + child
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp +
                                              child[:-len(word_idx[child])]]+ "c15"] += 1
                    except:
                        pass

                    try:
                        # fc16: parent + child
                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                              child[:-len(word_idx[child])]+ "c16"]] += 1
                    except:
                        pass

                    try:
                        grandsons = word_children[child]
                        for grandson in grandsons:
                            posg = word_pos[grandson]
                            try:
                                # fc17: posg + posp + posc
                                index_vec[self.f_dict[posp + posc + posg+ "c17"]] += 1
                            except:
                                pass

                            try:
                                # fc18: parent + child + grandson
                                index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                                      child[:-len(word_idx[child])] +
                                                      grandson[:-len(word_idx[grandson])]+ "c18"]] += 1
                            except:
                                pass

                            try:
                                grandgrandsons = word_children[grandson]

                                for grandgrandson in grandgrandsons:
                                    posgg = word_pos[grandgrandson]

                                    try:
                                        # fc19:posp + posc + posg + posgg
                                        index_vec[self.f_dict[posp + posc + posg + posgg + "c19"]] += 1
                                    except:
                                        pass

                                    try:
                                        # fc20: parent + child + grandson + grandgrandson
                                        index_vec[self.f_dict[parent[:-len(word_idx[parent])] +
                                                              child[:-len(word_idx[child])] +
                                                              grandson[:-len(word_idx[grandson])] +
                                                              grandgrandson[:-len(word_idx[grandgrandson])] + "c20"]] += 1
                                    except:
                                        pass

                            except:
                                pass

                    except:
                        pass

                    for child2 in children:
                        if word_idx[child] != word_idx[child2]:
                            posc2 = word_pos[child2]

                            try:
                                # fc21:posp + posc + posc2
                                index_vec[self.f_dict[posp + posc + posc2 + "c21"]] += 1
                            except:
                                pass

                            try:
                                # fc22:father + posp + posc + posc2
                                index_vec[self.f_dict[parent[:-len(word_idx[parent])] + posp + posc + posc2 + "c22"]] += 1
                            except:
                                pass

                            try:
                                # fc23:posp + posc + posc2 + child
                                index_vec[self.f_dict[posp + posc + posc2 + child2[:-len(word_idx[child2])] + "c23"]] += 1
                            except:
                                pass


        return index_vec
