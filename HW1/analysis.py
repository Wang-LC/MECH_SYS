import numpy as np
import math
import sys


def analyze_data(file_name, mean=None):  # Q10
    # read file
    t_list, p_list = loadCSV(file_name, mean)
    # Q3
    c_initial = p_list[0]
    c_final = p_list[-1]
    c_max = max(p_list)
    # position at 10% and 90% of the range from c_initial to c_final
    final_10 = (c_final - c_initial) * 0.1 + c_initial
    final_90 = (c_final - c_initial) * 0.9 + c_initial
    # max value of the 2% of the range from c_initial to c_final
    final_2 = (c_final - c_initial) * 0.02
    # Q4
    T_r = find_time(final_90, p_list, t_list) - find_time(final_10, p_list, t_list)
    # Q5
    T_p = find_time(c_max, p_list, t_list)
    # Q6
    OS = (c_max - c_final) / (c_final - c_initial) * 100
    # Q7
    T_s = find_time2(final_2, p_list, t_list, c_final)
    return c_initial, c_max, c_final, T_r, T_p, OS, T_s


def estimate_system(filename, mean=None):  # Q11
    mass = 1
    T_p, overshoot, T_s = analyze_data(filename, mean)[4:7]
    # Q8
    z = (-math.log(overshoot / 100)) / (math.sqrt(math.pi ** 2 + math.log(overshoot / 100) ** 2))
    omega_n = 4 / (T_s * z)
    # Q9
    spring = mass * omega_n ** 2
    damper = 2 * z * omega_n * mass
    return mass, spring, damper


def loadCSV(filename, mean):  # load file
    try:
        f = open(filename)
        f.close()
    except FileNotFoundError:
        print(filename, 'is not found')
        exit()
    except IOError:
        print(filename, 'is not accessible')
        exit()
    tmp = np.loadtxt(filename, dtype=np.str, delimiter=',')
    time = tmp[1:, 0].astype(np.float)
    position = tmp[1:, 1].astype(np.float)
    # extra credit
    if mean is None:  # without filter
        return list(time), list(position)
    elif mean == '-filter':  # with filter
        return mean_filter(list(time)), mean_filter(list(position))
    else:  # wrong filter command
        print('Wrong filter code')
        exit()


def find_time(value, position_list, time_list):  # find time using a position value
    for i in range(len(position_list)):
        while position_list[i] >= value:
            return time_list[i]


def find_time2(value, position_list, time_list, c_final):  # find the time using a range value(reverse)
    for i in range(len(time_list) - 1, -1, -1):
        while abs(position_list[i] - c_final) > value:
            return time_list[i+1]


def mean_filter(l, width=15):  # deal with noise
    if len(l) < width:
        return 'list is smaller than filter width'
    else:
        result = []
        for i in range(len(l)-width+1):
            result.append(sum(l[i: i+width])/width)
        return result


if __name__ == "__main__":
    if len(sys.argv) == 2:  # without filter
        initial, position_max, final, Tr, Tp, percentOS, Ts = analyze_data(sys.argv[1])
        m, k, c = estimate_system(sys.argv[1])
    elif len(sys.argv) == 3:  # with filter
        initial, position_max, final, Tr, Tp, percentOS, Ts = analyze_data(sys.argv[2], sys.argv[1])
        m, k, c = estimate_system(sys.argv[2], sys.argv[1])
    else:  # wrong code
        print('Please enter one file with or without filter')
        exit()

    zeta = (-math.log(percentOS / 100)) / (math.sqrt(math.pi ** 2 + math.log(percentOS / 100) ** 2))

    print('Peak time: %ss' % Tp)
    print('Percent overshoot: %s%%' % percentOS)
    print('Settling time: %ss' % Ts)
    print('Omega_n:', 4 / (Ts * zeta))
    print('Zeta:', zeta)
    print('Spring constant:', k)
    print('Mass:', m)
    print('Damper:', c)