def przygotuj_liste_przystankow(ile_przystankow):
    przystanki = []
    for i in range(ile_przystankow):
        przystanki.append(chr(ord('A') + i))
    return przystanki


def okresl_kierunek_ruchu(aktualny, poczatek, koniec, w_przod):
    if aktualny >= koniec:
        return False
    elif aktualny <= poczatek:
        return True
    return w_przod


def podaj_zakres_trasy(przystanki, trasa):
    pierwszy = 0
    ostatni = 0
    for i in range(len(przystanki)):
        if przystanki[pierwszy] in trasa:
            pierwszy = pierwszy + 1
        if przystanki[i] not in trasa:
            ostatni = i
    return pierwszy, ostatni
    

def tram(ile_przystankow, co_ktory_stop):
    aktualny_przystanek = 0
    trasa = ''
    poczatek = 0
    koniec = ile_przystankow - 1
    do_przodu = True
    przystanki = przygotuj_liste_przystankow(ile_przystankow)
    liczba_odwiedzonych = 1
    
    while len(trasa) != ile_przystankow:
        poczatek, koniec = podaj_zakres_trasy(przystanki, trasa)
        do_przodu = okresl_kierunek_ruchu(aktualny_przystanek, poczatek, koniec, do_przodu)
        if do_przodu:
            aktualny_przystanek = aktualny_przystanek + 1
        else:
            aktualny_przystanek = aktualny_przystanek - 1
        if przystanki[aktualny_przystanek] not in trasa:
            liczba_odwiedzonych = liczba_odwiedzonych + 1
        if liczba_odwiedzonych == co_ktory_stop:
            trasa = trasa + przystanki[aktualny_przystanek]
            liczba_odwiedzonych = 0

    return trasa


print(tram(6,5))
