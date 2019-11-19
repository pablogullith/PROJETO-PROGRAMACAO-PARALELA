from random import random

N = 10000000
k = 0
Atot = 4

for i in range(N):
    x = -1.0+2*random()
    y = -1.0+2*random()
    if ((x**2+y**2)<1):
        k+=1

pi_calc = Atot*k/N 
print (pi_calc)



#Testamos dois metodos de escalonamento de processos: o forte e o fraco, entre os processos
#o que apresentou um menor tempo de processamento foi o forte.
