def przygotuj_klucz(klucz, dlugosc):
    wynik = ''
    for i in range(dlugosc):
        wynik += klucz[i%len(klucz)]
    return wynik

def deszyfr(szyfrogram, klucz):
    dlugi_klucz = przygotuj_klucz(klucz, len(szyfrogram))
    wynik = ''
    for i in range(len(szyfrogram)):
        przesuniecie = (ord(szyfrogram[i]) + 26 - ord(dlugi_klucz[i])) % 26
        wynik += chr(ord('A') + przesuniecie)
    return wynik

print(deszyfr('CGSMURRBO', 'KRET'))
