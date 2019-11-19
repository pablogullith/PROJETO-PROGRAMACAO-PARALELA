#Autores: Pablo Gullith de Melo Dantas e Gabriel Zuza Diniz 
#Bibliotecas 
import time
from mpi4py import *
from random import random
from numpy import array, pi

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


t1 = time.monotonic()

N = 10000000
k = 0
Atot = 4
for i in range(int(N/size)):
	x = -1.0+ 2*random()
	y = -1.0+ 2*random()
	if ((x**2+y**2)<1):
		k+=1	
ktot = comm.reduce(k, op=MPI.SUM, root = 0)
if (rank==0):
	pi_calc = (Atot*ktot)/N
	t2 = time.monotonic()
	print (pi_calc)
	print('O tempo que levou pro processo foi:',t2-t1)



#Houve um bom escalonamento 
