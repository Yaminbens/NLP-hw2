from Features import *
from Parser import *

def main():
    d = Parser("train.labeled")
    f = Features(d.sentences)



if __name__ == "__main__":
    main()