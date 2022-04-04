from turtle import *

kratka = 7

def rysuj_klocek():
    fillcolor("red")
    begin_fill()
    for i in range(4):
        fd(2*kratka)
        lt(90)
        fd(kratka)
        rt(90)
        fd(kratka)
        rt(90)
        fd(kratka)
        lt(90)
        fd(2*kratka)
        lt(90)
    end_fill()

def rysuj_lacznik(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(3*kratka)
        lt(90)
        fd(kratka)
        lt(90)
    end_fill()

def przesun_do_lacznika_poziomego():
    pu()
    bk(2*kratka)
    lt(90)
    fd(2*kratka)
    rt(90)
    pd()

def przesun_do_lacznika_pionowego():
    pu()
    fd(3*kratka)
    lt(90)
    fd(4*kratka)
    rt(90)
    pd()
    lt(90)

def przesun_do_klocka_poziomo():
    pu()
    fd(2*kratka)
    rt(90)
    fd(2*kratka)
    lt(90)
    pd()

def przesun_do_klocka_pionowo():
    pu()
    fd(2*kratka)
    lt(90)
    fd(3*kratka)
    lt(180)
    pd()

def przesun_do_kolejnej_kolumny(liczba_klockow):
    pu()
    if liczba_klockow > 0:
        rt(90)
        fd(6*kratka*liczba_klockow)
        lt(90)
    fd(6*kratka)
    pd()

def centruj_obrazek(ile_klockow):
    pu()
    bk(6*kratka * ile_klockow/2 - kratka /2)
    lt(90)
    bk(6*kratka * ile_klockow/2 - kratka /2)
    rt(90)
    pd()

def piramida(ile_klockow):
    centruj_obrazek(ile_klockow)
    for i in range(ile_klockow):
        rysuj_klocek()
        
        for j in range(i):
            if j < ile_klockow - 1:
                przesun_do_lacznika_poziomego()
                rysuj_lacznik("green")
                przesun_do_klocka_poziomo()

                przesun_do_lacznika_pionowego()
                rysuj_lacznik("yellow")
                przesun_do_klocka_pionowo()

            rysuj_klocek()

        przesun_do_kolejnej_kolumny(i)
            
            
    
speed(0)
piramida(5)
