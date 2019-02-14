def mean_filter(l, width=3):
    if len(l) < width:
        return 'list is smaller than filter width'
    elif width % 2 == 0:
        return 'filter width must be odd'
    elif width < 0:
        return 'filter width must be positive'
    else:
        result = []
        for i in range(len(l)-width+1):
            result.append(sum(l[i: i+width])/width)
        return result

if __name__ == "__main__":
    l1 = [10, 13, 13]
    l2 = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]
    l3 = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]
    print(mean_filter(l1))
    print(mean_filter(l2))
    print(mean_filter(l3, 5))
    print(mean_filter(l2, 4))
    print(mean_filter(l2, -3))
    print(mean_filter(l1, 13))
    print(mean_filter([1, 2]))
    print(mean_filter([1], 0))