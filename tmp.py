from turtle import * 
from math import sqrt 
 
def kwadrat(bok): 
    begin_fill() 
    for i in range(4): 
        fd(bok); rt(90) 
    end_fill() 
 
def elt1(bok): 
    begin_fill() 
    rt(30) 
    for i in range(3): 
        fd(bok); rt(120) 
    lt(30) 
    end_fill() 
  
def elt2(bok): 
    begin_fill() 
    fd(bok); rt(150) 
    fd(bok); lt(120) 
    fd(bok); rt(150) 
    fd(bok); rt(90) 
    fd(bok); rt(90) 
    end_fill() 
 
def elt3(bok): 
    begin_fill() 
    rt(45) 
    fd(bok * sqrt(2)); rt(135) 
    fd(bok); rt(90) 
    fd(bok); rt(90) 
    end_fill() 
 
def elt4(bok): 
    begin_fill() 
    fd(bok); rt(135) 
    fd(bok * sqrt(2)); rt(135) 
    fd(bok); rt(90) 
    end_fill() 
 
def schemat(lista): 
    a = 50 
    n = len(lista) 
    # wyśrodkowanie rysunku 
    pu(); bk(n * 50 / 2); lt(90); bk(200); rt(90); pd() 
    for i in range(n): 
        lt(90) 
        color("black","green") 
        for j in range(lista[i]): 
            kwadrat(a) 
            fd(a) 
        color("black","lightgray") 
        if lista[(i - 1) % n] < lista[i] > lista[(i + 1) % n]: 
            elt1(a) 
        elif lista[(i - 1) % n] > lista[i] < lista[(i + 1) % n]: 
            elt2(a)        
        elif lista[i] < lista[(i + 1) % n]: 
            elt3(a)  
        elif lista[i] < lista[(i - 1) % n]: 
            elt4(a) 
        fd(-a * (lista[i])) 
        rt(90); fd(a)

#schemat([2, 4, 5, 3, 2, 4, 2])
schemat([1, 2, 3, 2, 1])
