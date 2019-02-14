def reverse_r(l):
    if len(l) == 0:
        return []
    return [l[-1]] + reverse_r(l[0:-1])

def reverse_i(l):
    list_new = list(l[:])
    count = -1
    for n in range(len(l)):
        list_new[n] = l[count]
        count -= 1
    return list_new




if __name__ == "__main__":
    m = 'hello'
    n = [1, 2, 3, 4, 5]
    print(reverse_r(m))
    print(reverse_r(n))
    print(reverse_i(m))
    print(reverse_i(n))