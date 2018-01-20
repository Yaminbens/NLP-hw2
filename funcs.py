import re


def f_uv(feats, sentence, u, v, mode):
    # u,v = words indices in sentence
    index_vec = []
    posp = sentence.word_pos[sentence.idx_word[u]]
    try:
        # f1: parent +posp
        index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp])
    except:
        pass
    try:
        # f3: posp
        index_vec.append(feats.f_dict[posp])
    except:
        pass
    try:
        # f2: parent
        index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)]])
    except:
        pass
    try:
        # f5 child
        index_vec.append(feats.f_dict[sentence.idx_word[v][:-len(v)]])
    except:
        pass
    posc = sentence.word_pos[sentence.idx_word[v]]
    try:
        # f4: child +posc
        index_vec.append(feats.f_dict[sentence.idx_word[v][:-len(v)] + posc])
    except:
        pass
    try:
        # f6: posc
        index_vec.append(feats.f_dict[posc])
    except:
        pass
    try:
        # f8: posp + posc + child
        index_vec.append(feats.f_dict[posp + posc + sentence.idx_word[v][:-len(v)]])
    except:
        pass
    try:
        # f10: posp + posc + parent
        index_vec.append(feats.f_dict[posp + posc + sentence.idx_word[u][:-len(u)]])
    except:
        pass
    try:
        # f13: posp + posc
        index_vec.append(feats.f_dict[posp + posc])
    except:
        pass

    #complex features
    if mode == "C":

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
            index_vec.append(feats.f_dict[posp + posbp + posc + posbc])
        except:
            pass

        try:
            # fc2: posp + posap + posc + posbc
            index_vec.append(feats.f_dict[posp + posap + posc + posbc])
        except:
            pass

        try:
            # fc3: posp + posbp + posc + posac
            index_vec.append(feats.f_dict[posp + posbp + posc + posac])
        except:
            pass

        try:
            # fc4: posp + posap + posc + posac
            index_vec.append(feats.f_dict[posp + posap + posc + posac])
        except:
            pass

        start_idx = min(int(u),int(v))
        end_idx = max(int(u),int(v))
        for idx in range(start_idx + 1, end_idx):
            middle = sentence.idx_word[str(idx)]
            posm = sentence.word_pos[middle]
            try:
                # fc5: posp + posm + posc
                index_vec.append(feats.f_dict[posp + posm + posc])
            except:
                pass
            try:
                # fc6: parent + middle + child
                index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                              sentence.idx_word[middle][:-len(middle)] +
                                              sentence.idx_word[v][:-len(v)]])
            except:
                pass

        try:
            # fc7: parent + bparent + child + bchild
            index_vec.append(feats.f_dict[u + bparent + v + bchild])
        except:
            pass

        try:
            # fc8: parent + aparent + child + bchild
            index_vec.append(feats.f_dict[u + aparent + v + bchild])
        except:
            pass

        try:
            # fc9: parent + bparent + child + achild
            index_vec.append(feats.f_dict[u + bparent + v + achild])
        except:
            pass

        try:
            # fc10: parent + aparent + child + achild
            index_vec.append(feats.f_dict[u + aparent + v + achild])
        except:
            pass

        distance = int(u)-int(v)
        try:
            # fc12: distance
            index_vec.append(feats.f_dict[abs(distance)])
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
                                          sentence.idx_word[v][:-len(v)] + posc])
        except:
            pass

        try:
            # f14: parent + child +posc
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                          sentence.idx_word[v][:-len(v)] + posc])
        except:
            pass

        try:
            # f15: parent + posp + child
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] + posp +
                                          sentence.idx_word[v][:-len(v)]])
        except:
            pass

        try:
            # f16: parent + child
            index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                          sentence.idx_word[v][:-len(v)]])
        except:
            pass

        try:
            grandsons = sentence.word_children[v]
            for grandson in grandsons:
                posg = sentence.word_pos[grandson]
                try:
                    # fc17: posp + posc + posg
                    index_vec.append(feats.f_dict[posp + posc + posg])
                except:
                    pass

                try:
                    # fc18: parent + child + grandson
                    index_vec.append(feats.f_dict[sentence.idx_word[u][:-len(u)] +
                                                  sentence.idx_word[v][:-len(v)]] +
                                                  grandson[:-len(sentence.word_idx(grandson))])
                except:
                    pass
        except:
            pass



    return index_vec


def w_f(w, f):
    num = 0.0
    for x in f:
        num += w[x]
    return num


def weights_calc(w, sentence, feats,mode):
    weights = {}
    for pidx, parent in sentence.idx_word.items():  # includes root
        for cidx, child in sentence.idx_word.items():
            if parent not in weights:
                weights.update({parent: {}})
            if child not in weights[parent]:
                uidx = sentence.word_idx[parent]
                vidx = sentence.word_idx[child]
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
