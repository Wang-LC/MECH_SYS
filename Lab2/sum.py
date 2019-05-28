def sum_i(list):
    sum = 0
    for n in list:
        sum = sum + n
    return sum

def sum_r(list):
    if list == []:
        return 0
    return list[0] + sum_r(list[1:])

if __name__ == "__main__":
    l = [1,3,5,6,4]
    s = sum_i(l)
    print(s)
    sr = sum_r(l)
    print(sr)