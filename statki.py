STATKI = 0
STRZALY = 1

POZIOMO = 0
PIONOWO = 1

plansza = []
statki = [[4, 'jednomasztowiec', 'jednomasztowca'],
          [3, 'dwumasztowiec', 'dwumasztowca'],
          [2, 'trzymasztowiec', 'trzymasztowca'],
          [1, 'czteromasztowiec', 'czteromasztowca']]


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


def podaj_zawartosc_planszy(ktora_plansza, kolumna, wiersz):
    return plansza[wiersz][kolumna][ktora_plansza]


def czy_prawidlowe_koordynaty(pozycja):
    if len(pozycja) != 2:
        return False
    if pozycja[0] not in 'ABCDEFGHIJ':
        return False
    if pozycja[1] not in '1234567890':
        return False
    return True


def czy_prawidlowy_strzal(strzal):
    if not czy_prawidlowe_koordynaty(strzal):
        return False
    x, y = podaj_pozycje(strzal)
    if podaj_zawartosc_planszy(x, y, STRZALY) != ' ':
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
        for i in range(liczba_masztow):
            if podaj_zawartosc_planszy(STATKI, kolumna, wiersz + i) != ' ':
                return False
    elif kierunek in 'O' and kolumna + liczba_masztow - 1 <= 9:
        for j in range(liczba_masztow):
            if podaj_zawartosc_planszy(STATKI, kolumna + j, wiersz) != ' ':
                return False
    else:
        return False
    return True


def ustaw_statek(liczba_masztow, koordynaty):
    wiersz, kolumna = podaj_pozycje(koordynaty[:2])
    kierunek = ' '
    if liczba_masztow > 1:
        kierunek = koordynaty[2]
    if kierunek in 'P ':
        for i in range(liczba_masztow):
            plansza[wiersz + i][kolumna][STATKI] = '#'
    else:
        for i in range(liczba_masztow):
            plansza[wiersz][kolumna + i][STATKI] = '#'


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
                wiersz += podaj_zawartosc_planszy(plansza, x, y)
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
            while not czy_prawidlowa_pozycja_statku(rozmiar, pozycja):
                print('Nieprawidlowe koordynaty: ' + pozycja + '. Podaj pozycje ' + statki[i][2] + ': ')
                pozycja = str(input()).upper()
            ustaw_statek(rozmiar, pozycja)


przygotuj_plansze()
# ustaw_statki()
print(czy_prawidlowa_pozycja_statku(4, 'J3P'))
ustaw_statek(4, 'J3P')
wyswietl_plansze()
