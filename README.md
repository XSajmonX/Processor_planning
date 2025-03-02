## Algorytmy planowania procesora:
Program generuje tablicę składającą się z procesów.
Każdy proces charakteryzuje się czasem nadejścia danego procesu oraz czasem potrzebnym na jego wykonanie przez procesor.
- Złożoność wykonywania procesu może być generowana losowo
- Złożoność wykonywania procesu może rosnąć z czasem
## Algorytm FCFS:
Algorytm wykonuje proces, który przyjdzie jako pierwszy. W 
implementacji tego algorytmu przejście jednego obiegu pętli oznacza 
jeden takt procesora. Na początku każdego obiegu wykonuję się funkcja 
wyszukująca proces o najmniejszym czasie przyjścia i zwraca jej indeks w 
tablicy procesów. Czas ten jest sprawdzany czy jest mniejszy równy 
obecnemu taktowi procesora. W przypadku nieznalezienia minimum 
zgodnego z obecnym taktem funkcja zwraca wartość -1 oznaczającą, że w 
tym takcie procesor nie pracuje.

## Algorytm LCFS:
Implementacja jest bardzo podobna w porównaniu do 
poprzedniego algorytmu z różnicą taką, że funkcja zwracająca indeks 
procesu nie szuka minimum zgodne z taktem procesora, lecz maksimum. 
Algorytm wykonuje ostatni proces, który przyszedł w danym takcie 
procesora. 
## Wyniki końcowe:
- Czas potrzebny na wykonanie wszystkich procesow [s]
- Czasy oczekiwania poszczegolnych procesow [s]
- Suma czasow oczekiwania [s]
- Średni czas oczekiania [s]