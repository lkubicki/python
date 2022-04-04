from turtle import *
from math import *

liczba_lopat = 12
obrot = 360/liczba_lopat
dlugosc_zielonej=125
element_zielonej=dlugosc_zielonej / 10
dlugosc_czerwonej=250
element_czerwonej=dlugosc_czerwonej / 10

def lopata_zielona(dlugosc, segment):
    pd()
    fillcolor("green")
    begin_fill()
    fd(dlugosc)
    lt(90)
    fd(3 * segment)
    lt(135)
    fd(3 * segment * sqrt(2) + 2 * segment * sqrt(2))
    rt(135)
    fd(2 * segment + segment)
    lt(135)
    fd(segment * sqrt(2))
    rt(45)
    end_fill()
    pu()
    fd(4 * segment)
    lt(180)
    

def lopata_czerwona(dlugosc, segment):
    pd()
    fillcolor("red")
    begin_fill()
    fd(dlugosc)
    rt(90)
    fd(3 * segment)
    rt(135)
    fd(3 * segment * sqrt(2) + 2 * segment * sqrt(2))
    lt(135)
    fd(2 * segment + segment)
    rt(135)
    fd(segment * sqrt(2))
    lt(45)
    end_fill()
    pu()
    fd(4 * segment)
    lt(180)

def wiatrak():
    for i in range(liczba_lopat):
        if i % 2 == 0:
            lopata_zielona(dlugosc_zielonej, element_zielonej)
        else:
            lopata_czerwona(dlugosc_czerwonej, element_czerwonej)
        lt(obrot)
    fillcolor("black")

wiatrak()
