import re
import collections


def f_uv(feats, sentence, u, v, mode):
    # u,v = words indices in sentence
    index_vec = []
    posp = sentence.word_pos[sentence.idx_word[u]]
    try:
        # f1: parent +posp
        index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp + "f1"])
    except:
        pass
    try:
        # f3: posp
        index_vec.append(feats.f_dict[posp+ "f3"])
    except:
        pass
    try:
        # f2: parent
        index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)]+ "f2"])
    except:
        pass
    try:
        # f5 child
        index_vec.append(feats.f_dict[sentence.idx_word[v][:-len(v)]+ "f5"])
    except:
        pass
    posc = sentence.word_pos[sentence.idx_word[v]]
    try:
        # f4: child +posc
        index_vec.append(feats.f_dict[sentence.idx_word[v][:-len(v)] + posc+ "f4"])
    except:
        pass
    try:
        # f6: posc
        index_vec.append(feats.f_dict[posc]+ "f6")
    except:
        pass
    try:
        # f8: posp + posc + child
        index_vec.append(feats.f_dict[posp + posc + sentence.idx_word[v][:-len(v)]+ "f8"])
    except:
        pass
    try:
        # f10: posp + posc + parent
        index_vec.append(feats.f_dict[posp + posc + sentence.idx_word[u][:-len(u)]+ "f10"])
    except:
        pass
    try:
        # f13: posp + posc
        index_vec.append(feats.f_dict[posp + posc+ "f13"])
    except:
        pass

    #complex features
    if mode == "C":
        # if int(u) - 1 != int(v) \
        #         and int(v) - 1 != int(u) \
        #         and int(u) + 1 != int(v) \
        #         and int(v) + 1 != int(u):
        posbp_idx = int(u) - 1
        if posbp_idx > 0:
            bparent = sentence.idx_word[str(posbp_idx)][:-len(str(posbp_idx))]
            posbp = sentence.word_pos[sentence.idx_word[str(posbp_idx)]]
        posbc_idx = int(v) - 1
        if posbc_idx > 0:
            bchild = sentence.idx_word[str(posbc_idx)][:-len(str(posbc_idx))]
            posbc = sentence.word_pos[sentence.idx_word[str(posbc_idx)]]
        posap_idx = int(u) + 1
        if posap_idx < sentence.slen:
            aparent = sentence.idx_word[str(posap_idx)][:-len(str(posap_idx))]
            posap = sentence.word_pos[sentence.idx_word[str(posap_idx)]]
        posac_idx = int(v) + 1
        if posac_idx < sentence.slen:
            achild = sentence.idx_word[str(posac_idx)][:-len(str(posac_idx))]
            posac = sentence.word_pos[sentence.idx_word[str(posac_idx)]]

        try:
            # fc1: posp + posbp + posc + posbc
            index_vec.append(feats.f_dict[posp + posbp + posc + posbc + "c1"])
        except:
            pass

        try:
            # fc2: posp + posap + posc + posbc
            index_vec.append(feats.f_dict[posp + posap + posc + posbc+ "c2"])
        except:
            pass

        try:
            # fc3: posp + posbp + posc + posac
            index_vec.append(feats.f_dict[posp + posbp + posc + posac+ "c3"])
        except:
            pass

        try:
            # fc4: posp + posap + posc + posac
            index_vec.append(feats.f_dict[posp + posap + posc + posac+ "c4"])
        except:
            pass

        start_idx = min(int(u),int(v))
        end_idx = max(int(u),int(v))
        for idx in range(start_idx + 1, end_idx):
            middle = sentence.idx_word[str(idx)]
            posm = sentence.word_pos[middle]
            try:
                # fc5: posp + posm + posc
                index_vec.append(feats.f_dict[posp + posm + posc+ "c5"])
            except:
                pass
            try:
                # fc6: parent + middle + child
                index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                              sentence.idx_word[middle][:-len(middle)] +
                                              sentence.idx_word[v][:-len(v)]+ "c6"])
            except:
                pass
            try:
                # fc6b: parent + posm + child
                index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                              posm +
                                              sentence.idx_word[v][:-len(v)]+ "c6b"])
            except:
                pass

        try:
            # fc7: parent + bparent + child + bchild
            index_vec.append(feats.f_dict[u + bparent + v + bchild+ "c7"])
        except:
            pass

        try:
            # fc8: parent + aparent + child + bchild
            index_vec.append(feats.f_dict[u + aparent + v + bchild+ "c8"])
        except:
            pass

        try:
            # fc9: parent + bparent + child + achild
            index_vec.append(feats.f_dict[u + bparent + v + achild+ "c9"])
        except:
            pass

        try:
            # fc10: parent + aparent + child + achild
            index_vec.append(feats.f_dict[u + aparent + v + achild+ "c10"])
        except:
            pass

        distance = int(u)-int(v)
        try:
            # fc11: distance
            index_vec.append(feats.f_dict[str(abs(distance))+ "c11"])
        except:
            pass

        direction = "LLLL" if distance > 0 else "RRRR"
        try:
            # fc12: direction
            index_vec.append(feats.f_dict[direction])
        except:
            pass


        try:
            # f13: parent + posp + child +posc
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp +
                                          sentence.idx_word[v][:-len(v)] + posc+ "c13"])
        except:
            pass

        try:
            # f14: parent + child +posc
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                          sentence.idx_word[v][:-len(v)] + posc+ "c14"])
        except:
            pass

        try:
            # f15: parent + posp + child
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp +
                                          sentence.idx_word[v][:-len(v)]+ "c15"])
        except:
            pass

        try:
            # f16: parent + child
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                          sentence.idx_word[v][:-len(v)]+ "c16"])
        except:
            pass

        # try:
        #     grandsons = sentence.word_children[v]
        #     for grandson in grandsons:
        #         posg = sentence.word_pos[grandson]
        #         try:
        #             # fc17: posp + posc + posg
        #             index_vec.append(feats.f_dict[posp + posc + posg+ "c17"])
        #         except:
        #             pass
        #
        #         try:
        #             # fc18: parent + child + grandson
        #             index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
        #                                           sentence.idx_word[v][:-len(v)] +
        #                                           grandson[:-len(sentence.word_idx(grandson))]+ "c18"])
        #         except:
        #             pass
        #
        #         try:
        #             grandgrandsons = sentence.word_children[grandson]
        #
        #             for grandgrandson in grandgrandsons:
        #                 posgg = sentence.word_pos[grandgrandson]
        #
        #                 try:
        #                     # fc19:posp + posc + posg + posgg
        #                     index_vec.append(feats.f_dict[posp + posc + posg + +posgg + "c19"])
        #                 except:
        #                     pass
        #
        #                 try:
        #                     # fc20: parent + child + grandson + grandgrandson
        #                     index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
        #                                           sentence.idx_word[v][:-len(v)] +
        #                                           grandson[:-len(sentence.word_idx[grandson])] +
        #                                           grandgrandson[:-len(sentence.word_idx[grandgrandson])] + "c20"])
        #                 except:
        #                     pass
        #
        #         except:
        #             pass
        #
        # except:
        #     pass
        #
        # try:
        #     for child2 in sentence.word_idx[sentence.idx_word[u]]:
        #         if v != sentence.word_idx[child2]:
        #             posc2 = sentence.word_pos[child2]
        #
        #             try:
        #                 # fc21:posp + posc + posc2
        #                 index_vec.append(feats.f_dict[posp + posc + posc2 + "c21"])
        #             except:
        #                 pass
        #
        #             try:
        #                 # fc22:father + posp + posc + posc2
        #                 index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp + posc + posc2 + "c22"])
        #             except:
        #                 pass
        #
        #             try:
        #                 # fc23:posp + posc + posc2 + child
        #                 index_vec.append(feats.f_dict[posp + posc + posc2 + child2[:-len(sentence.word_idx[child2])] + "c23"])
        #             except:
        #                 pass
        # except:
        #     pass


    return index_vec


def w_f(w, f):
    num = 0.0
    for x in f:
        num += w[x]
    return num


def weights_calc(w, sentence, feats,mode):
    weights = collections.OrderedDict()
    for pidx, parent in sentence.idx_word.items():  # includes root
        for cidx, child in sentence.idx_word.items():
            if parent not in weights:
                weights.update({parent: collections.OrderedDict()})
            if child not in weights[parent]:
                uidx = sentence.word_idx[parent]
                vidx = sentence.word_idx[child]
                # if uidx == vidx or vidx == 0:
                #     weights[parent].update({child: -1000})
                # else:
                #     weights[parent].update({child: w_f(w, f_uv(feats, sentence, uidx, vidx,mode))})
                if uidx != vidx and vidx != 0:
                    weights[parent].update({child: w_f(w, f_uv(feats, sentence, uidx, vidx,mode))})

    return weights


def evaluate(file1, file2):
    perc = 0.0
    num = 0.0
    with open(file1, 'r') as f1:
        s1 = []
        for line in f1:
            if line == '\n':
                continue
            else:
                match = re.split("\\s+", line)
                s1.append(match[6])
    with open(file2, 'r') as f2:
        s2 = []
        for line in f2:
            if line == '\n':
                continue
            else:
                match = re.split("\\s+", line)
                s2.append(match[6])

    # for w1,w2 in zip(s1,s2):
    #     print(w1,w2)

    for w1,w2 in zip(s1,s2):
        if w1 ==w2:
            perc += 1
        num += 1

    print("correct: ", perc/num)
