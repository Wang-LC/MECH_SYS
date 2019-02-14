import math
r_in=3
r_ou=4
r=(r_ou-r_in)/2

def vol(r):
    v = r**2*math.pi
    return v

def peri(r):
    s = 2*math.pi*r
    return s

V = vol(r)*peri(r_in+r)
print(V)