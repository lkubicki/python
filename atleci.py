from turtle import *

def rysuj_brzuch(kratka):
    fillcolor("green")
    begin_fill()
    for i in range(4):
        fd(2*kratka)
        rt(90)
    end_fill()

def rysuj_glowe(kratka):
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        lt(90)
        fd(kratka)
    end_fill()


def rysuj_rece_w_dol(kratka):
    pu()
    lt(90)
    fd(kratka)
    rt(90)
    pd()
    fd(2*kratka)
    rt(90)
    fd(2.5*kratka)
    rysuj_glowe(kratka)
    fd(1.5*kratka)
    rt(90)
    fd(2*kratka)
    pu()
    rt(90)
    fd(kratka)
    lt(90)
    pd()
    
def rysuj_rece_w_gorze(kratka):
    pu()
    lt(90)
    fd(kratka)
    rt(90)
    fd(4*kratka)
    rt(180)
    pd()
    fd(2*kratka)
    lt(90)
    fd(2.5*kratka)
    rysuj_glowe(kratka)
    fd(1.5*kratka)
    lt(90)
    fd(2*kratka)
    pu()
    rt(180)
    fd(4*kratka)
    rt(90)
    fd(kratka)
    lt(90)
    pd()

def rysuj_korpus(kratka, rece_w_gorze):
    fd(kratka)
    lt(90)
    fd(2*kratka)
    rysuj_brzuch(kratka)
    if rece_w_gorze:
        rysuj_rece_w_gorze(kratka)
    else:
        rysuj_rece_w_dol(kratka)
    fd(2*kratka)
    lt(90)
    fd(kratka)

def rysuj_ciezar(kratka):
    dlugosc = 3
    for i in range(3):
        lt(90)
        bk(dlugosc / 2 * kratka)
        fd(dlugosc * kratka)
        bk(dlugosc / 2 * kratka)
        rt(90)
        fd(0.5*kratka)
        dlugosc -= 1
    fd(5 * kratka)
    for i in range(3):
        dlugosc += 1
        fd(0.5*kratka)
        lt(90)
        bk(dlugosc / 2 * kratka)
        fd(dlugosc * kratka)
        bk(dlugosc / 2 * kratka)
        rt(90)
    

def przesun_do_ciezaru(kratka, rece_w_gorze):
    pu()
    bk(6*kratka)
    lt(90)
    if rece_w_gorze:
        fd(6*kratka)
    else:
        fd(1.5*kratka)
    rt(90)
    pd()

def przesun_do_kolejnego_atlety(kratka, rece_w_gorze):
    pu()
    fd(3*kratka)
    rt(90)
    if rece_w_gorze:
        fd(6*kratka)
    else:
        fd(1.5*kratka)
    lt(90)
    pd()

def centruj(kratka, ilu):
    pu()
    bk(380)
    lt(90)
    bk(4.5*kratka)
    pd()
    rt(90)

def rysuj_atlete(kratka, rece_w_gorze):
    rysuj_korpus(kratka, rece_w_gorze)
    przesun_do_ciezaru(kratka, rece_w_gorze)
    rysuj_ciezar(kratka)
    

def atleci(ilu):
    liczba_kratek = 9 * ilu + 1
    wielkosc_kratki = int(760 / liczba_kratek)
    centruj(wielkosc_kratki, ilu)
    rece_w_gorze = False
    for i in range(ilu):
        rysuj_atlete(wielkosc_kratki, rece_w_gorze)
        przesun_do_kolejnego_atlety(wielkosc_kratki, rece_w_gorze)
        rece_w_gorze = not rece_w_gorze
    return

speed(0)
atleci(6)
