import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random as ran
from PIL import Image
Nimg=512
im=Image.new("RGB",(Nimg,Nimg),"black")
x0=np.array([0.,0.])
# Barnsley fern
N=10000
p=np.array([0.73,0.13,0.11,0.03])
m1=np.array([0.85,0.04,-0.04,0.85,0.0,1.6]);
m2=np.array([0.2,-0.26,0.23,0.22,0.0,1.6]);
m3=np.array([-0.15,0.28,0.26,0.24,0.0,0.44]);
m4=np.array([0.0,0.0,0.0,0.16,0.0,0.0]);
x=np.zeros((N,2));
x[0,:]=x0;

def x_new(x,m):
 x_n=np.array([m[0]*x[0]+m[1]*x[1]+m[4],m[2]*x[0]+m[3]*x[1]+m[5]]);
 return x_n
for i in range(N-3):
 p1=ran.random();
 if p1<=p[0]:
  x[i+1,:]=x_new(x[i,:],m1)
 if p1<=p[0]+p[1] and p1>p[0]:
    x[i+1,:]=x_new(x[i,:],m2)
 if p1<=p[0]+p[1]+p[2] and p1>p[0]+p[1]:
     x[i+1,:]=x_new(x[i,:],m3)
 if p1<=np.sum(p) and p1>p[0]+p[1]+p[2]:
     x[i+1,:]=x_new(x[i,:],m4)
x[:,0]=x[:,0]/np.max(abs(x[:,0]))
x[:,1]=x[:,1]/np.max(abs(x[:,1]))
x0_min=np.min(x[:,0]);
x1_min=np.min(x[:,1]);
pixel_x=np.zeros(N)
pixel_y=np.zeros(N)
for j in range(len(x[:,0])):
 x[j,0]=x[j,0]-x0_min
 x[j,1]=x[j,1]-x1_min
 pixel_x[j]=int(Nimg*x[j,0])
 pixel_y[j]=int(Nimg*x[j,1])
 #im.putpixel((int(Nimg*x[j,0]),int(Nimg*x[j,1])),(63,255,0))
pixel_x=pixel_x/np.max(pixel_x)*Nimg
pixel_y=pixel_y/np.max(pixel_y)*Nimg

for k in range(len(pixel_x)):
    #print int(pixel_x[k]),int(pixel_y[k])
    if int(pixel_x[k])==512 or int(pixel_x[k])==0 or int(pixel_y[k])==512 or int(pixel_y[k])==0: 
     print np.abs(int(pixel_x[k]-1)),np.abs(int(pixel_y[k]-1))
     im.putpixel((np.abs(int(pixel_x[k]-1)),np.abs(int(pixel_y[k]-1))),(143, 0, 255)) 
    else:
         print int(pixel_x[k]),int(pixel_y[k])
         im.putpixel((int(pixel_x[k]),int(pixel_y[k])),(143, 0, 255))
#plt.scatter(tuple(x[:,0]),tuple(x[:,1]));
#plt.show()
im.save("fern.png","PNG")
