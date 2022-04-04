def robot(liczba_operacji, dlugosc_korytarza):
    pozycja = 0
    naladowanie = liczba_operacji
    maksymalne_ladowanie = liczba_operacji - 1
    do_przodu = True
    while maksymalne_ladowanie > 0 or naladowanie > 0:
        if do_przodu and pozycja < dlugosc_korytarza:
            pozycja = pozycja + 1
            naladowanie = naladowanie - 1
        elif not do_przodu and pozycja > 0:
            pozycja = pozycja - 1
            naladowanie = naladowanie - 1

        if pozycja == dlugosc_korytarza and naladowanie > 0:
            naladowanie = naladowanie - 1
            do_przodu = False
            print(f'{pozycja} {naladowanie} {do_przodu}')
                
        if pozycja == 0 and naladowanie > 0:
            naladowanie = naladowanie - 1
            do_przodu = True
            print(f'{pozycja} {naladowanie} {do_przodu}')

        if naladowanie == 0 and maksymalne_ladowanie > 0:
            naladowanie = maksymalne_ladowanie
            maksymalne_ladowanie = maksymalne_ladowanie - 1
            print(f'{pozycja} {naladowanie} naladowany')

        print(f'{pozycja} {naladowanie}')

    return pozycja

print(robot(6, 7))
print(robot(5,10))
