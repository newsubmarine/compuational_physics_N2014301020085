# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 23:39:03 2017

@author: Administrator
"""
from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math

dx=1
dt=0.25
D=1./2*(dx**2)/dt
x=[-50]
y=[-50]
#the density of x=0 is 1 ,others are 0
rho=[[([0]*101)for i in range(101)] for j in range(101)]
for i in[50]:
    for j in [50]:
        rho[0][i][j]=1
  
    
def run():
    for n in range(0,100):
        x.append(x[-1]+1)
        y.append(y[-1]+1)
        for i in range(0,100):
            for j in range(0,100):
                rho[n+1][i][j]=rho[n][i][j]+(D*dt/(dx**2))*(rho[n][i][j+1]+rho[n][i][j-1]+
                    rho[n][i+1][j]+rho[n][i-1][j]-4*rho[n][i][j])
            #rho[i-1][n]=(rho[i-1][n]+rho[i][n])*0.5            
run()  

def show_result():
    X,Y=np.meshgrid(x,y)
    fig = figure(figsize=[8,8])
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, r,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('density')
    title('t=0')
    fig = figure(figsize=[8,8])
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, x2,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('density')
    ax.set_zlim(0,1)
    title('t=10')
    fig = figure(figsize=[8,8])
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, x3,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('density')
    ax.set_zlim(0,1)
    title('t=90')
    show()
show_result()
"""
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
"""