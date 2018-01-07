
class Sentence:

    def __init__(self, slist):
        self.word_idx = {}
        self.idx_word = {}
        self.word_pos = {}
        self.word_parent = {} # insert word, get parent word
        self.word_children = {} # insert word, get all childre words

        #update indices and POS
        for i,word in enumerate(slist):
            self.idx_word.update({word[0] : word[1]})
            self.idx_word.update({word[1] : word[0]})
            self.word_pos.update({word[1] : word[2]})

        #update parents and children
        for i, word in enumerate(slist):
            if(word[3] == '0'):
                self.word_parent.update({word[1] : 'ROOT'})
                self.word_children.update({'ROOT' : word[1]})
            else:

                if(word[3] not in self.word_parent):
                    self.word_parent.update({word[1] : self.idx_word[word[3]]})
                # if(self.idx_word[i] not in self.word)


