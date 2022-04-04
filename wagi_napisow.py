def wylicz_wage_slowa(slowo):
    wynik=0
    for i in range(int(len(slowo)/2)):
        wynik = wynik + 2 * (i + 1)
    if len(slowo)%2 == 1:
        wynik = wynik + i + 2
    return wynik


def podaj_wage(element):
    return element[0]


def posortuj_slowa(wagi_slow):
    return wagi_slow.sort(key = podaj_wage)


def wypisz_zdanie(wagi_slow):
    for element in wagi_slow:
        print(element)


zdanie = input()
wagi_slow = []
slowa = zdanie.split(' ')
for slowo in slowa:
    wagi_slow.append([wylicz_wage_slowa(slowo), slowo])
posortuj_slowa(wagi_slow)
wypisz_zdanie(wagi_slow)
