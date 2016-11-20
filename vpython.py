# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:48:53 2016

@author: Administrator
"""

from visual import *
side = 5.0
thk = 0.01
s2 = 2*side - thk
s3 = 2*side + thk
wallR = box (pos=( side, 0, 0), size=(thk, s2, 0.5),  color = color.green)
wallL = box (pos=(-side, 0, 0), size=(thk, s2, 0.5),  color = color.green)
wallB = box (pos=(0, -side, 0), size=(s3, thk, 0.5),  color = color.green)
wallT = box (pos=(0,  side, 0), size=(s3, thk, 0.5),  color = color.green)
ball = sphere(pos=(0.2,0,0), color=color.blue, radius = 0.4, make_trail=True, retain=200)
ball.trail_object.radius = 0.05
ball.v = vector(0.5,0.3,0)
side = side - thk*0.5 - ball.radius
dt = 0.5
t=0.0
while True:
  rate(100)
  t = t + dt
  ball.pos = ball.pos + ball.v*dt
  if not (side > ball.x > -side):
    ball.v.x = -ball.v.x
  if not (side > ball.y > -side):
    ball.v.y = -ball.v.y