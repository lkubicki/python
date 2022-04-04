rok_przestepny=[0,31,29,31,30,31,30,31,31,30,31,30,31,0]
rok_nieprzestepny=[0,31,28,31,30,31,30,31,31,30,31,30,31,0]

def czy_rok_przestepny(rok):
    return rok % 4 == 0 and (rok %100 != 0 or rok % 400 == 0)


def podaj_dzien_miesiac_rok(napis):
    dzien = int(napis[1:3])
    miesiac = int(napis[3:5])
    rok = int(napis[5:])
    return dzien, miesiac, rok


def podaj_dni_do_konca_roku(dzien, miesiac, czy_przestepny):
    do_konca_roku = 0
    if czy_przestepny:
        do_konca_roku = rok_przestepny[miesiac] - dzien
    else:
        do_konca_roku = rok_nieprzestepny[miesiac] - dzien
    for i in range(miesiac + 1, 13):
        if czy_przestepny:
            do_konca_roku += rok_przestepny[i]
        else:
            do_konca_roku += rok_nieprzestepny[i]
    return do_konca_roku


def podaj_date(czy_przestepny, liczba_dni):
    miesiac = 0
    dni_w_miesiacu = 0
    while liczba_dni >= dni_w_miesiacu:
        if czy_przestepny:
            liczba_dni -= rok_przestepny[miesiac]
            dni_w_miesiacu = rok_przestepny[miesiac + 1]
        else:
            liczba_dni -= rok_nieprzestepny[miesiac]
            dni_w_miesiacu = rok_nieprzestepny[miesiac + 1]
        miesiac += 1
    return liczba_dni, miesiac


def zamien_na_tekst(wartosc):
    if wartosc < 10:
        return '0' + str(wartosc)
    else:
        return str(wartosc)


def urodziny(data, ktory_tysiac):
    liczba_dni = ktory_tysiac * 1000
    dzien, miesiac, rok = podaj_dzien_miesiac_rok(data)
    dni_do_konca_roku = podaj_dni_do_konca_roku(dzien, miesiac, czy_rok_przestepny(rok))
    liczba_dni -= dni_do_konca_roku
    rok += 1
    while (czy_rok_przestepny(rok) and liczba_dni >= 366) or (not czy_rok_przestepny(rok) and liczba_dni >= 365):
        if czy_rok_przestepny(rok):
            liczba_dni -= 366
        else:
            liczba_dni -= 365
        rok += 1
    dzien_k, miesiac_k = podaj_date(czy_rok_przestepny(rok), liczba_dni)
    dzien_slownie = zamien_na_tekst(dzien_k)
    miesiac_slownie = zamien_na_tekst(miesiac_k)
    return 'u'+dzien_slownie+miesiac_slownie+str(rok)


print(urodziny('u13022004', 2))
print(urodziny('u15011905', 10))
print(urodziny("u06042093", 1))
