# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 23:06:45 2017

@author: Administrator
"""
import math 
import numpy as np
import matplotlib.pyplot as plt


dx=1
dt=1
x=[-50]
D=1.0/4*(dx**2)/dt
#the density of x=0 is 1 ,others are 0
rho=[([0]*101)for i in range(101)]
for n in [50]:
    rho[0][n]=1
  
    
def run():
    for i in range(0,100):
        x.append(x[-1]+1)
        for n in range(0,100):
            rho[i+1][n]=rho[i][n]+(D*dt/(dx**2))*(rho[i][n+1]+rho[i][n-1]-2*rho[i][n])
            
run()  

def show_result():    
    plt.plot(x,rho[5],label="step number=5")
    plt.plot(x,rho[20],label="step number=20")
    plt.plot(x,rho[100],label="step number=100")
    plt.legend()
    plt.title('One-dimsenional Diffusion')
    plt.xlabel('x')
    plt.ylabel(r'$\rho{(x)}$')
    plt.xlim(-50,50)
    plt.show()
show_result()