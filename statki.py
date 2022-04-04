from time import *
from requests import *

START_URL = "http://3am.pl/ships/start.php"
SEND_SHOOT_URL = "http://3am.pl/ships/shoot.php"
SEND_RESULT_URL = "http://3am.pl/ships/shootresult.php"
GET_LAST_ACTION_URL = "http://3am.pl/ships/ships.php"

FAIL = 'FAIL'

PUDLO = 'O'
TRAFIONY = 'X'
PLONIE = '@'
DZIURA = '*'

STATKI = 0
STRZALY = 1

POZIOMO = 0
PIONOWO = 1

nazwa = ''
identyfikator_gry = 0
czyja_kolej = 0

plansza = []
statki = [[4, 'jednomasztowiec', 'jednomasztowca'],
          [3, 'dwumasztowiec', 'dwumasztowca'],
          [2, 'trzymasztowiec', 'trzymasztowca'],
          [1, 'czteromasztowiec', 'czteromasztowca']]
gracze = ['host', 'guest']


def przygotuj_plansze():
    for i in range(10):
        wiersz = []
        for j in range(10):
            wiersz.append([' ', ' '])
        plansza.append(wiersz)


def podaj_pozycje(pozycja):
    if czy_prawidlowe_koordynaty(pozycja):
        return ord(pozycja[0]) - ord('A'), int(pozycja[1])
    else:
        return -1, -1


def podaj_zawartosc_planszy(wiersz, kolumna, ktora_plansza):
    if 0 <= wiersz <= 9 and 0 <= kolumna <= 9:
        return plansza[wiersz][kolumna][ktora_plansza]
    return '!'


def ustaw_zawartosc_planszy(wiersz, kolumna, ktora_plansza, wartosc, czy_nadpisac=False):
    if 0 <= wiersz <= 9 and 0 <= kolumna <= 9 \
            and (plansza[wiersz][kolumna][ktora_plansza] == ' ' or czy_nadpisac):
        plansza[wiersz][kolumna][ktora_plansza] = wartosc


def czy_prawidlowe_koordynaty(pozycja):
    if len(pozycja) != 2:
        return False
    if pozycja[0] not in 'ABCDEFGHIJ':
        return False
    if pozycja[1] not in '1234567890':
        return False
    return True


def czy_prawidlowa_pozycja_statku_pionowo(wiersz, kolumna, liczba_masztow):
    if wiersz > 0:
        for i in range(-1, 2, 1):
            if podaj_zawartosc_planszy(wiersz - 1, kolumna + i, STATKI) not in ' !':
                return False
            if podaj_zawartosc_planszy(wiersz + liczba_masztow, kolumna + i, STATKI) not in ' !':
                return False
    for i in range(liczba_masztow):
        if podaj_zawartosc_planszy(wiersz + i, kolumna, STATKI) != ' ':
            return False
        if podaj_zawartosc_planszy(wiersz + i, kolumna - 1, STATKI) not in ' !':
            return False
        if podaj_zawartosc_planszy(wiersz + i, kolumna + 1, STATKI) not in ' !':
            return False
    return True


def czy_prawidlowa_pozycja_statku_poziomo(wiersz, kolumna, liczba_masztow):
    for i in range(-1, 2, 1):
        if podaj_zawartosc_planszy(wiersz + i, kolumna - 1, STATKI) not in ' !':
            return False
        if podaj_zawartosc_planszy(wiersz + i, kolumna + liczba_masztow, STATKI) not in ' !':
            return False
    for j in range(liczba_masztow):
        if podaj_zawartosc_planszy(wiersz, kolumna + j, STATKI) != ' ':
            return False
        if podaj_zawartosc_planszy(wiersz + 1, kolumna + j, STATKI) not in ' !':
            return False
        if podaj_zawartosc_planszy(wiersz - 1, kolumna + j, STATKI) not in ' !':
            return False
    return True


def czy_prawidlowa_pozycja_statku(liczba_masztow, koordynaty):
    wiersz, kolumna = podaj_pozycje(koordynaty[:2])
    if wiersz < 0 or kolumna < 0:
        return False
    kierunek = ' '
    if liczba_masztow > 1:
        if len(koordynaty) == 3 and koordynaty[2] in 'PO':
            kierunek = koordynaty[2]
        else:
            return False
    if kierunek in 'P ' and wiersz + liczba_masztow - 1 <= 9:
        return czy_prawidlowa_pozycja_statku_pionowo(wiersz, kolumna, liczba_masztow)
    elif kierunek in 'O' and kolumna + liczba_masztow - 1 <= 9:
        return czy_prawidlowa_pozycja_statku_poziomo(wiersz, kolumna, liczba_masztow)
    else:
        return False
    return True


def ustaw_statek(liczba_masztow, koordynaty):
    if not czy_prawidlowa_pozycja_statku(liczba_masztow, koordynaty):
        return False
    wiersz, kolumna = podaj_pozycje(koordynaty[:2])
    kierunek = ' '
    if liczba_masztow > 1:
        kierunek = koordynaty[2]
    if kierunek in 'P ':
        for i in range(liczba_masztow):
            ustaw_zawartosc_planszy(wiersz + i, kolumna, STATKI, chr(100 + liczba_masztow * 10 + i))
    else:
        for i in range(liczba_masztow):
            ustaw_zawartosc_planszy(wiersz, kolumna + i, STATKI, chr(liczba_masztow * 10 + i))
    return True


def wyswietl_plansze():
    wiersz = '  '
    for j in range(2):
        for i in range(10):
            wiersz += str(i) + ' '
        wiersz += '      '
    print(wiersz)

    for y in range(10):
        wiersz = ''
        for plansza in range(2):
            wiersz += chr(ord('A') + y) + ' '
            for x in range(10):
                zawartosc = podaj_zawartosc_planszy(y, x, plansza)
                if zawartosc not in ' ' + TRAFIONY + PUDLO + DZIURA + PLONIE:
                    wiersz += '#'
                else:
                    wiersz += zawartosc
                wiersz += '|'
            wiersz += '    '
        print(wiersz)
        wiersz = ''


def ustaw_statki():
    for i in range(4):
        rozmiar = i + 1
        for j in range(statki[i][0]):
            if i > 0:
                print('Podaj pozycje (punkt początkowy i [p]ionowo/p[o]ziomo) ' + statki[i][2] + ': ')
            else:
                print('Podaj pozycje (punkt początkowy) ' + statki[i][2] + ': ')
            pozycja = str(input()).upper()
            while not ustaw_statek(rozmiar, pozycja):
                print('Nieprawidlowe koordynaty: ' + pozycja + '. Podaj pozycje ' + statki[i][2] + ': ')
                pozycja = str(input()).upper()


def czy_prawidlowy_strzal(strzal):
    if not czy_prawidlowe_koordynaty(strzal):
        return False
    wiersz, kolumna = podaj_pozycje(strzal)
    return podaj_zawartosc_planszy(wiersz, kolumna, STRZALY) != ''


def czy_trafiony(koordynaty):
    wiersz, kolumna = podaj_pozycje(koordynaty)
    return podaj_zawartosc_planszy(wiersz, kolumna, STATKI) not in ' ' + PUDLO + TRAFIONY + DZIURA + PLONIE


def czy_zatopiony(koordynaty, dane_statku):
    wiersz, kolumna = podaj_pozycje(koordynaty)
    aktualny_maszt = dane_statku % 10
    if dane_statku > 100:
        liczba_masztow = (dane_statku - 100) // 10
        poczatek = wiersz - aktualny_maszt
        for i in range(liczba_masztow):
            if podaj_zawartosc_planszy(poczatek + i, kolumna, STATKI) != PLONIE:
                return False
    else:
        liczba_masztow = dane_statku // 10
        poczatek = kolumna - aktualny_maszt
        for i in range(liczba_masztow):
            if podaj_zawartosc_planszy(wiersz, poczatek + i, STATKI) != PLONIE:
                return False
    return True


def podaj_polozenie_statku(koordynaty, dane_statku):
    wiersz, kolumna = podaj_pozycje(koordynaty)
    aktualny_maszt = dane_statku % 10
    if dane_statku > 100:
        liczba_masztow = (dane_statku - 100) // 10
        poczatkowy_wiersz = wiersz - aktualny_maszt
        koncowy_wiersz = poczatkowy_wiersz + liczba_masztow
        return chr(ord('A') + poczatkowy_wiersz) + str(kolumna) + '-' + chr(ord('A') + koncowy_wiersz) + str(kolumna)
    else:
        liczba_masztow = dane_statku // 10
        poczatkowa_kolumna = kolumna - aktualny_maszt
        koncowa_kolumna = poczatkowa_kolumna + liczba_masztow
        return wiersz + str(poczatkowa_kolumna) + '-' + wiersz + str(koncowa_kolumna)


def oznacz_jako_zatopiony(koordynaty, dane_statku):
    print(f'ZATOPIONY {koordynaty}')
    wiersz, kolumna = podaj_pozycje(koordynaty)
    aktualny_maszt = dane_statku % 10
    if dane_statku > 100:
        liczba_masztow = (dane_statku - 100) // 10
        poczatek = wiersz - aktualny_maszt
        for i in range(poczatek - 1, poczatek + liczba_masztow + 1):
            for j in range(-1, 2):
                ustaw_zawartosc_planszy(i, kolumna + j, STATKI, DZIURA)
    else:
        liczba_masztow = dane_statku // 10
        poczatek = kolumna - aktualny_maszt
        for i in range(poczatek - 1, poczatek + liczba_masztow + 1):
            for j in range(-1, 2):
                ustaw_zawartosc_planszy(wiersz + j, i, STATKI, DZIURA)


def sprawdz_strzal(koordynaty):
    # while czy_prawidlowy_strzal(koordynaty):
    #     print('Nieprawidlowy strzal. Sprobuj jeszcze raz: ')
    wiersz, kolumna = podaj_pozycje(koordynaty)
    if czy_trafiony(koordynaty):
        dane_statku = ord(podaj_zawartosc_planszy(wiersz, kolumna, STATKI))
        print(f'TRAFIONY {dane_statku}')
        ustaw_zawartosc_planszy(wiersz, kolumna, STRZALY, PLONIE, True)
        ustaw_zawartosc_planszy(wiersz, kolumna, STATKI, PLONIE, True)
        if czy_zatopiony(koordynaty, dane_statku):
            oznacz_jako_zatopiony(koordynaty, dane_statku)
            return 'SUNK', podaj_polozenie_statku(koordynaty, dane_statku)
        return 'HIT', koordynaty
    else:
        ustaw_zawartosc_planszy(wiersz, kolumna, STRZALY, PUDLO)
        ustaw_zawartosc_planszy(wiersz, kolumna, STATKI, PUDLO)
        print(f'{int(time_ns() / 100)} PUDLO')
        return 'MISS', koordynaty
    # return podaj_zawartosc_planszy(wiersz, kolumna, STRZALY)


def oznacz_strzal(koordynaty, rezultat):
    wiersz, kolumna = podaj_pozycje(koordynaty)
    if rezultat == 'HIT':
        print(f'{koordynaty} TRAFIONY')
        ustaw_zawartosc_planszy(wiersz, kolumna, STRZALY, PLONIE, True)
    elif rezultat == 'SUNK':
        print(f'{koordynaty} ZATOPIONY')
        #todo: oznaczyc na planszy po koordynatach, gdzie zatopiono statek (oraz pola dookoła)
        ustaw_zawartosc_planszy(wiersz, kolumna, STRZALY, PLONIE, True)
    else:
        ustaw_zawartosc_planszy(wiersz, kolumna, STRZALY, PUDLO)
        print(f'{koordynaty} PUDLO')
    return podaj_zawartosc_planszy(wiersz, kolumna, STRZALY)


def nowa_gra():
    global identyfikator_gry
    global nazwa
    global czyja_kolej
    identyfikator_gry = int(time_ns() / 100)
    nazwa = gracze[0]
    czyja_kolej = 1
    odpowiedz = post(START_URL, data={'gameId': str(identyfikator_gry)})
    if odpowiedz.text == 'OK':
        print(f'{int(time_ns() / 100)} - identyfikator gry: {str(identyfikator_gry)}')


def dolacz(idgry):
    global identyfikator_gry
    global nazwa
    global czyja_kolej
    nazwa = gracze[1]
    czyja_kolej = 0
    odpowiedz = FAIL
    while odpowiedz == FAIL:
        odpowiedz = get(GET_LAST_ACTION_URL, params={'gameId': idgry}).text
        if odpowiedz == 'FAIL':
            print(f'{int(time_ns() / 100)} - nie dołączono do gry: {idgry}, odpowiedź: {odpowiedz}')
            sleep(3)
    identyfikator_gry = idgry
    print(f'{int(time_ns() / 100)} - dołączono do gry: {identyfikator_gry}')


def oddaj_strzal():
    global identyfikator_gry
    global nazwa
    koordynaty = ""
    while koordynaty == "" or not czy_prawidlowy_strzal(koordynaty):
        koordynaty = input("koordynaty pola: ").upper()
    strzel(koordynaty, nazwa)


def strzel(koordynaty, nazwa_gracza):
    global identyfikator_gry
    post(SEND_SHOOT_URL, data={'gameId': identyfikator_gry, 'player': nazwa_gracza, 'target': koordynaty})


def pobierz_dane():
    global identyfikator_gry
    dane = ''
    nazwa_gracza = nazwa
    akcja = ''
    while nazwa_gracza == nazwa:
        odpowiedz = get(GET_LAST_ACTION_URL, params={'gameId': identyfikator_gry})
        if odpowiedz.text != '':
            czas, akcja, nazwa_gracza, dane = odpowiedz.text.split(',')
        sleep(3)
    return akcja, dane


def wyslij_odpowiedz(akcja, koordynaty):
    global identyfikator_gry
    global nazwa_gracza
    post(SEND_RESULT_URL, data={'gameId': identyfikator_gry, 'player': nazwa_gracza, 'result': akcja, 'corrdinates': koordynaty})


def gra():
    global czyja_kolej
    while True:
        if gracze[czyja_kolej] == nazwa:
            oddaj_strzal()
            akcja, dane = pobierz_dane()
            oznacz_strzal(dane, akcja)
            czyja_kolej = (czyja_kolej + 1) % 2
        else:
            akcja, dane = pobierz_dane()
            oznacz_strzal(dane, akcja)
            akcja, koordynaty = sprawdz_strzal(dane)
            wyslij_odpowiedz(akcja, koordynaty)
            czyja_kolej = (czyja_kolej + 1) % 2


def start_gry():
    global nazwa
    global identyfikator_gry
    nazwa = ''
    wybor = '.'
    while wybor not in "wd":
        wybor = input("[w]ystartować nową grę, czy [d]ołączyć do istniejącej? ")
    if wybor == 'w':
        nowa_gra()
    else:
        idgry = input("podaj identyfikator gry: ")
        dolacz(idgry)
    if identyfikator_gry != 0:
        gra()
    else:
        print(f'{int(time_ns() / 100)} - nie udało się uruchomić nowej lub dołączyć do istniejącej gry')


przygotuj_plansze()
start_gry()

# nowa_gra()
# strzel('A1', 'host')
# pobierz_dane()
# dolacz(identyfikator_gry)
# oddaj_strzal()
# pobierz_dane()
