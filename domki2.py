from turtle import*
speed(0)
kratka = 100/5

def rownoleglobok1(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(kratka*2)
        rt(45)
        fd(kratka*5)
        rt(135)
    end_fill()

def rownoleglobok2(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(kratka*2)
        lt(45)
        fd(kratka*5)
        lt(135)
    end_fill()

def skrypt():
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(kratka*5)
        lt(90)
    end_fill()
    pu()
    fd(kratka)
    lt(90)
    fd(kratka)
    pd()
    fillcolor("lightblue")
    begin_fill()
    for i in range(4):
        fd(kratka)
        rt(90)
    end_fill()
    for i in range(3):
        fillcolor("lightblue")
        begin_fill()
        pu()
        fd(kratka*2)
        pd()
        for i in range(5):
            fd(kratka)
            rt(90)  
        end_fill()
    pu()
    fd(kratka*4)
    rt(90)
    fd(4*kratka)
    pd()
    rt(45)
    rownoleglobok1("red")
    rt(45)
    fd(5*kratka)
    rt(90)
    fd(kratka*5)
    lt(135)
    rownoleglobok2("gray")
    fd(kratka*2)
    rt(45)
def domki(n):
    for i in range(n):
        skrypt()
   
domki(1)
