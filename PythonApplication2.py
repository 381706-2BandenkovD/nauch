import matplotlib.pyplot as plt
#import random


def func(x,y):
    E=0.05
    a=0.1
    num=(E*(-y + x + a))
    denom=(x - (x**3)/3 -y)
    if(denom==0):
        return 1
    res=  num / denom
    #print(res)
    return res
 
    
def Euler(x0, y0, t, h):
    y=[]#float(list())
    x=[]#float(list())
    y.append(y0)
    x.append(x0+h)
    i=0
    dt=0
    time=[]
    time.append(dt)
    while dt<=t:
        Y=y[i] + h * func(x[i],y[i])
        #print("i= ",i)
        #print("Y= ",Y)
        X=x[i] + h
        #print("X= ",X)
        y.append(Y)
        x.append(X)
        
        dt+=h
        time.append(dt)
        i+=1
    print("x0:",x0)
    print("y0:",y0)    
    print("Шаг:",h)
    print("Время:",t)  
    print("Число точек:",i)
        
    #print(x)
    #print(y)
    
    #plt.scatter(points, koeff)
    plt.scatter(x, y, label = 'Точки', color='w')
    plt.plot(x, y, label = 'График',color='r')
    
    plt.xlabel(' Х')
    plt.ylabel('У')
    plt.legend()
    plt.show() 
    
    #time=[i for i in range(10000) ]
    
    plt.scatter( time, x,label = 'Точки', color='w')
    plt.plot( time,x, label = 'График',color='r')

    plt.ylabel('t')
    plt.xlabel('X')
    plt.legend()
    plt.show() 
   
    plt.scatter( time, y,label = 'Точки', color='w')
    plt.plot( time,y, label = 'График',color='r')

    plt.ylabel('t')
    plt.xlabel('Y')
    plt.legend()
    plt.show() 

##################################################
x0=0
y0=0
t=100

h=0.01
Euler(x0, y0, t, h)
