def reverse_list(l):
    result = []
    i = len(l) - 1
    while i >= 0:
        result.append(l[i])
        i = i - 1
    return result