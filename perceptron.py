# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:21:57 2019

@author: 17pd04
"""
import matplotlib.pyplot as plt

def statements():
    print("\n\niteration ",i)
    print("x[0]=",X[i][0]," x[1]=",X[i][1]," y[i]=",y[i],"  yc[i]=",yc[i])
    print(" y :",y," yc :",yc)
    print(" w :",w)
    print(" sum:",summ)
    print(" val :",val)

def scatplot(X,col):
    x1axis=[]
    x2axis=[]
    for i in range(len(X)):
        x1axis.append(X[i][0])
        x2axis.append(X[i][1])
    plt.scatter(x1axis,x2axis,c=col)



w=[-0.5,0.5,0.5]
X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1]
#X=[[0.958,0.003],[1.043,0.001],[1.907,0.003],[0.78,0.002],[0.579,0.001],[0.003,0.105],[0.001,1.748],[0.014,1.839],[0.007,1.021],[0.004,0.214]]
#y=[0,0,0,0,0,1,1,1,1,1]
eta=0.5
teta=0
val=[]
tot=0
while(1):
    print("Epoch : ",tot)
    yc,x2,x1=[],[],[]
    for i in range(len(X)):
        summ=w[0]
        for j in range(len(X[0])):
            summ+=w[j+1]*X[i][j]
        if(summ>=teta):
            yc.append(1)
            x1.append(X[i])
        else:
            yc.append(0)
            x2.append(X[i])
        if(yc[i]==y[i]):
            statements()
            continue
        else:
            val=[]
            val.append(eta)
            w[0]+=(val[0]*(y[i]-yc[i]))
            for jj in range(len(X[0])):
                    val.append(eta*X[i][jj]*(y[i]-yc[i]))
            for ii in range(1,len(w)):
                w[ii]+=val[ii]
            statements()
    if(y==yc):
        break
    tot+=1

scatplot(x1,'r')
scatplot(x2,'b')

x1int=(teta-w[0])/w[1]
x2int=(teta-w[0])/w[2]
if(x1int==x2int):
    slope=1
else:
    slope= -x2int/x1int

xa=list(plt.xlim())
ya=[]
for i in xa:
    ya.append(slope*i + x2int)
plt.plot(xa,ya,c='g')    
