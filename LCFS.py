import numpy as np

def lcfs_planning(tab1,p,w):
    # Algorytm LCFS
    print("*************** Algorytm LCFS ***************")
    print(tab1)
    print("*********************************************")

    # funkcja szukająca minimum w czasie naedjścia i zwraca jej indeks
    def maksimum(tab, timer):
        max1 = -1
        max2 = 0
        dl = tab.size
        for i in range(dl):
            if (tab[i][0] <= timer):  # sprawdza czy minimum jest zgodne z taktem
                if (tab[i][0] > max1):
                    max1 = tab[i][0]
                    max2 = i

        if (tab[max2][0] <= timer):
            return max2
        else:
            return -1
    f = open("Wynik_LCFS.txt",'w')
    timer = 0  # kolejne takty procesora [s]
    a = 1  # zmienna, ktora ustala czy proces sie wykonuje i jak dlugo
    wait = []  # tablica czasow oczekiwania procesow
    while True:
        if (a == 1):  # znalezienie aktualnego max zgodnego z taktem
            o = maksimum(tab1, timer)

        if (o == -1):
            print("procesor nie pracuje | czas: " + str(timer))
            f.write("procesor nie pracuje | czas: " + str(timer) + "\n")
        else:
            print("proces: " + str(tab1[o]) + " | czas: " + str(timer))
            f.write("proces: " + str(tab1[o]) + " | czas: " + str(timer) + "\n")
        if (o != -1):
            if (a < tab1[o][1]):
                a += 1
            elif (a == tab1[o][1]):
                a = 1
                sum = 0
                sum = timer - tab1[o][1] + 1 - tab1[o][0]
                wait.append(int(sum))  # zapis czasu oczekiwania
                tab1 = np.delete(tab1, o)  # usuwa proces z tablicy

        if (tab1.size == 0):  # przerwanie petli
            break
        timer += 1  # zwiekszanie taktu

    w.write("*****LCFS******\n")

    # dane i statystyki
    print("Czas potrzebny na wykonanie wszystkich procesow: " + str(timer) + " [s]")
    w.write("Czas potrzebny na wykonanie wszystkich procesow: " + str(timer) + " [s]\n")
    print("Czasy oczekiwania poszczegolnych procesow: ")
    print(wait)
    w.write("Czasy oczekiwania poszczegolnych procesow: {}\n".format(wait))
    suma2 = 0
    for i in range(len(wait)):
        suma2 += wait[i]
    print("Suma czasow oczekiwania: " + str(suma2) + " [s]")
    w.write("Suma czasow oczekiwania: "+str(suma2)+" [s]\n")
    print("sredni czas oczekiania LCFS to: " + str(suma2 / p) + " [s]")
    w.write("sredni czas oczekiania FCFS to: "+str(suma2 / p)+" [s]\n")
    f.close()