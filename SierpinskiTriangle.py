import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random as ran
from PIL import Image
Nimg=512
im=Image.new("RGB",(Nimg,Nimg),"black")
x0=np.array([0.,0.])
#SIERPINSKI TRIANGLE
N=10000
p=np.array([1./3.,1./3.,1./3.])
m1=np.array([0.5,0.,0.,0.5,0.,0.]);
m2=np.array([0.5,0.,0.,0.5,0.5,0.]);
m3=np.array([0.5,0.,0.,0.5,0.25,np.sqrt(3.)/4.]);
x=np.zeros((N,2));
x[0,:]=x0;
#print x0
def x_new(x,m):
 x_n=np.array([m[0]*x[0]+m[1]*x[1]+m[4],m[2]*x[0]+m[3]*x[1]+m[5]]);
 return x_n
for i in range(N-3):
 p1=ran.random();
 if p1<=p[0]:
  x[i+1,:]=x_new(x[i,:],m1)
 if p1<=p[0]+p[1] and p1>p[0]:
    x[i+1,:]=x_new(x[i,:],m2)
 if p1<=np.sum(p) and p1>p[0]+p[1]:
     x[i+1,:]=x_new(x[i,:],m3)
# print x[i+1,:]
 im.putpixel((int(Nimg*x[i+1,0]),int(Nimg*x[i+1,1])),(143, 0, 255))
 print int(Nimg*x[i+1,0]),int(Nimg*x[i+1,1])
plt.scatter(tuple(x[:,0]),tuple(x[:,1]));
#plt.show()
im.save("sierpinski.png","PNG")
