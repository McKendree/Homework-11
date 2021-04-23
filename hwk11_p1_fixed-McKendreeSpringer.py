import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    gridsize = 100
    target = 1e-6 #target accuracy in volts
    rho = 1/10000 #Coulombs per cm^2

    phi = np.zeros((gridsize+1, gridsize+1))
    phi[20:40,60:80] = rho
    phi[60:80,20:40] = -rho

    phiprime = np.zeros(phi.shape)

    #relaxation method
    max_diff = 1.0
    while max_diff > target:
        #calculate new values of potential
        for i in range(gridsize+1):
            for j in range(gridsize+1):
                if i==0 or i==gridsize or j==0 or j==gridsize:
                    phiprime[i,j] = phi[i,j]
                else:
                    phiprime[i,j] = 0.25*(phi[i+1,j] + phi[i-1,j] +
                                          phi[i,j+1] + phi[i,j-1])#+(gridsize**2)/4*rho
        
        max_diff = np.max(abs(phi-phiprime))
        phi, phiprime = phiprime, phi

    #prints the value of the central point in phi
    print('Relaxation method central point value:',phi[50,50])

    #plots relaxation method
    plt.imshow(phi)
    plt.savefig('relaxation_method.png')
    plt.show()
    plt.clf()

    phi = np.zeros((gridsize+1, gridsize+1))
    phi[20:40,60:80] = rho
    phi[60:80,20:40] = -rho

    #Guass-Seidal method
    max_diff = 1.0
    w = 0.5
    while max_diff > target:
        phiprime = phi
        #calculate new values of potential
        for i in range(gridsize+1):
            for j in range(gridsize+1):
                if i==0 or i==gridsize or j==0 or j==gridsize:
                    phi[i,j] = phi[i,j]
                else:
                    phi[i,j] = (1+w)/4*(phi[i+1,j] + phi[i-1,j] +
                                          phi[i,j+1] + phi[i,j-1])
        
        max_diff = np.max(abs(phi-phiprime))

    #prints the value of the central point in phi
    print('Gauss-Seidal method central point value:',phi[50,50])

    #plots Guass-Seidal method
    plt.imshow(phi)
    plt.savefig('Gauss-Seidal_method.png')
    plt.show()
    plt.clf()
