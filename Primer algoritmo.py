import time
s=time.time()
#Primer algortimo implementado en python:
def insertion_short(A):
    for j in range(len(A)):
        key=A[j]
        i=j-1
        while i>=0 and key < A[i]:
            A[i+1] = A[i]
            i=i-1
        A[i+1]=key
    return A
A=[]
for i in range(10000000):
    A.append(i)
insertion_short(A)
e=time.time()
print(e - s)