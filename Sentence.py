
class Sentence:

    def __init__(self, slist):

        self.word_idx = {} # insert word, get index of word in sentence
        self.idx_word = {} # insert index in sentence, get word at index
        self.word_pos = {} # inser word get POS
        self.word_parent = {} # insert word, get parent word
        self.word_children = {} # insert word, get all childre words
        self.parent_child = []

        #update indices and POS
        for i,word in enumerate(slist):
            self.idx_word.update({word[0]: word[1]+word[0]})
            if word[1]+word[0] not in self.word_idx:
                self.word_idx.update({word[1]+word[0]: []})
            self.word_idx[word[1]+word[0]].append(word[0])
            if word[1]+word[0] not in self.word_pos:
                self.word_pos.update({word[1]+word[0]:[]})
            self.word_pos[word[1]+word[0]].append(word[2])
            if word[3] == '0':
                self.word_parent.update({word[1]+word[0]: ['ROOT']})
                self.word_children.update({"ROOT*": [word[1]+word[0]]})
        self.idx_word.update({'*': "ROOT*"})
        self.word_idx.update({"ROOT*": '*'})
        self.word_pos.update({"ROOT*":["ROOT"]})
        # print(self.idx_word)
        self.slen = len(self.idx_word)
        #update parents and children
        for i, word in enumerate(slist):
            if word[3] == '0':
                continue
            if word[1]+word[0] not in self.word_parent:
                self.word_parent.update({word[1]+word[0]: []})
            # print(self.word_parent[word[1]])
            self.word_parent[word[1]+word[0]].append(self.idx_word[word[3]])
            # print(word[1])
            # print(word[3])
            if self.idx_word[word[3]] not in self.word_children:
                self.word_children.update({self.idx_word[word[3]]: []})
            self.word_children[self.idx_word[word[3]]].append(word[1]+word[0])
            # print(word[1])

        for parent in self.word_children:
            for child in self.word_children[parent]:
                self.parent_child.append(parent+child)

    def sentence_fc(self): #fully connected: returns dic of parents with all other edges connected
        parents = {}
        for word in self.word_idx:
            parents.update({word: []})
            for child in self.word_idx:
                if child != 'ROOT':
                    parents[word].append(child)

        return parents


