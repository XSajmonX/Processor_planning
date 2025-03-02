import FCFS,LCFS
import numpy as np
from numpy import random

p = input("Podaj ilość procesów: ") #ilość procesów
p = int(p)
tab = np.array([],type(int)) # tablica procesow
for i in range(0,p):
    t1 = random.randint(100) # generowanie czasu przyjscia
    t2 = random.randint(1,10) # generowanie dlugsci wykonywania procesu - losowo
    #t2 = random.randint(2, t1+4) # generowanie dlugsci wykonywania procesu - rośnie z czasem
    p1 = np.array([t1, t2])
    #print(p1)
    tab = np.append(tab, [0])
    tab[i]=p1 # dodawanie kolejnego procesu do tablicy glownej
print("wartosc procesu 1: "+str(tab[1]))
print("ilosc procesow: "+str(tab.size))
tab1 = tab.copy()

w = open("Wynik.txt", 'w')
w.write("Ilosc procesow: {}\n".format(p))

FCFS.fcfs_planning(tab,p,w)
LCFS.lcfs_planning(tab1,p,w)

w.close()