##Uses fast fourier transform to plot the Fraunhofer diffraction pattern

import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

samplesize = 2**9
L = 10**-2
d = 2*10**-3
D = 10
wavelength = 5*10**-7
k = 2*pi/(wavelength)
dx = L/samplesize
s = 10**-4
m=8

freq = np.linspace(-1/(2*dx),1/(2*dx),samplesize)
y = freq*wavelength*D


#Calculating the phase shift at every point along the grating
#The fresnel parameter is either 1 or 0 depending on if it is the Fresnel regime required
def phaseShift(m,s,d,dx,k,D,fresnel):
    a = np.linspace(-d/2,d/2,d/dx)
    exponent = (m/2)*np.sin(2*pi*a/s) + fresnel*(a**2)*k/(2*D)
    shift = np.exp(1J * exponent)
    return shift

def sineGrate(L,ss,d,m,s,k,D,fresnel):
    grating = phaseShift(m,s,d,L/ss,k,D,fresnel)
    padding = np.zeros((ss-grating.size)/2)
    appature = np.hstack((padding,grating,padding))
    return appature

def FFT(L,ss,d,m,s,k,D,fresnel):
    transform = dx*np.fft.fft(sineGrate(L,ss,d,m,s,k,D,fresnel))
    centeredTransform = np.hstack((transform[ss/2:ss],transform[0:ss/2]))
    return (np.abs(centeredTransform))**2/(wavelength*D)



plt.figure(1)
plt.plot(y,FFT(L,samplesize,d,m,s,k,D,0),'b')
plt.title('Sinesoidal phase grating in the Fraunhofer regime')
plt.xlabel('y /m')
plt.ylabel('Intensity')
plt.savefig('SinusoidalPhaseGratingFraunhofer-Ex3ACore2.png',bbox_inches='tight')


##################################################################

#Supplementary task

D2 = 0.5

plt.figure(2)
plt.plot(y,FFT(L,samplesize,d,m,s,k,D2,1),'b')
plt.title('Sinesoidal phase grating in the Fresnel regime')
plt.xlabel('y /m')
plt.ylabel('Intensity')
plt.savefig('SinusoidalPhaseGratingFresnel-Ex3ASup1.png',bbox_inches='tight')
