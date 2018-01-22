import collections
class Sentence:

    def __init__(self, slist):

        self.word_idx = collections.OrderedDict() # insert word, get index of word in sentence  ###dic
        self.idx_word = collections.OrderedDict() # insert index in sentence, get word at index ###dic
        self.word_pos = collections.OrderedDict() # inser word get POS                          ###dic
        self.word_children = collections.OrderedDict() # insert word, get all childre words     ###dic of lists
        self.parent_child = []
        self.word_children_inf = []
        self.idx_word_unlowered = collections.OrderedDict()
        # sentence.idx_word[idx][:-len(idx)]

        #update indices and POS
        for i,word in enumerate(slist):
            self.idx_word_unlowered.update({word[0]: word[4]})
            self.idx_word.update({word[0]: word[1]+word[0]})
            self.word_idx.update({word[1]+word[0]: word[0]})
            self.word_pos.update({word[1]+word[0]:word[2]})
            if word[3] == '0':
                self.word_children.update({"ROOT0": [word[1]+word[0]]})
        self.idx_word.update({'0': "ROOT0"})
        self.word_idx.update({"ROOT0": '0'})
        self.word_pos.update({"ROOT0": "ROOT"})

        #length of sentence
        self.slen = len(self.idx_word)

        #update parents and children
        for i, word in enumerate(slist):
            if word[3] == '0':
                continue
            if self.idx_word[word[3]] not in self.word_children:
                self.word_children.update({self.idx_word[word[3]]: []})
            self.word_children[self.idx_word[word[3]]].append(word[1]+word[0])

        for parent in self.word_children:
            for child in self.word_children[parent]:
                self.parent_child.append(parent+child)

        # print(self.word_children)

    #TODO consider creating a smarter graph

    def sentence_fc(self): #fully connected: returns dic of parents with all other edges connected
        parents = collections.OrderedDict()
        for word in self.word_idx:
            parents.update({word: []})
            for child in self.word_idx:
                if child != 'ROOT0':
                    parents[word].append(child)

        return parents


