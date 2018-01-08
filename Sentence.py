
class Sentence:

    def __init__(self, slist):

        self.word_idx = {} # insert word, get index of word in sentence
        self.idx_word = {} # insert index in sentence, get word at index
        self.word_pos = {} # inser word get POS
        self.word_parent = {} # insert word, get parent word
        self.word_children = {} # insert word, get all childre words

        #update indices and POS
        for i,word in enumerate(slist):
            self.idx_word.update({word[0]: word[1]})
            if word[1] not in self.word_idx:
                self.word_idx.update({word[1]: []})
            self.word_idx[word[1]].append(word[0])
            if word[1] not in self.word_pos:
                self.word_pos.update({word[1]:[]})
            self.word_pos[word[1]].append(word[2])
            if word[3] == '0':
                self.word_parent.update({word[1]: ['ROOT']})
                self.word_children.update({"ROOT": [word[1]]})
        self.idx_word.update({'0': "ROOT"})
        self.word_idx.update({"ROOT": '0'})
        self.word_pos.update({"ROOT":["ROOT"]})
        # print(self.idx_word)
        self.slen = len(self.idx_word)
        #update parents and children
        for i, word in enumerate(slist):
            if word[3] == '0':
                continue
            if word[1] not in self.word_parent:
                self.word_parent.update({word[1]: []})
            # print(self.word_parent[word[1]])
            self.word_parent[word[1]].append(self.idx_word[word[3]])
            # print(word[1])
            # print(word[3])
            if self.idx_word[word[3]] not in self.word_children:
                self.word_children.update({self.idx_word[word[3]]: []})
            self.word_children[self.idx_word[word[3]]].append(word[1])
            # print(word[1])


    #
    # def __contains__(self, x):
    #     return x in self.word_idx.keys()
    #
    # def __iter__(self):
    #     return iter(self.word_idx.keys())
