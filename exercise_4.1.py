# -*- coding: utf-8 -*-
"""
Created on Fri Oct 07 16:47:35 2016

@author: Administrator
"""

import pylab as pl
class two_types_of_decay:
   def __init__(self, number_A = 100, number_B=0, time_constant = 1, time_duration = 10, time_step
 = 0.05):
        self.n_A = [number_A]
        self.n_B = [number_B]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.nsteps = int(time_duration // time_step + 1)
   def calculate(self):
        for i in range(self.nsteps):
            NA = self.n_A[i] + ( self.n_B[i] / self.tau - self.n_A[i] / self.tau) * self.dt
            NB = self.n_B[i] + ( self.n_A[i] / self.tau - self.n_B[i] / self.tau) * self.dt
            self.n_A.append(NA)
            self.n_B.append(NB)
            self.t.append(self.t[i] + self.dt)
   def show_results(self):
        pl.plot(self.t, self.n_A)
        pl.plot(self.t, self.n_B, 'r') 
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend(['$N_A$','$N_B$'])
        pl.grid()
        pl.show()
a = two_types_of_decay()
a.calculate()
a.show_results()


