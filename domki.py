from turtle import*
from math import*

speed(0)
kratka = 100/5

def rownoleglobok1(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(kratka*sqrt(2)*2)
        rt(45)
        fd(kratka*5)
        rt(135)
    end_fill()

def rownoleglobok2(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(kratka*sqrt(2)*2)
        lt(45)
        fd(kratka*5)
        lt(135)
    end_fill()

def sciana_frontowa():
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(kratka*5)
        lt(90)
    end_fill()

def okno():
    fillcolor("lightblue")
    begin_fill()
    for i in range(4):
        fd(kratka)
        rt(90)
    end_fill()

def przesun_do_kolejnego_okna():
    pu()
    fd(kratka*2)
    fd(kratka)
    rt(90)  
    pd()

def okna():
    for i in range(4):
        okno()
        przesun_do_kolejnego_okna()

def dach():
    rownoleglobok1("red")
    rt(45)
    fd(5*kratka)
    rt(90)
    fd(kratka*5)

def sciana_boczna():
    lt(135)
    rownoleglobok2("gray")
    fd(kratka*2*sqrt(2))
    rt(45)

def przesun_do_okna():
    pu()
    fd(kratka)
    lt(90)
    fd(kratka)
    pd()

def przesun_do_dachu():
    pu()
    fd(kratka*4)
    lt(90)
    fd(kratka)
    pd()
    rt(135)

def przesun_do_parzystego_domku():
    pu()
    bk(4*kratka)
    rt(90)
    fd(4*kratka)
    lt(90)
    pd()

def domek():
    sciana_frontowa()
    przesun_do_okna()
    okna()
    przesun_do_dachu()
    dach()
    sciana_boczna()

def wysrodkuj(n):
    pu()
    bk(policz_domki(n) * kratka / 2)
    rt(90)
    fd(6*kratka)
    lt(90)
    pd()
    
def policz_domki(n):
    suma = 0
    for i in range(n):
        if i % 2 == 0:
            suma += 7
        else:
            suma += 3
    if n % 2 == 0:
        suma += 4
    return suma

def domki(n):
    wysrodkuj(n)
    for i in range(n):
        domek()
        if i % 2 == 1:
            przesun_do_parzystego_domku()

speed(0)
domki(7)
