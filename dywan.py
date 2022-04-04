from turtle import *
from math import *


bok_dywanu=400
bok_cwiartki = bok_dywanu / 2
dluzszy_bok_prostokata = bok_cwiartki / 5 * 2
krotszy_bok_prostokata = bok_cwiartki / 5
krotsze_ramie = bok_dywanu / 10 * sqrt(2) / 2
podstawa = bok_dywanu / 10 * sqrt(2)


def prostokat():
    fd(dluzszy_bok_prostokata)
    rt(90)
    fd(krotszy_bok_prostokata)
    rt(90)
    fd(dluzszy_bok_prostokata)
    rt(90)
    fd(krotszy_bok_prostokata)

def strzalka():
    fillcolor("green")
    pencolor("black")
    begin_fill()
    lt(45)
    fd(krotsze_ramie)
    rt(90)
    fd(krotsze_ramie)
    lt(90)
    fd(podstawa)
    lt(90)
    fd(krotsze_ramie)
    rt(90)
    fd(krotsze_ramie)
    lt(135)
    fd(dluzszy_bok_prostokata)
    lt(90)
    fd(dluzszy_bok_prostokata)
    end_fill()


def ramka_strzalki():
    fillcolor("white")
    pencolor("black")
    begin_fill()
    for i in range(3):
        fd(dluzszy_bok_prostokata)
        lt(90)
    end_fill()
    

def wzorek():
    rt(90)
    prostokat()
    lt(180)
    fd(krotszy_bok_prostokata + dluzszy_bok_prostokata)
    lt(90)
    ramka_strzalki()
    strzalka()
    rt(90)
    fd(krotszy_bok_prostokata)
    rt(90)
    fd(bok_cwiartki)
    

def cwiartka():
    fillcolor("red")
    pencolor("black")
    begin_fill()
    for i in range(3):
        fd(bok_cwiartki)
        rt(90)
    fd(bok_cwiartki)
    end_fill()
    for j in range(4):
        wzorek()


def dywan():
    lt(90)
    for i in range(4):
        cwiartka()
    for i in range(4):
        for j in range(3):
            fd(bok_cwiartki)
            rt(90)
        fd(bok_cwiartki)

speed("fastest")
dywan()
