import re


def f_uv(feats, sentence, u, v):
    # u,v = words indices in sentence
    index_vec = []
    for posp in sentence.word_pos[sentence.idx_word[u]]:
        index_vec.append(feats.f_dict[sentence.idx_word[u] + posp])
        index_vec.append(feats.f_dict[posp])
    index_vec.append(feats.f_dict[sentence.idx_word[u]])
    index_vec.append(feats.f_dict[sentence.idx_word[v]])
    for posc in sentence.word_pos[sentence.idx_word[v]]:
        index_vec.append(feats.f_dict[sentence.idx_word[v] + posc])
        index_vec.append(feats.f_dict[posc])
        if sentence.idx_word[u] + sentence.idx_word[v] in sentence.parent_child:
            index_vec.append(feats.f_dict[sentence.idx_word[u] + sentence.idx_word[v] + posc])
            for posp in sentence.word_pos[sentence.idx_word[u]]:
                index_vec.append(feats.f_dict[sentence.idx_word[u] + posp + posc])
                index_vec.append(feats.f_dict[posp + posc])

    return index_vec


def w_f(w, f):
    num = 0.0
    num = sum([w[x] for x in f])
    return num


def weights_calc(w, sentence, feats):
    weights = {}
    for pidx, parent in sentence.idx_word.items():  # includes root
        for cidx, child in sentence.idx_word.items():
            if parent not in weights:
                weights.update({parent: {}})
            if child not in weights[parent]:
                for uidx in sentence.word_idx[parent]:
                    for vidx in sentence.word_idx[child]:
                        weights[parent].update({child: w_f(w, f_uv(feats, sentence, uidx, vidx))})

    return weights


def weight_calc(sentence,u,v,weights):
    num = 0.0
    for uidx in sentence.word_idx[u]:
        for vidx in sentence.word_idx[v]:
            num += weights[uidx][vidx]
    return num


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
