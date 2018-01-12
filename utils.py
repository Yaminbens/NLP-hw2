
DUM = "dum"
TRAIN = "train.labeled"
TEST = "test.labeled"

ITER = 20
THRESHOLD = 0

W = "w_" + str(ITER) + "_RAND"
W_VEC = "weights_vec/" + W

FEAT = "_th_" + str(THRESHOLD)

TRAIN_R = "results/"+"train with " + W +FEAT
TEST_R = "results/"+"test with " + W +FEAT