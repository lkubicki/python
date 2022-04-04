def ustal_kolejnosc_kolumn(klucz):
    kolejnosc = []
    litery = list(klucz)
    litery.sort()
    
    for i in range(len(klucz)):
        zamiana = False
        pozycja = 0
        while not zamiana and pozycja < len(klucz):
            if klucz[i] == litery[pozycja] and not zamiana:
                kolejnosc.append(pozycja)
                litery[pozycja] = '_'
                zamiana = True
            pozycja+=1
    return kolejnosc

def wpisz_w_tabele(tekst, klucz):
    tabela = []
    tymczasowe = []
    for i in range(len(tekst)):
        tymczasowe.append(tekst[i])
        if (i + 1) % len(klucz) == 0:
            tabela.append(tymczasowe)
            tymczasowe = []
    tabela.append(tymczasowe)
    return tabela

def szyfr_kolumnowy(tekst, klucz):
    kolejnosc_kolumn = ustal_kolejnosc_kolumn(klucz)
    tabela = wpisz_w_tabele(tekst, klucz)
    wynik = ''
    liczba_wierszy = int(len(tekst)/len(klucz))
    dlugosc_ostatniej = len(tekst) % len(klucz) - 1

    for i in range(len(kolejnosc_kolumn)):
        lwierszy = liczba_wierszy
        if kolejnosc_kolumn[i] <= dlugosc_ostatniej:
            lwierszy += 1
        for j in range(lwierszy):
            wynik = wynik + tabela[j][kolejnosc_kolumn[i]]
    return wynik


print('jimtadsawocnao  <---')    
print(szyfr_kolumnowy('tajnawiadomosc', 'plot'))
