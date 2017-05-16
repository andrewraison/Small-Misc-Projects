##Uses the fast fourier transform to calculate diffraction patterns
##using Huygen's construction.
##Compares this to the analytical approximation appropriate to the problem


import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

samplesize = 2**9
L = 5*10**-3
d = 10**-4
D = 1
wavelength = 5*10**-7
k = 2*pi/(wavelength)
dx = L/samplesize
x = np.linspace(-L/2,L/2,samplesize)

freq = np.linspace(-1/(2*dx),1/(2*dx),samplesize)
y = freq*wavelength*D

#fresnel will equal 1 or 0, to remove the fresnel correct if required
def singleSlit(L,ss,d,fresnel,x,k,D):
    appature = np.zeros(ss, dtype='complex128')
    exponent = x[ss/2 - d*ss/(2*L) : ss/2 + d*ss/(2*L)]**2*k/(2*D)
    appature[ss/2 - d*ss/(2*L) : ss/2 + d*ss/(2*L)] = np.exp(1J * fresnel*exponent)
    return appature

def FFT(L,ss,d,fresnel,x,k,D):
    transform = dx*np.fft.fft(singleSlit(L,ss,d,fresnel,x,k,D))
    centeredTransform = np.hstack((transform[ss/2:ss],transform[0:ss/2]))
    return (np.abs(centeredTransform))**2/(wavelength*D)

def sincIntensity(y,d,wavelength,D):
    Sinc = np.sinc(y*d/(wavelength*D))
    intensity = (d*Sinc)**2/(wavelength*D)
    return intensity


plt.figure(1)
plt.plot(y,FFT(L,samplesize,d,0,x,k,D),'b',label='Fast fourier transform')
plt.plot(y,sincIntensity(y,d,wavelength,D),'r',label='Analytic transform')
plt.title('Analytic and computational solutions to the single slit problem in the Fraunhofer regime')
plt.xlabel('y /m')
plt.ylabel('Intensity')
plt.legend(loc='best')
plt.savefig('SingleSlitFraunhoferRegime-Ex3ACore1.png',bbox_inches='tight')


####################################################################

#Supplementary task

D2 = 5*10**-3

plt.figure(2)
plt.plot(y,FFT(L,samplesize,d,1,x,k,D2))
plt.title('Solution to the single slit problem in the Fresnel regime')
plt.xlabel('y /m')
plt.ylabel('Intensity')
plt.savefig('SingleSlitFresnelRegime-Ex3ASup1.png',bbox_inches='tight')
