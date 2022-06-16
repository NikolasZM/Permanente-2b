# Permanente-2b
Implementación de 2 algoritmos de ordenamiento en Python.
Autor: Nikolas Zuñiga Monroy<br>
<h2>¿Qué se hizo?</h2>
Se implemento los 2 algoritmos de ordenamiento dados en Python, y se realizaron dos gráficas, las cuales se encuentran en el archivo Excel, donde compara el tiempo en segundos con la cantidad de elementos ordenados (n).<br>
Los valores se realizarón en el mejor de los casos.<br>
<h2>Ejemplo del primer algoritmo:</h2>
import time<br>
s=time.time()<br>
def insertion_short(A):<br>
    ___for j in range(len(A)):<br>
       ______ key=A[j]<br>
        ______i=j-1<br>
        ______while i>=0 and key < A[i]:<br>
            _________A[i+1] = A[i]<br>
            _________i=i-1<br>
        ______A[i+1]=key<br>
    ___return A<br>
A=[_]<br>
for i in range(10000000):<br>
    A.append(i)<br>
insertion_short(A)<br>
e=time.time()<br>
print(e - s)<br>
