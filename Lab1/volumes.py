def cylinder_volume(r, h):
    if r < 0 or h < 0:
        raise ValueError
    else:
        import math
        volume = math.pi * r ** 2 * h
        return volume


def torus_volume(r_out, r_in):
    if r_out < r_in or r_in < 0:
        raise ValueError
    else:
        import math
        r_mid = (r_out - r_in) / 2
        volume = (r_mid ** 2 * math.pi) * (2 * math.pi * (r_in + r_mid))
        return volume

if __name__ == '__main__':

    try:
        V = cylinder_volume(2, 3)
    except ValueError:
        print("ValueError")
    else:
        print(V)

    try:
            V = cylinder_volume(-2, 3)
    except ValueError:
        print("ValueError")
    else:
        print(V)

    try:
        torusV = torus_volume(4, 3)
    except ValueError:
        print("ValueError")
    else:
        print(torusV)

    try:
        torusV = torus_volume(-4, 3)
    except ValueError:
        print("ValueError")
    else:
        print(torusV)