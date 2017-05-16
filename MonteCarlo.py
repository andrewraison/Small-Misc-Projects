##Uses the Monte Carlo method to integrate the function:
##    f = 10^6 * sin(x_0 + x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7)
##over all 8 varibles from 0 to pi/8
##
##It also gives an error plot comparing to the analytical answer

import numpy as np
import time
from numpy import pi
import matplotlib.pyplot as plt
import pdb
import math


#get the seed from the time and initialise the generator
seed = round(time.time())
np.random.seed(seed)


#allows the current seed to be seen and gives the option to enter a new one
def seeds(seed):
    print(seed, '\nIf you want to change seed enter y')
    newSeed = "n"
    newSeed = input(' ')
    if newSeed == "y":
        print('enter new seed')
        s = input(' ')
        seed = int(s)
    return seed
    

#creates a random distribution with the correct range and array structure
def sample(N, dimensions, ranges, seed):
    sample_0to1 = np.random.rand(N,dimensions)
    if (ranges.size == 1):
        rang = ranges[0]
        tmp = rang*sample_0to1
        return tmp
    else:
        return NULL


#does a single Monte Carlo Intergration at a high N
def monteCarloIteration():
    N=10**7
    dimensions = 8
    rang = np.array([pi/8])
    Volume = rang[0]**dimensions
    sample1 = sample(N,dimensions,rang, seed)
    #f refers to the function f in the handout
    f = np.sin(sample1.sum(axis=1))
    mean_f = (f.sum())/N
    mean_fsquared = ((f**2).sum())/N
    integrationPlus = 10**6*Volume*(mean_f + (((mean_fsquared - mean_f**2)/N)**0.5))
    integrationMinus = 10**6*Volume*(mean_f - (((mean_fsquared - mean_f**2)/N)**0.5))
    return (integrationPlus + integrationMinus)/2


##################################################################################################


#does many Monte Carlo Integrations at a varity of N, and plots the standard deviations on a graph
def errorPlot():
    nt=100
    Nmany = np.linspace(10,10**3,200)
    Ntot = nt*Nmany.sum()
    Nplot = Nmany[1:Nmany.size]
    dimensions = 8
    rang = np.array([pi/8])
    Volume = rang[0]**dimensions

    #get all the random numbers that will be used in the loop (unique sets for each iteration of the integration)
    sample2 = sample(Ntot,dimensions,rang, seed)
    f = np.sin(sample2.sum(axis=1))
    
    cumlative = 0
    intPlus = np.empty((Nmany.size,1))
    intMinus = np.empty((Nmany.size,1))
    errorP = np.empty((Nmany.size,1))
    errorM = np.empty((Nmany.size,1))

    #i loops over the values in Nmany, while j loops over the nt iterations of each value of Nmany
    for i in range(0,Nmany.size):
        intP = np.empty((nt,1))
        intM = np.empty((nt,1))
        for j in range(0,nt):
            #pick the next Nmany values from the set of random numbers
            x=f[cumlative + j*Nmany[i]:(cumlative + (j+1)*Nmany[i])]
            
            mean = (x.sum())/Nmany[i]
            meansquare = ((x**2).sum())/Nmany[i]
            intP[j] = 10**6*Volume*(mean + ((math.fabs(meansquare - mean**2)/Nmany[i])**0.5))
            intM[j] = 10**6*Volume*(mean - ((math.fabs(meansquare - mean**2)/Nmany[i])**0.5))
        intPlus[i] = (intP.sum())/nt
        intMinus[i] = intM.sum()/nt
        errorP[i] = np.std(intP)
        errorM[i] = np.std(intM)
        cumlative += Nmany[i]*nt



#   plot the error against the sample size, and plotting the expected N^-0.5 trend against it

    plt.plot(Nmany,errorP.flatten(),'r',label='Monte Carlo integrations')
    #32.5 is included as a scale factor so the 2 lines lie on top of each other
    plt.plot(Nmany,32.5*(Nmany**-0.5),'b',label='N^-0.5')
    plt.title('Error against N, and the expected N^-0.5')
    plt.ylabel('Error')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('N')
    plt.legend(loc='best')
    plt.savefig('MonteCarloError-Ex1Core.png',bbox_inches='tight')



##################################################################################################


#gives options for choosing which part of the program to run
def options():
    print('\nEnter e to get the error plot against N')
    print('Enter m to do the most accurate Monte Carlo inegration')
    print('Enter s to show the current seed and give option to enter a new seed')
    print('Enter q to quit')


choice ="x"
options()


#loops over the choice selection until the user quits the program
while choice != "q":
        choice = input("")
        if choice == "e":
            errorPlot()
            options()
            
        elif choice == "m":
            nt = 25
            values = np.empty((nt,1))
            #do the loop nt times and give the average as the estimate
            for i in range(0,nt):
                values[i] = monteCarloIteration()
            estimate = values.sum()/nt
            print(estimate)
            print(np.std(values))
            options()
            
        elif choice == "s":
            seed2 = seeds(seed)
            #check to see if the seed has changed, if so reseed the generator
            if seed2 != seed:
                seed = seed2
                np.random.seed(seed)
            options()
            
        elif choice =="q":
            break
        
        else:
            print('\nThat was not a valid option, try again:')
            #pause so that the message insn't lost in the options
            time.sleep(1)
            options()
