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
                    try:
                        wordproc = float(match[1])
                        wordproc = "NUMBERWORD"
                    except:
                        wordproc = match[1].lower()

                    sentence.append([match[0], wordproc, match[3],match[6],match[1]])
            new_sentence = Sentence(sentence)
            self.sentences.append(new_sentence)