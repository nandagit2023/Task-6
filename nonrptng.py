list1 = [1, 2, 3, 3, 4, 1, 4, 3]


def non_repeating_num(x):
    list2 = []
    for i in x:  # iterate given list
        if x.count(i) < 2:  # if occurrence of elements is less than 2 then its non repeating
            list2.append(i)
    return list2


print(non_repeating_num(list1))
