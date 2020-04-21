def makeAnagram(a, b):
    non_common = []

    c_list= list(a)
    b_list = list(b)
    my_d = {}
    for char in c_list:
        my_d[char] = c_list.count(char)

    for char in b_list:
        if char not in my_d.keys() or b_list.count(char) != c_list.count(char):
            non_common.append(char)

    return len(non_common)