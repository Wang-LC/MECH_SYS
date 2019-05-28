def close(a, b, c):
    if abs(a - b) < c:
        return True
    else:
        return False


if __name__ == '__main__':
    print(close(1, 2, 3))
    print(close(1, 2, 0.5))
