
def f_uv(feats, sentence, u, v):
    # u,v = words indices in sentence
    index_vec = []

    for posp in sentence.word_pos[sentence.idx_word(u)]:
        index_vec.append(feats.f_dict[sentence.idx_word(u) + posp])
        index_vec.append(feats.f_dict[posp])
    index_vec.append(feats.f_dict[sentence.idx_word(u)])
    index_vec.append(feats.f_dict[sentence.idx_word(v)])
    for posc in sentence.word_pos[sentence.idx_word(v)]:
        index_vec.append(feats.f_dict[sentence.idx_word(v) + posc])
        index_vec.append(feats.f_dict[posc])
        if sentence.idx_word(u) + sentence.idx_word(v) in sentence.parent_child:
            index_vec.append(feats.f_dict[sentence.idx_word(u) + sentence.idx_word(v) + posc])
            for posp in sentence.word_pos[sentence.idx_word(u)]:
                index_vec.append(feats.f_dict[sentence.idx_word(u) + posp + posc])
                index_vec.append(feats.f_dict[posp + posc])

    return index_vec


def w_f(w, f):
    num = 0.0
    num = sum([w[x] for x in f])
    return num