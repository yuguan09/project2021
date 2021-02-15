#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from numpy import linalg as LA


dimension=2   #次元を指定する

def randomnumber(dimension): #ランダムな行列の生成
    return np.random.random((dimension,dimension))


def gram(a,b):   #規格化
    return ((np.dot(a,b)/np.dot(a,a))*a)


def hermatite(a): #複素共役
    return np.conjugate(a.T)

v=randomnumber(dimension)
e=np.zeros((dimension,dimension),dtype='float64')#エルミット演算子を生成する単位ベクトル

u=np.zeros((dimension,dimension),dtype='float64')#規格化するためのベクトル
u[0]=v[0]

x=0
sum=np.array([0,0],dtype='float64')

for a in range(1,dimension):
    for b in range(0,a):
        sum+=gram(u[b],v[a])
    u[a]=v[a]-sum
    

for c in range(0,dimension):
    e[c]=u[c]/LA.norm(u[c],2)#·ord=2
    
print(e)


# In[8]:


for c in range(0,dimension):
    e[c]=u[c]/LA.norm(u[c],2)#·ord=2
    
print(e)


# In[ ]:




