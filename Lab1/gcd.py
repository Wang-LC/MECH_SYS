def gcd(a, b):
    if a < b:
        n = a
    else:
        n = b
    for i in range(1, n + 1):
        if a % i == 0 and b % i == 0:
            ans = i

    return (ans)


if __name__ == '__main__':
    from math import gcd as gcdB
    import random

    passTimes = 0
    testTimes = 100
    for count in range(testTimes):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        if gcd(a, b) == gcdB(a, b):
            passTimes = passTimes + 1

    if passTimes == testTimes:
        print("gcd passed all tests!")
    else:
        print("gcd failed!")
