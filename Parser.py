import re
from Sentence import *


class Parser:

    def __init__(self, file):
        self.sentences = []
        with open(file, 'r') as f:

            sentence = []
            for line in f:
                if line == '\n':
                    new_sentence = Sentence(sentence)
                    sentence = []
                    self.sentences.append(new_sentence)

                else:

                    match = re.split("\\s+", line)
                    sentence.append([match[0], match[1], match[3],match[6]])
            new_sentence = Sentence(sentence)
            self.sentences.append(new_sentence)