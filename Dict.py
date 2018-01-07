import re
import numpy as np
import operator
import pandas as pd
from Sentence import *


class Dict:

    def __init__(self, file):
        # df = pd.read_csv(
        #     filepath_or_buffer=file,
        #     # index_col=0,
        #     header=None,
        #     names=["idx", "word", "3", "POS", "5", "6", "head","8","9","10"],
        #     usecols=["idx", "word", "POS","head"],
        #     delim_whitespace=True)
        # df.reset_index()
        # # df.columns = ["idx", "word", "3", "POS", "5", "6", "head","8","9","10"]
        # # df.dropna(how="all", inplace=True)  # drops the empty line at file-end
        #
        # # print(df.loc[df['idx']==1])
        # print(df)

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
        print(self.sentences)