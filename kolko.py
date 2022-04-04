import random


plansza = [[1,2,3],[4,5,6],[7,8,9]]
gracze = ['O', 'X']
wygrany = '_'
random.seed()


def rysuj_plansze():
    print()
    for i in range(3):
        print(f'{plansza[i][0]}|{plansza[i][1]}|{plansza[i][2]}')
        if i < 2:
            print('-+-+-')


def losuj_zaczynajacego():
    return random.randint(0,1)


def oblicz_wspolrzedne(wybrane_pole):
    return int(wybrane_pole / 3), wybrane_pole % 3


def sprawdz_zajetosc_pola(x, y):
    return plansza[x][y] in ('O', 'X')


def wykonaj_ruch(gracz):
    ruch_wykonany = False
    while not ruch_wykonany:
        wybrane_pole = int(input(f'{gracze[gracz]} wybiera: '))
        if wybrane_pole < 1 or wybrane_pole > 9:
            print('zly zakres')
        else:
            x, y = oblicz_wspolrzedne(wybrane_pole -1)
            zajete = sprawdz_zajetosc_pola(x, y)
            if not zajete:
                plansza[x][y] = gracze[gracz]
                ruch_wykonany = True


def kolejny_gracz(aktualny_gracz):
    return (aktualny_gracz + 1) % 2


#def sprawdz_czy_wygrany(gracz):
#    if plansza[0][0] == plansza[1][0] == plansza[2][0] == gracze[gracz]:
#        return True
#    elif plansza[0][1] == plansza[1][1] == plansza[2][1] == gracze[gracz]:
#        return True
#    elif plansza[0][2] == plansza[1][2] == plansza[2][2] == gracze[gracz]:
#        return True
#    elif plansza[0][0] == plansza[0][1] == plansza[0][2] == gracze[gracz]:
#        return True
#    elif plansza[1][0] == plansza[1][1] == plansza[1][2] == gracze[gracz]:
#        return True
#    elif plansza[2][0] == plansza[2][1] == plansza[2][2] == gracze[gracz]:
#        return True
#    elif plansza[0][0] == plansza[1][1] == plansza[2][2] == gracze[gracz]:
#        return True
#    elif plansza[2][0] == plansza[1][1] == plansza[0][2] == gracze[gracz]:
#        return True
#    else:
#        return False


def sprawdz_czy_wygrany(gracz):
    wygrane_ruchy=[[(0,0), (0,1),(0,2)],
                   [(1,0), (1,1),(1,2)],
                   [(2,0), (2,1),(2,2)],
                   [(0,0), (1,0),(2,0)],
                   [(0,1), (1,1),(2,1)],
                   [(0,2), (1,2),(2,2)],
                   [(0,0), (1,1),(2,2)],
                   [(0,2), (1,1),(2,0)]]
    for okno in range(0, len(wygrane_ruchy)):
        x1,y1 = wygrane_ruchy[okno][0]
        x2,y2 = wygrane_ruchy[okno][1]
        x3,y3 = wygrane_ruchy[okno][2]
        if plansza[x1][y1] == plansza[x2][y2] == plansza[x3][y3]:
            return True
    return False    


def wypelniona_cala_plansza():
    for i in range(3):
        for j in range(3):
            if plansza[i][j] not in ('O', 'X'):
                return False
    return True
    


gracz = losuj_zaczynajacego()
while not wygrany in ('O', 'X', 'REMIS'):
    rysuj_plansze()
    wykonaj_ruch(gracz)    
    if not sprawdz_czy_wygrany(gracz):
        if wypelniona_cala_plansza():
            wygrany = 'REMIS'
        else:
            gracz = kolejny_gracz(gracz)
    else:
        wygrany = gracze[gracz]
rysuj_plansze()
print(f'Wygrywa: {wygrany}')
