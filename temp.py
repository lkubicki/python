maks = 9
liczba_kwadratow = 0
for i in range(maks):
    if i < maks/2:
        liczba_kwadratow += 1
    if i > maks/2:
        liczba_kwadratow -= 1
    print(liczba_kwadratow)
