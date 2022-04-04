from math import *

def srednia_arytmetyczna(liczby):
    return sum(liczby) / len(liczby)

def podaj_dzielniki_wlasciwe(liczba):
    dzielniki = [1]
    dzielniki_suma = 0
    for i in range(2, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki

def czy_jest_liczba_janka(liczba):
    dzielniki = podaj_dzielniki_wlasciwe(liczba)
    print(f'{liczba}  -  {dzielniki}  -  {sqrt(liczba)}  >=  {srednia_arytmetyczna(dzielniki)}')
    return len(dzielniki) > 1 and srednia_arytmetyczna(dzielniki) <= sqrt(liczba)
    
def liczby_janka(liczba):
    liczby = []
    while len(liczby) < 5:
        liczba += 1
        if czy_jest_liczba_janka(liczba):
            liczby.append(liczba)
    return liczby
            

print(liczby_janka(8))
