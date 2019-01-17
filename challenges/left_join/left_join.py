"""Module to perform a left join on two hash tables."""


def left_join(ht1, ht2):
    ht1_list = []
    for i in range(len(ht1)):
        if ht1.hash_table[i]:
            ht1_list.append(ht1.hash_table[i][0][0])
            ht1_list.append(ht1.hash_table[i][0][1])

    split_list = [ht1_list[2*i:2*i + 2] for i in range(len(ht1_list)//2)]

    for i in range(len(ht2)):
            if ht2.hash_table[i]:
                for j in range(len(split_list)):
                    if ht2.hash_table[i][0][0] == split_list[j][0]:
                        split_list[j].append(ht2.hash_table[i][0][1])

    return split_list
