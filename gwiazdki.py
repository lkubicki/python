from turtle import *
from math import *

kolory = ["olivedrab","olivedrab","tomato","tomato"]

def gwiazdka(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(6):
        fd(bok)
        rt(60)
        fd(bok)
        lt(120)
    end_fill()

def pusta_gwiazdka(bok, wysokosc, kolor):
    gwiazdka(bok, kolor)
    przesun_do_mniejszego(wysokosc)
    gwiazdka(bok/2, "white")
    wroc_z_mniejszego(wysokosc)
    

def przesun_do_mniejszego(wysokosc):
    pu()
    lt(30)
    fd(wysokosc)
    rt(30)
    pd()
    

def wroc_z_mniejszego(wysokosc):
    pu()
    lt(30)
    bk(wysokosc)
    rt(30)
    pd()
    

def przesun_do_nastepnej(bok):
    pu()
    fd(3*bok)
    pd()

def oblicz_wysokosc(bok):
    return int(sqrt((bok*bok) - ((bok/2)*(bok/2))))

def ustaw_na_poczatek(bok):
    pu()
    lt(90)
    fd(bok)
    rt(90)
    bk(280)
    pd()

def przesun_do_nowej_linii(w_poziomie, w_pionie):
    pu()
    rt(90)
    fd(w_pionie)
    lt(90)
    bk(w_poziomie)
    pd()
    

def gwiazdy(kod):
    napis_kod = str(kod)
    bok = int(560 / (3*len(napis_kod)))
    wysokosc = oblicz_wysokosc(bok)
    wysokosc_duzego_trojkata = oblicz_wysokosc(3*bok)
    ustaw_na_poczatek(wysokosc_duzego_trojkata)
    for j in range(3):
        for i in range(len(napis_kod)-j):
            nr_gwiazdy = int(napis_kod[i])
            print(nr_gwiazdy)
            if nr_gwiazdy % 2 == 1:
                pusta_gwiazdka(bok, wysokosc, kolory[nr_gwiazdy%4])
            else:
                gwiazdka(bok, kolory[nr_gwiazdy%4])
            przesun_do_nastepnej(bok)
        przesun_do_nowej_linii((len(napis_kod)-j-1)*3*bok, wysokosc + wysokosc_duzego_trojkata)

speed(0)
#gwiazdy(2490)
gwiazdy(1234567890)
