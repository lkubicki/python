def przygotuj_przystanki(liczba_przystankow):
    przystanki = []
    for i in range(liczba_przystankow):
        przystanki.append(chr(ord('A') + i))
    return przystanki


def podaj_zakres_przystankow(przystanki):
    pierwszy = 0
    ostatni = len(przystanki)-1
    for i in range(len(przystanki)):
        if przystanki[pierwszy] == '_':
            pierwszy = pierwszy + 1
        if przystanki[i] != '_':
            ostatni = i
    return pierwszy, ostatni


def okresl_kierunek_ruchu(do_konca, aktualny_przystanek, liczba_przystankow, przystanki):
    pierwszy, ostatni = podaj_zakres_przystankow(przystanki)
    if aktualny_przystanek >= ostatni:
        return False
    elif aktualny_przystanek <= pierwszy:
        return True
    return do_konca


def podaj_aktualna_pozycje(do_konca, aktualny_przystanek):
    if do_konca:
        return aktualny_przystanek + 1
    return aktualny_przystanek - 1
    

def oblicz_trase(przystanki, liczba_przystankow, co_ktory_postoj):
    trasa = ''
    do_konca = True
    aktualny_przystanek = 0
    od_ostatniego_zatrzymania = 1
    
    while len(trasa) != liczba_przystankow:
        do_konca = okresl_kierunek_ruchu(do_konca, aktualny_przystanek, liczba_przystankow, przystanki)
        aktualny_przystanek = podaj_aktualna_pozycje(do_konca, aktualny_przystanek)
        if przystanki[aktualny_przystanek] != '_':
            od_ostatniego_zatrzymania = od_ostatniego_zatrzymania + 1
            print(str(od_ostatniego_zatrzymania) + ' ' + przystanki[aktualny_przystanek])
        if od_ostatniego_zatrzymania == co_ktory_postoj:
            od_ostatniego_zatrzymania = 0
            trasa = trasa + przystanki[aktualny_przystanek]
            przystanki[aktualny_przystanek] = '_'
        
    return trasa      

def tram(liczba_przystankow, co_ktory_postoj):
    przystanki = przygotuj_przystanki(liczba_przystankow)
    return oblicz_trase(przystanki, liczba_przystankow, co_ktory_postoj)


print(tram(6,5))
