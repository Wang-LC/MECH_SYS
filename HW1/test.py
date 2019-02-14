from analysis import analyze_data
from analysis import estimate_system

initial, p, final, Tr, Tp, percentOS, Ts = analyze_data('data1.csv')
m, k, c = estimate_system('data1.csv')
print(initial)
print(p)
print(final)
print(Tr)
print(Tp)
print(percentOS)
print(Ts)
print(p)
print(m)
print(k)
print(c)


