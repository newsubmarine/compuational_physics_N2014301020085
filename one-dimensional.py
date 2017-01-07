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
    def __init__(self,timestep=1,totaltime=100,number=500):
        self.x=[0]
        self.t=[0]
        self.x2ave=[0]
        self.time=totaltime
        self.timestep=timestep
        self.number=number
    def run(self):
        for i in range(self.number):
            self.x=[0] 
            for i in range(self.time):
                rnd=random.random()
                if rnd<=0.5:
                    self.x.append(self.x[-1]-1)
                else:
                    self.x.append(self.x[-1]+1)
                self.t.append(self.t[-1]+self.timestep)
                self.x2ave.append(self.x2ave[-1]+self.x[-1]*self.x[-1])
    def show_results(self):
        plt.plot(self.t,self.x2ave,'.')
        plt.xlabel('time')
        plt.ylabel('x')
        plt.legend()
        plt.title('Random walk')
        plt.show
    
a = randomwalk()
a.run()
a.show_results()
        
        
        