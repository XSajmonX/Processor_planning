import numpy as np

def fcfs_planning(tab,p,w):
    # Algorytm FCFS
    print("*************** Algorytm FCFS ***************")
    print(tab) # tablica wygenerowanych procesow
    print("*********************************************")

    #funkcja szukająca minimum w czasie naedjścia i zwraca jej indeks
    def minimun(tab,timer):
        min1 = tab[0][0]
        min2 = 0
        dl=tab.size
        for i in range(dl):


            if(tab[i][0]<min1):
                min1=tab[i][0]
                min2 = i

        if(tab[min2][0] <= timer): #sprawdza czy minimum jest zgodne z taktem
            return min2
        else: return -1

    f = open("Wynik_FCFS.txt",'w')
    timer=0 # kolejne takty procesora [s]
    a=1 # zmienna, ktora ustala czy proces sie wykonuje i jak dlugo
    wait=[] # tablica czasow oczekiwania procesow
    while True: # petla glowna w ktorej wykonuja sie procesy

        o=minimun(tab,timer)
        if(o==-1):
            print("procesor nie pracuje | czas: "+str(timer))
            f.write("procesor nie pracuje | czas: "+str(timer)+"\n")
        else:
            print("proces: "+str(tab[o])+" | czas: " + str(timer))
            f.write("proces: "+str(tab[o])+" | czas: " + str(timer)+"\n")
        if(o!=-1):
            if(a<tab[o][1]):
                a+=1
            elif(a==tab[o][1]): # zmienna a jest flagą (proces wykonuje sie)
                a=1
                sum=0
                sum=timer-tab[o][1]+1-tab[o][0]
                wait.append(int(sum)) #zapis czasu oczekiwania
                tab = np.delete(tab,o) # usunięcie procesu

        if(tab.size==0): # przerwanie petli
            break
        timer+=1 #zwiekszanie taktu

    w.write("*****FCFS******\n")
    # dane i statystyki
    print("Czas potrzebny na wykonanie wszystkich procesow: "+str(timer)+" [s]")
    w.write("Czas potrzebny na wykonanie wszystkich procesow: " + str(timer) + " [s]\n")
    print("Czasy oczekiwania poszczegolnych procesow: ")
    print(wait)
    w.write("Czasy oczekiwania poszczegolnych procesow: {}\n".format(wait))
    suma1=0
    for i in range(len(wait)):
        suma1+=wait[i]
    print("Suma czasow oczekiwania: "+str(suma1)+" [s]")
    w.write("Suma czasow oczekiwania: "+str(suma1)+" [s]\n")
    print("sredni czas oczekiania FCFS to: "+str(suma1/p)+" [s]")
    w.write("sredni czas oczekiania FCFS to: "+str(suma1/p)+" [s]\n")
    f.close()