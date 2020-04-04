import matplotlib.pyplot as plt

def Euler(x0,y0,t,h):
    y = []
    x = []
    time = []
    x.append(x0)
    y.append(y0)
    t0 = 0.
    time.append(t0)
    i = 0
    yt = 0
    xt = 0
    while(t0 < t):
        yt = y[i] + h * fy(x[i], y[i])
        y.append(yt)
        xt = x[i] + h * fx(x[i],y[i])
        x.append(xt)
        t0+=h
        time.append(t0)
        i+=1

    plt.plot(time,y, label = 'График y(t)')
    plt.plot(time,x, label = 'График x(t)')
    plt.xlabel('Ось time')
    plt.ylabel('Оси X,Y')
    plt.legend()
    plt.show()
    plt.plot(x, y, label = 'График y(x)')
    plt.ylabel('Осьy')
    plt.xlabel('ОсьX')
    plt.legend()
    plt.show()

def Runge_Kutt(x0,y0,t,h):
    y = []
    x = []
    time = []
    x.append(x0)
    y.append(y0)
    t0 = 0.
    time.append(t0)
    i = 0
    yt = 0
    xt = 0
    while(t0 < t):
        k1_y = h * fy(x[i], y[i])
        kx = x[i] + h / 2
        y1 = y[i] + k1_y / 2
        k2_y = h * fy(kx, y1)
        y1 = y[i] + k2_y / 2
        k3_y = h * fy(kx, y1)
        kx = kx + h / 2
        y1 = y[i] + k3_y
        k4_y = h * fy(kx, y1)
        yt = y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        y.append(yt)
        
        k1_x = h * fx(x[i], y[i])
        kx = x[i] + h / 2
        y1 = y[i] + k1_x / 2
        k2_x = h * fx(kx, y1)
        y1 = y[i] + k2_x / 2
        k3_x = h * fx(kx, y1)
        kx = kx + h / 2
        y1 = y[i] + k3_x
        k4_x = h * fx(kx, y1)
        xt = x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        x.append(xt)
        t0+=h
        time.append(t0)
        i+=1
        
    plt.plot(time,y, label = 'График y(t)')
    plt.plot(time,x, label = 'График x(t)')
    plt.xlabel('Ось time')
    plt.ylabel('Оси X,Y')
    plt.legend()
    plt.show()

    plt.plot(x, y, label = 'График y(x)')
    plt.ylabel('Осьy')
    plt.xlabel('ОсьX')
    plt.legend()
    plt.show()

def fx(x,y):
    return float(x - x * x * x / 3. - y)

def fy(x, y):
    E = 0.05
    #a=0.1
    a = 2
    return float(E * (-y + x + a))


x0 = 0.
y0 = 0.
t = 100
h = 0.01
Euler(x0,y0,t,h)
Runge_Kutt(x0,y0,t,h)
