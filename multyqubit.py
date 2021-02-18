#!/usr/bin/env python
# coding: utf-8

# In[17]:


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


def getu(dimension):
    u=np.zeros((dimension,dimension),dtype='float64')#規格化するためのベクトル
    u[0]=v[0]
    x=0
    sum=np.array([0,0],dtype='float64')
    for a in range(1,dimension):
        for b in range(0,a):
            sum+=gram(u[b],v[a])
        u[a]=v[a]-sum
    return u

u=getu(dimension)
print(u)

for c in range(0,dimension):
    e[c]=u[c]/LA.norm(u[c],2)#·ord=2
    
print(e)


# In[18]:


#psi=np.random.random((dimension))
#psi=e[0]
psi=np.array([e[0]])
print(psi)
print(LA.norm(psi,2))   #ノルム確認


# In[19]:


np.dot(np.dot(psi,e),psi.T)


# In[27]:


f=0
for a in range(0,10000):
    u=getu(dimension)
    for c in range(0,dimension):
        e[c]=u[c]/LA.norm(u[c],2)#·ord=2
    psi=psi=np.array([e[0]])
    d=np.dot(np.dot(psi,e),psi.T)
    if(d>=0):
        f=f+1
        
print(f)


# # 多量子ビット系

# In[28]:


for a in range(0,2):
    


# In[ ]:




