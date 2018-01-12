from Inference import *
from main import *
from funcs import evaluate
import utils

t = Parser(utils.TEST)
d = Parser(utils.TRAIN)
# d = Parser("dum")
f = Features(d.sentences)
# w = np.zeros(f.f_len)
w = pickle.load(open(utils.W_VEC, 'rb'))
inf = Inference(w,t.sentences,f)
inf.tag_text(utils.TEST_R)
evaluate(utils.TEST, utils.TEST_R)




