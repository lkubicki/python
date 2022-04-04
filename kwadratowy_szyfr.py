from turtle import *

def ktory_pelny(litera):
    return ord(litera)-ord('a')


def pusty_kwadracik(bok):
    for i in range(4):
        fd(bok)
        rt(90)


def pelny_kwadracik(bok):
    fillcolor('red')
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

def zmien_kolumne(bok):
    pu()
    rt(90)
    fd(bok*2)
    rt(90)
    bk(bok)
    pd()

def zmien_litere():
    rt(180)
    

def rysuj_kolumny(litera, bok):
    pelny = ktory_pelny(litera)
    for i in range (26):
        if i == pelny:
            pelny_kwadracik(bok)
        else:
            pusty_kwadracik(bok)
        if i == 12:
            zmien_kolumne(bok)
        else:
            ustaw_na_pocztek_kwadracika(bok)


def ustaw_na_poczatek_obrazka(bok):
    pu()
    rt(90)
    fd(6.5*bok)
    rt(90)
    fd(760/2)
    pd()
    rt(90)

def ustaw_na_pocztek_kwadracika(bok):
    fd(bok)


def kod(tekst):
    bok = round(760 / (len(tekst)*2))

    print(bok)
    
    ustaw_na_poczatek_obrazka(bok)
    for litera in tekst:
        rysuj_kolumny(litera, bok)
        zmien_litere()

speed(0)
kod("alamakota")
