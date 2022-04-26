klawiatura = [['0', '+'],
              ['1', ' '],
              ['2', 'a', 'b', 'c'],
              ['3', 'd', 'e', 'f'],
              ['4', 'g', 'h', 'i'],
              ['5', 'j', 'k', 'l'],
              ['6', 'm', 'n', 'o'],
              ['7', 'p', 'q', 'r', 's'],
              ['8', 't', 'u', 'v'],
              ['9', 'w', 'x', 'y', 'z']]

def dekoduj_znak(co_naciskamy, ile_razy):
    if co_naciskamy in '#*':
        return co_naciskamy
    else:
        cyfra = int(co_naciskamy)
        liczba_znakow = len(klawiatura[cyfra])
        return klawiatura[cyfra][(ile_razy - 1) % liczba_znakow]


def wiadomosc_z_telefonu(zaszyfrowane):
    wynik = ''
    for sekwencja in zaszyfrowane.split(' '):
        co_naciskamy = sekwencja[0]
        ile_razy = 1
        if len(sekwencja) > 1:
            ile_razy = int(sekwencja[1])
        wynik += dekoduj_znak(co_naciskamy, ile_razy)
    return wynik

print(wiadomosc_z_telefonu("# 92 44 64 75 63 22 12 21 01 21 21"))
print(wiadomosc_z_telefonu("92 44 64 75 63 22"))
print(wiadomosc_z_telefonu("74 64 53 12 21 01 21 21"))
print(wiadomosc_z_telefonu("53 64 32 # 21 31 02 11 41 *"))