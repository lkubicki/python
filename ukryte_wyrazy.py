rozmiar = 10
kierunki = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def przygotuj_tabelke(ciag):
    nr_kolumny = 0
    tabelka = []
    wiersz = []
    for litera in ciag:
        nr_kolumny += 1
        if (nr_kolumny > rozmiar):
            tabelka.append(wiersz)
            nr_kolumny = 1
            wiersz = []
        wiersz += litera
    tabelka.append(wiersz)
    return tabelka


def szukaj_w_tabelce_od_miejsca(tabelka, wyraz, wiersz, kolumna):
    if len(wyraz) == 0:
        return wiersz * 10 + kolumna + 1

    if 0 <= wiersz < rozmiar and 0 <= kolumna < rozmiar:
        if tabelka[wiersz][kolumna] == wyraz[0]:
            for i in range(4):
                znaleziono = szukaj_w_tabelce_od_miejsca(tabelka, wyraz[1:], wiersz + kierunki[i][0],
                                                         kolumna + kierunki[i][1])
                if znaleziono >= 0:
                    return wiersz * 10 + kolumna + 1
    return -1


def szukaj_w_tabelce(tabelka, wyraz):
    znaleziono = -1
    nr_wiersza = 0
    nr_kolumny = 0
    while znaleziono == -1 and nr_wiersza + nr_kolumny < 2 * rozmiar:
        znaleziono = szukaj_w_tabelce_od_miejsca(tabelka, wyraz, nr_wiersza, nr_kolumny)
        nr_kolumny += 1
        if nr_kolumny >= rozmiar:
            nr_kolumny = 0
            nr_wiersza += 1
    print(znaleziono)


def ukryte_wyrazy(ciag, wyraz):
    tabelka = przygotuj_tabelke(ciag)
    return szukaj_w_tabelce(tabelka, wyraz)


ukryte_wyrazy("ABCDERASSQMGYUKAESSQTRWOISOABCUIHKAIWYUKYEWAGHOSSQRTTKRAKYUKWYUKAYUKSQISSQASSQUKEYYUKYUKSQOSASQAQYUK",
              "KRAKOWIAK")
ukryte_wyrazy("AXCDERASSQMGLECAESSQTRWOISOAKCUWHKAIWYUKYEWAGHOSSRRTTKRAKMUKWTUKAYUKSQISSCASSQUWEUYEKYUKSQOSALQAQYUK",
              "CEL")
ukryte_wyrazy("AXCDERASSQMGLECAESSQTRWOISOAKCUWHKAIWYUKYEWAGHOSSRRTTKRAKMUKWTUKAYUKSQISSCASSQUWEUYEKYUKSQOSALQAQYUK",
              "NIEMA")
