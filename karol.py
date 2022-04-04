def kolejna(poczatkowa, ktora):
    kolejne = 0
    aktualna = poczatkowa
    while kolejne < ktora:
        aktualna+=1
        if '3' not in str(aktualna):
            kolejne +=1
    return aktualna

print(kolejna(28, 5))
