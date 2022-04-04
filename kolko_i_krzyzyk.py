plansza = [['1','2','3'],['4','5','6'],['7','8','9']]
symbole_graczy=['X','O']
gracz= 0
wygrana='-'
jest_ruch=True

def rysuj_plansze():
    for wiersz in range(0,3):
        print(f'{plansza[wiersz][0]} | {plansza[wiersz][1]} | {plansza[wiersz][2]}')
        print('--+---+---')

def ustaw_znak_w_polu(pole):
    for wiersz in range(0,3):
        for kolumna in range (0,3):
            if plansza[wiersz][kolumna] == pole:
                plansza[wiersz][kolumna] = symbole_graczy[gracz]
                return True
    print('Nieprawidłowe pole')
    return False
            
def wybierz_pole():
    ustawiono = False
    while not ustawiono:
        pole = input(f'Gdzie chcesz postawić {symbole_graczy[gracz]}: ')
        ustawiono = ustaw_znak_w_polu(pole)

def sprawdz_czy_jest_ruch():
    for wiersz in range(0,3):
        for kolumna in range (0,3):
            if plansza[wiersz][kolumna] != symbole_graczy[0] and plansza[wiersz][kolumna] != symbole_graczy[1]:
                return True
    return False

def sprawdz_czy_wygrana():
    if plansza[0][0]==plansza[0][1]==plansza[0][2]:
        return plansza[0][0]
    if plansza[1][0]==plansza[1][1]==plansza[1][2]:
        return plansza[1][0]
    if plansza[2][0]==plansza[2][1]==plansza[2][2]:
        return plansza[2][0]
    if plansza[0][0]==plansza[1][0]==plansza[2][0]:
        return plansza[0][0]
    if plansza[0][1]==plansza[1][1]==plansza[2][1]:
        return plansza[0][1]
    if plansza[0][2]==plansza[1][2]==plansza[2][2]:
        return plansza[0][2]
    if plansza[0][0]==plansza[1][1]==plansza[2][2]:
        return plansza[0][0]
    if plansza[2][0]==plansza[1][1]==plansza[0][2]:
        return plansza[2][0]
    return '-'

def sprawdz_czy_wygrana2():
    wygrane_ruchy=[[(0,0), (0,1),(0,2)],
                   [(1,0), (1,1),(1,2)],
                   [(2,0), (2,1),(2,2)],
                   [(0,0), (1,0),(2,0)],
                   [(0,1), (1,1),(2,1)],
                   [(0,2), (1,2),(2,2)],
                   [(0,0), (1,1),(2,2)],
                   [(0,2), (1,1),(2,0)]]
    for okno in range(0, len(wygrane_ruchy)):
        if plansza[wygrane_ruchy[okno][0].first][wygrane_ruchy[okno][0].second]==plansza[wygrane_ruchy[okno][1].first][wygrane_ruchy[okno][1].second]==plansza[wygrane_ruchy[okno][2].first][wygrane_ruchy[okno][2].second]:
            return plansza[wygrane_ruchy[okno][0].first][wygrane_ruchy[okno][0].second]
    return '-'    


def ustaw_grajacego():
    return (gracz + 1) % 2


while jest_ruch and wygrana=='-' : 
    rysuj_plansze()
    wybierz_pole()
    wygrana=sprawdz_czy_wygrana()
    jest_ruch = sprawdz_czy_jest_ruch()
    gracz = ustaw_grajacego()
if wygrana == '-':
    print('Remis')
else:
    print(f'Wygrał {wygrana}')
rysuj_plansze()
