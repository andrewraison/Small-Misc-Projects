##Uses scipy libraries to do the Fresnel integrals


import numpy as np
from numpy import pi
from scipy.integrate import quad
import matplotlib.pyplot as plt
import pdb
import math

#defining the 2 integrands
def cosIntegrand(x):
    return np.cos(pi*(x**2)/2)

def sinIntegrand(x):
    return np.sin(pi*(x**2)/2)

#defining the 2 integrals
def cosIntegral(x0, x1):
    c = np.array(quad(cosIntegrand, x0, x1))
    return c[0]

def sinIntegral(x0, x1):
    s = np.array(quad(sinIntegrand, x0, x1))
    return s[0]


def fresnelIntegral(x0,x1):
    C = cosIntegral(x0, x1)
    S = sinIntegral(x0, x1)
    return np.array([C,S])

################################################################
#Suplementary task 1
#calculates the cornu spiral
steps = 1000
uLimits = 15
u = np.linspace(-uLimits , uLimits, steps)
C = np.empty(steps)
S = np.empty(steps)
for i in range(0,steps):
    C[i] = cosIntegral(0, u[i])
    S[i] = sinIntegral(0, u[i])


plt.figure(1)
plt.plot(C,S)
plt.title('Cornu Spiral calculated numerically')
plt.ylabel('Fresnel sine integral')
plt.xlabel('Fresnel cosine integral')
plt.savefig('Cornu_Spiral-Ex1Sup1.png',bbox_inches='tight')


################################################################

#Suplementary task 2

wavelength =1
d = 10
D = np.array([30, 50, 100])
xLimits = 30
x = np.linspace(-xLimits, xLimits, steps)


amplitude = np.empty((steps,D.size))
phase = np.empty((steps,D.size))

#Doing the integral for each D within the loop
for i in range(0, 3):
    y=(2/(wavelength*D[i]))**0.5
    slit = d/2*y
    for j in range(0, steps):
        psi = fresnelIntegral(x[j]*y-slit,x[j]*y+slit)
        amplitude[j,i] = (psi**2).sum()
        phase[j,i] = math.atan(psi[1]/psi[0])


#plotting the amplitudes of each D
plt.figure(2)
plt.plot(x,amplitude[:,0],'r',label=D[0])
plt.plot(x,amplitude[:,1],'b',label=D[1])
plt.plot(x,amplitude[:,2],'g',label=D[2])
plt.title('Amplitude for various distances from the screen')
plt.ylabel('Amplitude')
plt.xlabel('x /cm')
plt.legend(loc='best')
plt.savefig('AmplitudeForVariousD-Ex1Sup2.png',bbox_inches='tight')


#plotting the phases, they are on different subplots because one plot was overcrowded 
plt.figure(3)

plt.subplot(221)
plt.plot(x,phase[:,0])
plt.ylabel('Phase')
plt.xlabel('x /cm')
plt.title('Phase for distance from the screen 30 cm')

plt.subplot(222)
plt.plot(x,phase[:,1])
plt.ylabel('Phase')
plt.xlabel('x /cm')
plt.title('Phase for distance from the screen 50 cm')

plt.subplot(223)
plt.plot(x,phase[:,2])
plt.ylabel('Phase')
plt.xlabel('x /cm')
plt.title('Phase for distance from the screen 100 cm')

plt.savefig('PhaseForVariousD-Ex1Sup2.png',bbox_inches='tight')
