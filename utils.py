
DUM = "dum"
TRAIN = "train.labeled"
TEST = "test.labeled"

MODE = "C" #complex
# MODE = "B" #basic

ITER = 15
THRESHOLD = 3

# W = "c1w_" + str(ITER)  + "_RAND"

W = "comp_w_" + str(ITER) + "c"#+ "_RAND"
W_VEC = "weights_vec/" + W

FEAT = "_th_" + str(THRESHOLD)


TRAIN_R = "results/"+"train with " + W +FEAT
TEST_R = "results/"+"test with " + W +FEAT