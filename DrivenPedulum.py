##Uses an ODE solver in scipy to solve the equation:
##    d^2(theta)/dt^2 = -(g/l)*sin(theta) - q* d(theta)/dt + F*sin(omega*t)
##By splitting it into 2 coupled first order equations


import numpy as np
from numpy import pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

#constants that don't change over the task
g=1
l=1
drivingFreq=2/3


def derivatives(y,t,g,l,q,F,drivingFreq):
    return [y[1],-(g/l)*(math.sin(y[0])) - q*y[1] + F*(math.sin(drivingFreq*t))]

#returns energy per mass
def energy(theta,thetadot,g,l):
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

##################################################################

#A single undamped oscillator (not driven) over a long time

q=0
F=0
y0 = np.array([0.01,0.0])
t = np.linspace(0,10**5,1000001)
sol = odeint(derivatives, y0, t, args=(g,l,q,F,drivingFreq))

analytic = y0[0]*np.cos((g/l)**0.5*t) + y0[1]*np.sin((g/l)**0.5*t)


energies = np.empty((t.size,1))
for i in range(0, t.size -1):
    y = sol[i,1]
    energies[i] = energy(sol[i,0],sol[i,1],g,l)



plt.figure(1)
#Plot of the first 10 seconds of theta, omega and the analytical solution
plt.subplot(221)
plt.plot(t[0:100], sol[0:100, 0], 'b', label='theta(t)')
plt.plot(t[0:100], sol[0:100, 1], 'g', label='omega(t)')
plt.plot(t[0:100], analytic[0:100], 'r', label='analytic solution')
plt.legend(loc='best')
plt.ylabel('theta /rad')
plt.xlabel('t /s')
#Plot of theta, omega and the analytical solution at a large t
plt.subplot(222)
plt.plot(t[900000:900100], sol[900000:900100, 0], 'b', label='theta(t)')
plt.plot(t[900000:900100], sol[900000:900100, 1], 'g', label='omega(t)')
plt.plot(t[900000:900100], analytic[900000:900100], 'r', label='analytic solution')
plt.axis([t[900000],t[900100],-y0[0],y0[0]])
plt.legend(loc='best')
plt.ylabel('theta /rad')
plt.xlabel('t /s')
#Plot of the entire run of theta
#(for a trend of the maximum, the individual oscilations can't be resloved)
plt.subplot(223)
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.legend(loc='best')
plt.xlabel('t /s')
plt.ylabel('theta /rad')
plt.savefig('ThetaAgainstTime-Ex2ACore.png',bbox_inches='tight')


#Plot of the total energy against time
plt.figure(2)
plt.plot(t,energies)
plt.title('Total Energy against time')
plt.xlabel('t /s')
plt.ylabel('Total Energy /J')
plt.savefig('TotalEnergyAgainstTime-Ex2ACore.png',bbox_inches='tight')


####################################################################

#Calculate periods for various initial thetas

N = 100
t = np.linspace(0,100,1001)
period = np.empty((N,1))
theta0 = np.linspace(0,pi,N+1)

#theta0 = 0 not actually calculated because this is a stationary pendulum (undefined period)
for i in range(0,N):
    solution = odeint(derivatives,[theta0[i+1],0],t, args=(g,l,q,F,drivingFreq))
    period[i] = t[max(solution[:,0])]

    
plt.figure(3)
plt.plot(theta0[1:N+1],period)
plt.title('Period against the initial theta')
plt.xlabel('Theta /rad')
plt.ylabel('Period /t')
plt.savefig('PeriodOfOscillationAgainstInitialTheta-Ex2ACore.png',bbox_inches='tight')


print('Period when theta0 = pi/2:',t[max(odeint(derivatives,[pi/2,0],t, args=(g,l,q,F,drivingFreq))[:,0])])



