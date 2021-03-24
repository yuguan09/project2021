import numpy as np
from numpy import linalg as LA  #ユークリッドノルム
import random

def gram(a,b):
    return ((np.dot(a,b)/np.dot(a,a))*a)

#直交ベクトル
a=np.array([3,2,1])
b=np.array([2,1,3])
c=np.array([1,3,2])

Va=a
Vb=b-gram(Va,b)
Vc=c-gram(Va,c)-gram(Vb,c)
print(Va,Vb,Vc)
print(np.dot(Va,Vb))
#直交ベクトル

#絶対値
Ea=Va/LA.norm(Va,2)
Eb=Vb/LA.norm(Vb,2)
Ec=Vc/LA.norm(Vc,2)
print(Ea,Eb,Ec)
#絶対値
print(np.dot(Ea,Eb))