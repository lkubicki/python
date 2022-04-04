from turtle import *
from math import *


def rysuj_kwadrat():
    fillcolor("green")
    begin_fill()
    for i in range(4):
        fd(50)
        rt(90)
    end_fill()


def rysuj_kwadraty(ile):
    for i in range(ile):
        rysuj_kwadrat()
        fd(50)


def przesun_do_kolejnej_kolumny(wysokosc):
    pu()
    rt(90)
    fd(50)
    rt(90)
    fd(50*wysokosc)
    rt(180)
    pd()


def rysuj_trojkat_rownoramienny():
    fillcolor("gray")
    begin_fill()
    lt(90)
    for i in range(3):
        rt(120)
        fd(50)
    rt(90)
    end_fill()


def rysuj_trojkat_prostokatny_lewy():
    fillcolor("gray")
    begin_fill()
    rt(45)
    fd(50*sqrt(2))
    rt(135)
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    end_fill()


def rysuj_trojkat_prostokatny_prawy():
    fillcolor("gray")
    begin_fill()
    fd(50)
    rt(135)
    fd(50*sqrt(2))
    rt(135)
    fd(50)
    rt(90)
    end_fill()


def rysuj_wyciety_kwadrat():
    fillcolor("gray")
    begin_fill()
    fd(50)
    rt(150)
    fd(50)
    lt(120)
    fd(50)
    rt(150)
    fd(50)
    rt(90)
    fd(50)
    rt(90)
    end_fill()


def podaj_lewy(definicja, aktualny):
    if aktualny == 0:
        return 0
    return definicja[aktualny - 1]


def podaj_prawy(definicja, aktualny):
    if aktualny == len(definicja) - 1:
        return 0
    return definicja[aktualny + 1]


def wyznacz_rodzaj(lewy, aktualny, prawy):
    if lewy < aktualny and prawy < aktualny:
        return 1
    elif lewy > aktualny and prawy > aktualny:
        return 2
    elif lewy <= aktualny and prawy > aktualny:
        return 3
    elif lewy > aktualny and prawy <= aktualny:
        return 4
    else:
        return 0


def rysuj_czubek(definicja, aktualny):
    lewy = podaj_lewy(definicja, aktualny)
    prawy = podaj_prawy(definicja, aktualny)
    aktualny = definicja[aktualny]
    rodzaj = wyznacz_rodzaj(lewy, aktualny, prawy)
    if rodzaj == 1:
        rysuj_trojkat_rownoramienny()
    elif rodzaj == 2:
        rysuj_wyciety_kwadrat()
    elif rodzaj == 3:
        rysuj_trojkat_prostokatny_lewy()
    elif rodzaj == 4:
        rysuj_trojkat_prostokatny_prawy()
        


def schemat(definicja):
    lt(90)
    for i in range(len(definicja)):
        rysuj_kwadraty(int(definicja[i]))
        rysuj_czubek(definicja, i)
        przesun_do_kolejnej_kolumny(int(definicja[i]))

speed(0)
schemat([1, 2, 3, 2, 1])
