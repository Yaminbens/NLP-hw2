from Inference import *
from main import *
from funcs import evaluate

TRAIN = "train.labeled"
TEST = "test.labeled"
t = Parser(TEST)
d = Parser(TRAIN)
# d = Parser("dum")
f = Features(d.sentences)
# w = np.zeros(f.f_len)
ITER = 20
w = pickle.load(open("weights_vec/" + "w" + str(ITER) + "_RAND", 'rb'))
inf = Inference(w,d.sentences,f)
filename = "results/"+"train with w" +str(ITER) + "_RAND"
inf.tag_text(filename)
evaluate(TRAIN, filename)




