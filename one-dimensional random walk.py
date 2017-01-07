# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 21:16:20 2017

@author: Administrator
"""
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import random
import math
class randomwalk :
    def __init__(self,timestep=1,number=100,totaltime=100):
        self.t=[0]
        self.number=number
        self.x2ave=[0]
        self.time=totaltime
        self.timestep=timestep
    def run(self):
        for i in range(self.number):
            self.x=[0] 
            for j in range(self.time):
                rnd=random.random()
            if rnd<=0.5:
                self.x.append(self.x[-1]-1)
            else:
                self.x.append(self.x[-1]+1)
                self.t.append(self.t[-1]+self.timestep)
                self.x2ave.append(self.x2ave[-1]+self.x[-1]*self.x[-1])
    def show_results(self):
        self.a=np.polyfit(self.t,self.x2ave,1)
        self.z=np.polyval(self.a,self.t)
        p=np.poly1d(self.a)   
        plt.plot(self.t,self.z,'r',label='linear')
        plt.plot(self.t,self.x2ave,'.',label='raw')
        plt.xlabel('time=step number')
        plt.ylabel('$<x^2>$')
        plt.legend()
        plt.text(10,40,p)
        plt.axis()
        plt.grid(True)
        plt.title('one-dimensional Random walk')
        print(p)
        plt.show
    
a = randomwalk()
a.run()
a.show_results()
        
        
        
