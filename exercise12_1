from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy
from pylab import *
V0=[[[0 for i in range(21)]for j in range(21)]for k in range(21)]#i represents x, j represents y

VV=[]
VV.append(V0)
s=0
dx=0.1

p0=[[[0 for i in range(21)]for j in range(21)]for k in range(21)]
for i in [10]:
    for j in [10]:
        for k in [10]:
            p0[k][j][i]=1/dx**3

p=[]
p.append(p0)

while True:
    VV.append(V0)
    p.append(p0)
    for m in range(1,len(V0)-1):
        for j in range(1,len(V0[1])-1):
            for i in range(1,len(V0[1][1])-1):
                VV[s+1][m][j][i]=(VV[s][m][j][i+1]+VV[s][m][j][i-1]+VV[s][m][j+1][i]+VV[s][m][j-1][i]+VV[s][m+1][j][i]+VV[s][m-1][j][i])/6.0+p[s][m][j][i]*dx**2/6.0

                

    VV[s]=np.array(VV[s])
    VV[s+1]=np.array(VV[s+1])
    dVV=VV[s+1]-VV[s]

    dV=0
    for k in range(len(V0)):
        for j in range(1,len(V0[1])-1):
            for i in range(1,len(V0[1][1])-1):
                dV=dV+abs(dVV[k][j][i])
          
    s=s+1
    if dV<0.0001 and s>1:
        break
print s

V=np.array(VV[-1][10])
Ex=np.array(V0[10])
Ey=np.array(V0[10])
for j in range(1,len(V0[10])-1):
    for i in range(1,len(V0[10][1])-1):
        Ex[j][i]=-(V[j][i+1]-V[j][i-1])/(2*dx)
        Ey[j][i]=-(V[j+1][i]-V[j-1][i])/(2*dx)
figure(figsize=[8,8])
x=np.arange(-1.0,1.01,dx)
y=np.arange(-1.0,1.01,dx)
X,Y=np.meshgrid(x,y)
CS = contour(X,Y,V,8)
clabel(CS, inline=1, fontsize=10)
xlim(-0.5,0.5)
xlabel('x')
ylim(-0.5,0.5)
ylabel('y')
title('Equipotential lines around a point charge in 3D')
fig = figure(figsize=[8,8])
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, V,rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V')
title('electric potential')
fig.colorbar(surf, shrink=0.5, aspect=5)
figure(figsize=[8,8])
Q=quiver(X,Y,Ex,Ey,scale=100)
xlim(-1,1)
xlabel('x')
ylim(-1,1)
ylabel('y')
title('Field lines around a point charge in 3D')
show()
