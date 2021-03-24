import numpy as np
from numpy import linalg as LA
import math
import random


#任意次元のベクトルを生成する関数
#nは生成したい次元
def qubit(n):
    e=np.zeros(n,dtype='float64')
    e[0]=random.random()
    unf=1-e[0]
    for i in range(1,n-1):
        e[i]=random.uniform(0,unf)
        unf=unf-e[i]
    e[n-1]=unf
    return e


#ランダムなベクトルを規格化し、状態ベクトルになる．
def normal(e):
    n=e.size                                 #配列の次元を確認する関数
    E=np.zeros(n,dtype='float64')
    for i in range(0,n):
        E[i]=np.sqrt(e[i])
    return E


#ベクトルの間のテンソル積
def tensor(a,b):
    n1=a.size
    n2=b.size
    P=np.zeros(n1*n2,dtype='float64')
    for i in range(0,n1):
        for j in range(0,n2):
            P[i*n2+j]=a[i]*b[j]
    return P

#xはn1次元のベクトル、yはn2次元のベクトルとおく、zの次元はn1*n2である
x=normal(qubit(2))
y=normal(qubit(3))
z=tensor(x,y)

print(x)
print(y)
print(z)


#ノルムの確認
print(LA.norm(x,2))
print(LA.norm(y,2))
print(LA.norm(z,2))
