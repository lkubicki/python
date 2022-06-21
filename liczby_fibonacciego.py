liczby_fibonacciego = []


def przygotuj_liczby_fibonacciego(ile):
    liczby_fibonacciego.append(0)
    liczby_fibonacciego.append(1)
    liczby_fibonacciego.append(2)
    for i in range(3, ile + 1):
        liczby_fibonacciego.append(liczby_fibonacciego[i - 2] + liczby_fibonacciego[i - 1])


def przelicz_na_fibonacciego(liczba):
    wynik = ''
    for licznik in range(len(liczby_fibonacciego) - 1, 0, -1):
        if liczba / liczby_fibonacciego[licznik] >= 1:
            wynik += '1'
            liczba -= liczby_fibonacciego[licznik]
        elif wynik != '':
            wynik += '0'
    return wynik


przygotuj_liczby_fibonacciego(5000)
# print(przelicz_na_fibonacciego(3))
# print(przelicz_na_fibonacciego(11))
# wynik = przelicz_na_fibonacciego(16)
wynik = przelicz_na_fibonacciego(1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890)

suma = 0
for i in range(len(wynik), 0, -1):
    suma += liczby_fibonacciego[i] * int(wynik[len(wynik) - i])
print(suma)