from Inference import *
from main import *
from funcs import evaluate

d = Parser("train.labeled")
# d = Parser("dum")
f = Features(d.sentences)
# w = np.zeros(f.f_len)
ITER = 20
w = pickle.load(open("weights_vec/" + "w" + str(ITER)+"_Rand", 'rb'))
inf = Inference(w,d.sentences,f)
filename = "results/"+"train with w" + str(ITER)+"_Rand"
inf.tag_text(filename)
evaluate("train.labeled", filename)




