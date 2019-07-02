# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:21:57 2019

@author: 17pd04
"""

w=[-0.5,0.5,0.5]
X=[[0,0],[0,1],[1,0],[1,1]]
y=[0,0,0,1]
yc=[]
eta=0.5
teta=0
val=[]
for i in range(len(X)):
    summ=w[0]
    for j in range(len(X[0])):
        summ+=w[j+1]*X[i][j]
    if(summ>=teta):
        yc.append(1)
    else:
        yc.append(0)
    if(yc[i]==y[i]):
        print("\n\niteration ",i)
        print("x[0]=",X[i][0]," x[1]=",X[i][1]," y[i]=",y[i],"  yc[i]=",yc[i])
        print(" y :",y," yc :",yc)
        print(" w :",w)
        print(" sum:",summ)
        print(" val :",val)
        continue
    elif(y[i]==0 and yc[i]==1):
        count=len(w)
        val=[]
        val.append(eta)
        w[0]-=val[0]
        for jj in range(len(X[0])):
                val.append(eta*X[i][jj])
        for ii in range(1,count):
            w[ii]=w[ii]-val[ii]
        print("\n\niteration ",i)
        print("x[0]=",X[i][0]," x[1]=",X[i][1]," y[i]=",y[i],"  yc[i]=",yc[i])
        print(" y :",y," yc :",yc)
        print(" w :",w)
        print(" sum:",summ)
        print(" val :",val)
    elif(y[i]==1 and yc[i]==0):
        count=len(w)
        val=[]
        val.append(eta)
        w[0]+=val[0]
        for jj in range(len(X[0])):
                val.append(eta*X[i][jj])
        for ii in range(1,count):
            w[ii]=w[ii]+val[ii]
        print("\n\niteration ",i)
        print("x[0]=",X[i][0]," x[1]=",X[i][1]," y[i]=",y[i],"  yc[i]=",yc[i])
        print(" y :",y," yc :",yc)
        print(" w :",w)
        print(" sum:",summ)
        print(" val :",val)
    
    