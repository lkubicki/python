from turtle import *


def rysuj_kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)


def rysuj_kwadrat_dolny(bok):
    for i in range(4):
        fd(bok)
        lt(90)


def rysuj_kwadraty(bok, ile):
    for i in range(ile):
        rysuj_kwadrat(bok)
        fd(bok)
    pu()
    bk(bok*ile)
    pd()


def rysuj_kwadraty_dolne(bok, ile):
    for i in range(ile):
        rysuj_kwadrat_dolny(bok)
        fd(bok)
    pu()
    bk(bok*ile)
    pd()


def rysuj_koralik(bok):
    for i in range(6):
        fd(bok)
        rt(60)

def przesun_na_poczatek_koralika(bok):
    pu()
    fd(bok)
    lt(30)
    pd()


def przesun_na_poczatek_ogniwa(bok):
    pu()
    rt(90)
    fd(bok)
    lt(90)
    fd(int(bok/2))
    pd()


def przesun_na_poczatek_ogniwa_dol(bok):
    pu()
    fd(int(bok/2))
    pd()


def przesun_na_gorny_kwadrat(bok):
    pu()
    fd(bok)
    rt(60)
    fd(bok)
    lt(30)
    pd()


def rysuj_srodek(bok):
    rysuj_kwadrat(bok)
    przesun_na_poczatek_koralika(bok)
    rysuj_koralik(bok)
    przesun_na_gorny_kwadrat(bok)
    rysuj_kwadrat(bok)


#def rysuj_ogniwo_proste(liczba_kwadratow, bok):
#    for i in range(liczba_kwadratow -1):
#        rysuj_kwadrat(bok)
#        przesun_do_kolejnego_kwadratu_ogniwa(bok)
#    rysuj_kwadrat(bok)
    

def rysuj_ogniwo_zlozone(liczba_kwadratow, bok):
    liczba_wierszy = 0
    for i in range(liczba_kwadratow):
        if i < liczba_kwadratow/2:
            liczba_wierszy += 1
        if i > liczba_kwadratow/2:
            liczba_wierszy -= 1
        rysuj_kwadraty(bok, liczba_wierszy)
        przesun_do_kolejnego_kwadratu_ogniwa(bok)
    

def rysuj_ogniwo_zlozone_dolne(liczba_kwadratow, bok):
    liczba_wierszy = 0
    for i in range(liczba_kwadratow):        
        if i < liczba_kwadratow/2:
            liczba_wierszy += 1
        if i > liczba_kwadratow/2:
            liczba_wierszy -= 1
        rysuj_kwadraty_dolne(bok, liczba_wierszy)
        przesun_do_kolejnego_kwadratu_ogniwa_dolnego(bok)
    

def rysuj_ogniwo_proste_dolne(liczba_kwadratow, bok):
    for i in range(liczba_kwadratow):
        rysuj_kwadrat(bok)
        przesun_do_kolejnego_kwadratu_ogniwa(bok)
    

def rysuj_ogniwo_proste(liczba_kwadratow, bok):
    for i in range(liczba_kwadratow):        
        rysuj_kwadrat_dolny(bok)
        przesun_do_kolejnego_kwadratu_ogniwa_dolnego(bok)
    

def przesun_do_kolejnego_kwadratu_ogniwa(bok):
    pu()
    rt(90)
    fd(bok)
    lt(90)
    pd()
    

def przesun_do_kolejnego_kwadratu_ogniwa_dolnego(bok):
    pu()
    lt(90)
    fd(bok)
    rt(90)
    pd()
    

def przesun_do_kolejnego_srodka(bok):
    pu()
    fd(bok / 2)
    rt(90)
    fd(bok)
    rt(90)
    pd()
    

def przesun_do_kolejnego_srodka_dolnego(bok):
    pu()
    fd(bok / 2)
    lt(180)
    pd()

def przesun_do_kolejnego_ogniwa_prostego(bok):
    pu()
    lt(90)
    fd(bok)
    lt(90)
    fd(bok/2)
    rt(30)
    fd(bok)
    lt(60)
    fd(bok)
    rt(30)
    fd(bok/2)
    pd()
    

def przesun_do_kolejnego_ogniwa_prostego_dolnego(bok):
    pu()
    rt(180)
    fd(bok/2)
    rt(30)
    fd(bok)
    lt(60)
    fd(bok)
    lt(60)
    fd(bok)
    rt(90)
    fd(bok/2)
    pd()
    

def ogniwa(liczba_koralikow, liczba_kwadratow):
    bok = 700 / (liczba_koralikow + liczba_kwadratow * (liczba_koralikow - 1))
    lt(90)
    rysuj_srodek(bok)
    for i in range(liczba_koralikow - 1):
        if i % 2 == 0:
            przesun_na_poczatek_ogniwa(bok)
            rysuj_ogniwo_zlozone(liczba_kwadratow, bok)
            przesun_do_kolejnego_srodka(bok)
        else:
            przesun_na_poczatek_ogniwa_dol(bok)
            rysuj_ogniwo_zlozone_dolne(liczba_kwadratow, bok)
            przesun_do_kolejnego_srodka_dolnego(bok)
        rysuj_srodek(bok)
    if liczba_koralikow % 2 == 0:
        pu()
        rt(90)
        fd(bok)
        lt(90)
        fd(bok/2)
        pd()
    else:
        pu()
        fd(bok/2)
        pd()
    for j in range(i + 1, liczba_koralikow + i):
        if j % 2 == 0:
            rysuj_ogniwo_proste(liczba_kwadratow, bok)
            przesun_do_kolejnego_ogniwa_prostego(bok)
        else:
            rysuj_ogniwo_proste_dolne(liczba_kwadratow, bok)
            przesun_do_kolejnego_ogniwa_prostego_dolnego(bok)
    return

pu()
bk(350)
pd()
speed(0)
ogniwa(9, 6)
