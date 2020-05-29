import matplotlib.pyplot as plt
from math import *
import cmath
a_p = 0.001
a_z = 0.001

alfa_0 = 0.23

b_p = 0.01
b_z = 0.01

g_p = 0.001 #0.1
Qp = 1.5 #6
Qz = 6.  #1.1
Z0 = 0
Z1 = 1
P0 = 0
P1 = 1
k_z = 6.67 #1 / 0.15
k_p = 20   #1 / 0.05

Q0 = 5
Qs = 0.01
w_q = 0.01

#def dq(Vt):
#    return float(-a_q * Q0 + b_q/(1 + exp(-Vt/k_q)))

def dq(t, Z):
    return float(Q0 + alfa_0 * Z + Qs * sin(w_q * t))

def dz(Z, P, dq):
    return float(-(a_z + g_p * P) * Z + b_z * (Z0 - (Z0 - Z1)/(1 + exp(-(dq-q_z) * k_z))))

def dp(P, dq):
    return float(-a_p * P + b_p * (P0 - (P0 - P1)/(1 + exp(-(dq-q_p) * k_p))))

#roots
#найдем  точки ср (у нас одна)
Q = Q0 + alfa_0 #

p = (b_p * (P0 - (P0 - P1)/(1 + exp(-(Q - Qp) * k_p)))) / a_p

z = b_z * (Z0 - (Z0 - Z1)/(1 + exp(-(Q - Qz) * k_z))) / (a_z + g_p * p)

dFz = (-1) * (a_z + g_p * p)
dFp = (-1) * (g_p * z)

dGz = 0
dGp = (-1) * (a_p)


print("p = ",p)
print("z = ",z)

#смотрим устойчивость
print("dFz = ",dFz)
print("dFp = ",dFp)
print("dGz = ",dGz)
print("dGp = ",dGp)

#ищем корни хп
a=1
b= a_p + a_z + g_p*p
c= a_z * a_p + a_p + g_p * p

D = b*b - 4*a*c
print("D = ",D)

x1=(-b+cmath.sqrt(D))/2*a
x2=(-b-cmath.sqrt(D))/2*a

print("x1 = ",x1)
print("x2 = ",x2)

#у нас комплексые корни с отриц действ частью -> устойчивый узел
