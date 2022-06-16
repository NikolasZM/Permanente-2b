from random import shuffle
import time
s=time.time()
#Segundo algoritmo implementado en python:
def bubb(L):
    n =len(L)
    for i in range(n-1):
        for j in range(n-1,i+1):
            if L[j]<L[j-1]:
                key = L[j]
                L[j]=L[j-1]
                L[j-1]=key
    return L

A=[]
for i in range(10000000):
    A.append(i)
A1=A[::-1]
bubb(A1)
e=time.time()
print(e - s)
