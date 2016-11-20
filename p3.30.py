# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:10:16 2016

@author: Administrator
"""

import pylab as pl
import math
class Billiard_Program :
    def __init__(self,i=0,initial_theta=math.pi/6,initial_velocity=1,total_time=80,\
                 initial_x=0.2,initial_y=0,time_step=0.01):
        self.theta=[initial_theta]
        self.v=[initial_velocity]        
        self.x=[initial_x]
        self.y=[initial_y]
        self.time=total_time
        self.dt=time_step
        self.t=[0]
        self.phi=[]
        self.v_x=[self.v[-1]*math.cos(self.theta[-1])]
        self.v_y=[self.v[-1]*math.sin(self.theta[-1])]
    def run(self):
        _time=0
        a=1
        r=1
        while(_time<self.time):
            self.x.append(self.x[-1]+self.v_x[-1]*self.dt)
            self.y.append(self.y[-1]+self.v_y[-1]*self.dt)
            if(self.y[-1]<-a*r and (pow(self.x[-1],2)+pow(self.y[-1]+a*r,2))>pow(r,2)):                
                self.x[-1]=self.x[-2]
                self.y[-1]=self.y[-2]
                while(1):                    
                    self.x.append(self.x[-1]+self.v_x[-1]*self.dt*0.01)
                    self.y.append(self.y[-1]+self.v_y[-1]*self.dt*0.01)
                    if(pow(self.x[-1],2)+pow(self.y[-1]+a*r,2)>pow(r,2)):  
                        cos_theta=self.x[-1]/r
                        sin_theta=(self.y[-1]+a*r)/r
                        vi_prependicular_x=abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*cos_theta
                        vi_prependicular_y=abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*sin_theta
                        vi_parallel_x=self.v_x[-1]-abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*cos_theta
                        vi_parallel_y=self.v_y[-1]-abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*sin_theta    
                        vf_parallel_x=vi_parallel_x
                        vf_parallel_y=vi_parallel_y
                        vf_prependicular_x=-vi_prependicular_x
                        vf_prependicular_y=-vi_prependicular_y
                        vf_x=vf_parallel_x+vf_prependicular_x
                        vf_y=vf_parallel_y+vf_prependicular_y
                        self.v_x.append(vf_x)
                        self.v_y.append(vf_y)
                        break
            if(self.y[-1]>a*r and (pow(self.x[-1],2)+pow(self.y[-1]-a*r,2))>pow(r,2)):                
                self.x[-1]=self.x[-2]
                self.y[-1]=self.y[-2]
                while(1):                    
                    self.x.append(self.x[-1]+self.v_x[-1]*self.dt*0.01)
                    self.y.append(self.y[-1]+self.v_y[-1]*self.dt*0.01)
                    if(pow(self.x[-1],2)+pow(self.y[-1]-a*r,2)>pow(r,2)):  
                        cos_theta=self.x[-1]/r
                        sin_theta=(self.y[-1]-a*r)/r
                        vi_prependicular_x=abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*cos_theta
                        vi_prependicular_y=abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*sin_theta
                        vi_parallel_x=self.v_x[-1]-abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*cos_theta
                        vi_parallel_y=self.v_y[-1]-abs(self.v_x[-1]*cos_theta+self.v_y[-1]*sin_theta)*sin_theta    
                        vf_parallel_x=vi_parallel_x
                        vf_parallel_y=vi_parallel_y
                        vf_prependicular_x=-vi_prependicular_x
                        vf_prependicular_y=-vi_prependicular_y
                        vf_x=vf_parallel_x+vf_prependicular_x
                        vf_y=vf_parallel_y+vf_prependicular_y  
                        self.v_x.append(vf_x)
                        self.v_y.append(vf_y)
                        break
            if(-a<self.y[-1]<a and self.x[-1]>1):
                self.x[-1]=self.x[-2]
                self.y[-1]=self.y[-2]
                while(1):                    
                    self.x.append(self.x[-1]+self.v_x[-1]*self.dt*0.01)
                    self.y.append(self.y[-1]+self.v_y[-1]*self.dt*0.01)
                    if(self.x[-1]>1):                
                        self.v_x.append(-self.v_x[-1])
                        break
            if(-a<self.y[-1]<a and self.x[-1]<-1):
                self.x[-1]=self.x[-2]
                self.y[-1]=self.y[-2]
                while(1):                    
                    self.x.append(self.x[-1]+self.v_x[-1]*self.dt*0.01)
                    self.y.append(self.y[-1]+self.v_y[-1]*self.dt*0.01)
                    if(self.x[-1]<-1):                
                        self.v_x.append(-self.v_x[-1])
                        break
            self.t.append(_time)            
            _time += self.dt
    def show_results(self):
        pl.plot(self.x,self.y)
        pl.title('$\alpha$ =1')
        pl.xlabel('x')
        pl.ylabel('y')
        pl.xlim(-3,3)
        pl.ylim(-3,3)
        pl.legend()
        pl.show()
a = Billiard_Program()
a.run()
a.show_results()  