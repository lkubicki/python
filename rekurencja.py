import time
import random

liczby_do_posortowania = []
random.seed()
for i in range(0,10000):
    liczby_do_posortowania.append(random.randint(0,10000))

posortowane = False

def sortuj(liczby):
    if len(liczby) <= 1:
        return liczby
    liczba=liczby[0]
    mniejsze=[]
    wieksze = []
    for i in range(1, len(liczby)):
        if liczby[i] < liczba:
            mniejsze.append(liczby[i])
        else:
            wieksze.append(liczby[i])    
    wynik=[]
    wynik.extend(sortuj(mniejsze))
    wynik.append(liczba)
    wynik.extend(sortuj(wieksze))
    return wynik


poczatek = time.time()
sortuj(liczby_do_posortowania)
koniec = time.time()

print(str(koniec-poczatek))
