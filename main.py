from Features import *
from Parser import *

def main():
    # d = Parser("train.labeled")
    d = Parser("dum")
    for s in d.sentences:
        print(s.slen)
    f = Features(d.sentences)



if __name__ == "__main__":
    main()