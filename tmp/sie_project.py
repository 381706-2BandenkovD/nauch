import matplotlib.pyplot as plt
from math import *
a_p = 0.001
a_z = 0.0001
#a_q = 0.0001

alfa_0 = 0.23

b_p = 0.01
b_z = 0.01

g_p = 0.001 
q_p = 6
q_z = 5.7 
Z0 = 0
Z1 = 1
P0 = 0
P1 = 1
k_z = 0.15
k_p = 0.05

Q0 = 5
Qs = 0.15
w_q = 0.00242

#def dq(Vt):
#    return float(-a_q * Q0 + b_q/(1 + exp(-Vt/k_q)))

def dq(t, Z):
    return float(Q0 + alfa_0 * Z + Qs * sin(w_q * t))

def dz(Z, P, dq):
    return float(-(a_z + g_p * P) * Z + b_z * (Z0 - (Z0 - Z1)/(1 + exp(-(dq-q_z) / k_z))))

def dp(P, dq):
    return float(-a_p * P + b_p * (P0 - (P0 - P1)/(1 + exp(-(dq-q_p) / k_p))))

def Euler(p0,z0,t,h):
    fz=[]
    fp=[]
    qq = []
    time=[]
    fp.append(p0)
    fz.append(z0)
    t0=0.
    time.append(t0)
    i=0
    zt=0
    pt=0
    qq.append(dq(t0, fz[i]))
    #print("_______________________TEST FOR FUNCTIONS__________________________")
    #print("value for h = ", h)
    #print("value for t = ", t)
    #print("-------------------------------------------------------------------")
    #print("value dQ on STEP ", i, " = ", qq[i])
    #print("value dZ on STEP ", i, " = ", fz[i])
    #print("value dP on STEP ", i, " = ", fp[i])

    while(t0<t):
        pt=fp[i]+h*dp(fp[i],dq(t0, fz[i]))
        fp.append(pt)
        zt=fz[i]+h*dz(fz[i], fp[i], dq(t0, fz[i]))
        fz.append(zt)
        t0+=h
        qq.append(dq(t0, fz[i]))
        time.append(t0)
        i+=1
        #print("-------------------------------------------------------------------")
        #print("value dQ on STEP ", i, " = ", qq[i])
        #print("value dZ on STEP ", i, " = ", fz[i])
        #print("value dP on STEP ", i, " = ", fp[i])
    plt.plot(time,fz, label = 'График fz(t)')
    plt.plot( time,fp, label = 'График fp(t)')
    plt.xlabel('Ось time')
    plt.ylabel('Оси fz,fp')
    plt.legend()
    plt.show()

    #plt.plot(fz,qq, label = 'График fz(q)')
    #plt.plot(fp,qq, label = 'График fp(q)')
    #plt.ylabel('Ось Q')
    #plt.xlabel('Оси fz,fp')
    #plt.legend()
    #plt.show()

    #plt.plot( fp, fz, label = 'График p(z)') #z(p)
    #plt.ylabel('ОсьZ')
    #plt.xlabel('ОсьP')
    #plt.legend()
    #plt.show()

t= 2000.
h=0.01
Euler(Z0,P0,t,h)
#my_file = open('tests_for_project.txt', 'w')
#my_file.write(Euler(Z0,P0,t,h))
#my_file.close()