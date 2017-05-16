##Supplementary tasks to the DrivenPendulum.py
##It involves using the same code by with different initial conditions

import numpy as np
from numpy import pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
import pdb

g=1
l=1
drivingFreq=2/3

def derivatives(y,t,g,l,q,F,drivingFreq):
    return [y[1],-(g/l)*(math.sin(y[0])) - q*y[1] + F*(math.sin(drivingFreq*t))]

#returns energy per mass
def energy(theta,thetadot,g,l):
#    pdb.set_trace()
    return g*l*(1-math.cos(theta)) + 0.5*((l*thetadot)**2)

#finds the first maximum of a function (excluding the first value if that is a maximum)
def max(y):
    i = 0
    found = 0
    while found == 0:
        i += 1
        if y[i]>y[i+1] and y[i]>y[i-1]:
            found = 1;
    return i


########################################################################

#Supplementary Task part1
F=0
maxtime = 5*10**1
q=np.array([1,5,10])
y0 = np.array([0.01,0.0])
t = np.linspace(0,maxtime,maxtime*10 + 1)

solutions = np.empty((t.size,2*q.size))

for i in range(0,q.size):
    sol = odeint(derivatives, y0, t, args=(g,l,q[i],F,drivingFreq))
    solutions[:,2*i:(2*i+2)]=sol

energies = np.empty((t.size,q.size))
for j in range(0,q.size):
    for i in range(0, t.size):
       energies[i,j] = energy(solutions[i,j*2],solutions[i,j*2+1],g,l)


plt.figure(1)
plt.plot(t,solutions[:,0],'b',label=q[0])
plt.plot(t,solutions[:,2],'r',label=q[1])
plt.plot(t,solutions[:,4],'g',label=q[2])
plt.xlabel('time /s')
plt.ylabel('theta /rad')
plt.title('Damped solutions for various values of q, no driving force, theta plotted against time')
plt.legend(loc='best')
plt.savefig('DampedSolnsVariousq-Ex2ASup1.png',bbox_inches='tight')



plt.figure(2)
plt.plot(t[0:300],energies[0:300,0],'b',label=q[0])
plt.plot(t[0:300],energies[0:300,1],'r',label=q[1])
plt.plot(t[0:300],energies[0:300,2],'g',label=q[2])
plt.xlabel('time /s')
plt.ylabel('Energy /J')
plt.title('Damped solutions for various values of q, no driving force, energy plotted against time')
plt.legend(loc='best')
plt.savefig('DampedSolnsVariousqEnergy-Ex2ASup1.png',bbox_inches='tight')


#########################################################################

#Supplementary Task part2

q2 = 0.5
F2 = np.array([0.5,1.2,1.44,1.465,0.7,1.3,1.0])

solutions2 = np.empty((t.size, 2*F2.size))

for i in range(0,F2.size):
    sol = odeint(derivatives, y0, t, args=(g,l,q2,F2[i],drivingFreq))
    solutions2[:,2*i:(2*i+2)]=sol

period = np.empty((F2.size,1))
for i in range(0,F2.size):
    period[i] = t[max(solutions2[:,2*i])]


#theta not modded by 2pi so that the graphs are more legible
plt.figure(3)
plt.plot(t,solutions2[:,0],'b',label=F2[0])
plt.plot(t,solutions2[:,2],'r',label=F2[1])
plt.plot(t,solutions2[:,4],'g',label=F2[2])
plt.plot(t,solutions2[:,6],'m',label=F2[3])
plt.axis([t[0],t[t.size-1],-pi,pi])
plt.xlabel('time /s')
plt.ylabel('theta /rad')
plt.title('Damped solutions for various values of driving forces, q=0.5, theta plotted against time')
plt.legend(loc='best')
plt.savefig('DampedSolnsVariousDrivingForce-Ex2ASup1.png',bboc_inches='tight')


plt.figure(4)
plt.plot(F2,period,'bo')
plt.xlabel('Period /(1/t)')
plt.ylabel('Driving force amplitude')
plt.title('The period of oscillation plotted against the driving force amplitude')
plt.axis([0,1.5,0,6])
plt.savefig('PeriodAgainstDrivingForceAmplitude-Ex2ASup1.png',bbox_tight='tight')


#########################################################################

#Supplementary Task part3

tmax = 10**4
t2 = np.linspace(0,tmax,tmax*10+1)
y0[0] = 0.2

point2sol = odeint(derivatives, y0, t2, args=(g,l,q2,F2[1],drivingFreq))
point20001sol = odeint(derivatives, [y0[0]+0.00001,y0[1]], t2, args=(g,l,q2,F2[1],drivingFreq))



#theta not modded by 2pi so that the graphs are more legible
plt.figure(5)
plt.plot(t2,point2sol[:,0],'b', label='initial theta = 0.2')
plt.plot(t2,point20001sol[:,0],'g',label='intial theta = 0.20001')
plt.xlabel('time /s')
plt.ylabel('theta /rad')
plt.title('Solutions for very slightly different initial theta, q=0.5, driving force amplitude =1.2')
plt.legend(loc='best')
plt.savefig('ThetaEvolutionWithSlightlyDifferentInitialConditons-Ex2ASup1.png',bbox_inches='tight')
