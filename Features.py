import numpy as np


class Features:

    def __init__(self, sentences):
        idx = 0.0
        self.f1, idx = self.f_parent_posp(sentences,idx)
        print(self.f1)
        self.f2, idx = self.f_parent(sentences,idx)
        self.f3, idx = self.f_posp(sentences, idx)
        self.f4, idx = self.f_child_posc(sentences,idx)
        self.f5, idx = self.f_child(sentences,idx)
        self.f6, idx = self.f_posc(sentences,idx)
        self.f8, idx = self.f_parent_child_posc(sentences,idx)
        self.f10, idx = self.f_parent_posp_posc(sentences,idx)
        self.f13, idx = self.f_posp_posc(sentences,idx)

        self.f_len = idx-1
        self.features_v = {}
        for d in (self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f8, self.f10, self.f13):
            self.features_v.update(d)

    #feature1: parent word + pos(parent)
    def f_parent_posp(self,sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent in sentence.word_children.keys():
                if parent+sentence.word_pos[parent] not in dic:
                    dic.update({parent+sentence.word_pos[parent]:num})
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
                if sentence.word_pos[parent] not in dic:
                    dic.update({sentence.word_pos[parent]: num})
                    num += 1
        return dic, num

    # feature4: child word + pos(parent)
    def f_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent,children in sentence.word_children.items():
                for child in children:
                    if child + sentence.word_pos[child] not in dic:
                        dic.update({child + sentence.word_pos[child]: num})
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
                    if sentence.word_pos[child] not in dic:
                        dic.update({sentence.word_pos[child]: num})
                        num += 1
        return dic, num

    # feature8: parent word + child word + POS of child
    def f_parent_child_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent+child+sentence.word_pos[child] not in dic:
                        dic.update({parent+child+sentence.word_pos[child]: num})
                        num += 1
        return dic, num

    # feature10: parent word + POS of parent + POS of child
    def f_parent_posp_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if parent + sentence.word_pos[parent] + sentence.word_pos[child] not in dic:
                        dic.update({parent + sentence.word_pos[parent] + sentence.word_pos[child]: num})
                        num += 1
        return dic, num

    # feature13: POS of parent + POS of child
    def f_posp_posc(self, sentences, idx):
        dic = {}
        num = idx
        for sentence in sentences:
            for parent, children in sentence.word_children.items():
                for child in children:
                    if sentence.word_pos[parent] + sentence.word_pos[child] not in dic:
                        dic.update({sentence.word_pos[parent] + sentence.word_pos[child]: num})
                        num += 1
        return dic, num


