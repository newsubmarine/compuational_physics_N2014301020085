# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 23:39:03 2017

@author: Administrator
"""
import math 
import numpy as np
import matplotlib.pyplot as plt


dx=1
dt=0.5
D=1./2*(dx**2)/dt
x=[-50]
#the density of x=0 is 1 ,others are 0
rho=[([0]*101)for i in range(101)]
for n in [50]:
    rho[0][n]=1
  
    
def run():
    for i in range(0,100):
        x.append(x[-1]+1)
        for n in range(0,100):
            rho[i+1][n]=rho[i][n]+(D*dt/(dx**2))*(rho[i][n+1]+rho[i][n-1]-2*rho[i][n])
            #rho[i-1][n]=(rho[i-1][n]+rho[i][n])*0.5            
run()  

def show_result():  
    
   plt.title('One-dimsenional Diffusion')    
   plt.subplot(131)
   plt.plot(x,rho[0],label="step number=0")
   plt.plot(x,rho[0],'b.')   
   plt.xlabel('x')
   plt.ylabel(r'$\rho{(x)}$')  
   plt.xlim(-50,50)
   plt.title('One-dimsenional Diffusion',fontsize=10)
   plt.legend(loc="best",fontsize=10)
   
   plt.subplot(132)
   plt.plot(x,rho[10],label="step number=10")
   plt.plot(x,rho[10],'b.')   
   plt.xlabel('x')
   plt.ylabel(r'$\rho{(x)}$')  
   plt.xlim(-50,50)
   plt.title('One-dimsenional Diffusion',fontsize=10)  
   plt.legend(loc="best",fontsize=10)
   
   plt.subplot(133)
   plt.plot(x,rho[90],label="step number=90")
   plt.plot(x,rho[90],'b.')
   plt.xlabel('x')
   plt.ylabel(r'$\rho{(x)}$')  
   plt.xlim(-50,50)
   plt.title('One-dimsenional Diffusion',fontsize=10)
   plt.legend(loc="best",fontsize=10)
   plt.show()
show_result()
