from turtle import *

kolory=['yellow','green']

def przejdz_do_kolejnego(bok):
    pu()
    fd(bok)
    pd()

def przejdz_do_kolejnej_kolumny(bok, liczba_kwadratow_kolumny):
    pu()
    rt(90)
    fd(bok)
    rt(90)
    fd(bok*liczba_kwadratow_kolumny)
    rt(180)
    pd()

def ustaw_na_poczatek_obrazka(bok, szerokosc, wysokosc):
    pu()
    bk(bok * szerokosc / 2)
    lt(90)
    bk(bok * wysokosc / 2)
    pd()

def rysuj_kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

def przygotuj_definicje_wiez(definicja):
    wieze = []
    poprzednia = definicja[0]
    licznik = 0
    najwyzsza = 0
    for litera in definicja:
        if litera != poprzednia:
            if najwyzsza < licznik:
                najwyzsza = licznik
            wieze.append(licznik)
            licznik = 1
        else:
            licznik += 1
        poprzednia = litera
    if najwyzsza < licznik:
        najwyzsza = licznik
    wieze.append(licznik)
    return wieze, najwyzsza

def wie(definicja):
    wieze, najwyzsza = przygotuj_definicje_wiez(definicja)
    liczba_kwadratow = najwyzsza
    if liczba_kwadratow < len(wieze):
        liczba_kwadratow = len(wieze)
    bok = int(400/liczba_kwadratow)
    ustaw_na_poczatek_obrazka(bok, len(wieze), najwyzsza)
        
    nr_koloru = 0 
    if definicja[0] == 'G':
        nr_koloru = 1
    for wysokosc in wieze:
        kolor_wiezy = kolory[nr_koloru%2]
        for i in range(wysokosc):
            rysuj_kwadrat(bok, kolor_wiezy)
            przejdz_do_kolejnego(bok)
        przejdz_do_kolejnej_kolumny(bok, wysokosc)
        nr_koloru+=1
    
tracer(False)
#wie('GGGYGGGYYYYYYYYGGGGGGYGGYGYYGGGGGGYGGGYYGGGGGGGGGYYG')
wie('GGYYYYYYYYYYYYYYYYYYYYYYY')
update()
