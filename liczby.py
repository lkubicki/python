def zamien_na_cyfry(liczba):
    cyfry = []
    while liczba > 0:
        cyfry.append(liczba % 10)
        liczba = int(liczba / 10)
    return cyfry

def zamien_na_napis(liczba):
    return str(liczba)

def zsumuj_cyfry(cyfry):
    suma = 0
    for i in range(len(cyfry)):
        suma += cyfry[i]
    return suma

def zsumuj_cyfry_napis(cyfry):
    suma = 0
    for cyfra in cyfry:
        suma += int(cyfra)
    return suma

def pomnoz_cyfry(cyfry):
    iloczyn = 1
    for i in range(len(cyfry)):
        iloczyn = iloczyn * cyfry[i]
    return iloczyn

def pomnoz_cyfry_napis(cyfry):
    iloczyn = 1
    for cyfra in cyfry:
        iloczyn = iloczyn * int(cyfra)
    return iloczyn

def ile(lista):
    licznik = 0
#    for i in range(len(lista)):
#        cyfry = zamien_na_cyfry(lista[i])
#        suma_cyfr = zsumuj_cyfry(cyfry)
#        iloczyn_cyfr = pomnoz_cyfry(cyfry)
#        if suma_cyfr == iloczyn_cyfr:
#            licznik = licznik + 1
#    return licznik
    for i in range(len(lista)):
        cyfry = zamien_na_napis(lista[i])
        suma_cyfr = zsumuj_cyfry_napis(cyfry)
        iloczyn_cyfr = pomnoz_cyfry_napis(cyfry)
        if suma_cyfr == iloczyn_cyfr:
            licznik = licznik + 1
    return licznik


print(ile([7, 13, 1122, 111, 52, 52111]))
print(ile([11, 1000, 123]))
print(ile([321, 152, 2141, 4211]))
