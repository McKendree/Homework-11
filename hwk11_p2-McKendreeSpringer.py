import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def psi(x, L, C, sigma):
    return C*(x*(L-x))/(L**2)*np.exp((-1*(x-d)**2)/(2*sigma**2))

if __name__ in "__main__":
    L = 1 #length in m
    d = 0.1 #distance in m
    C = 1 #m/s
    sigma = 0.3 #m
    v = 100 #m/s
    t = 0 #initial time in s
    tmax = 0.01 #maximum time in s
    
    a = 1e-4 #physical stepsize in m
    h = 1e-6 #time stepsize in s

    #string length positions
    x = np.arange(0,L+a,a)

    time = np.arange(t,tmax,h)

    #vertical position of string
    string = np.zeros(len(x))
    new_string = string.copy()

    #creates plot figure
    title = 'Vibrating String'
    plt.ion()
    fig = plt.figure(figsize=(8,8))
    ax = plt.subplot()

    #sets up plot axes
    ax.set_xlabel('Position (m)')
    ax.set_ylabel('Position (m)')
    ax.set_xlim(0, L)
    ttl = ax.set_title(title)
    ttl.set_position([.5, .85])
    wax, = ax.plot([],[])
    plt.tight_layout()
    plt.show()

    tend = 1
    counter = 0
    while t<tend:
        for i in range(1, len(string)-1):
            #FTCS
            new_string[i] = string[i] + h*(v**2/a**2)*(psi[x[i]+a,L,C,sigma]
                                                       +psi[x[i]-a,L,C,sigma]
                                                       -2*psi[x[i],L,C,sigma])
        t+=h
        string, new_string = new_string, string
        #plots every 100 computations
        if counter % 100 == 0:
            wax.set_data(x, string)
            ax.set_title(title+'\nTime: '+'%.2f'%t+'s')
            plt.draw()
            plt.pause(0.01)
        counter = counter+1
