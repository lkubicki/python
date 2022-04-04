szukane = "papadam"
tekst = "papaadm"

liczba_wystapien=0
litera_w_szukane = 0
litera_w_tekscie = 0
while litera_w_tekscie < len(tekst):
    if szukane[litera_w_szukane] == tekst[litera_w_tekscie]:
        litera_w_szukane+=1
        if litera_w_szukane >= len(szukane):
            litera_w_szukane = litera_w_szukane % len(szukane)
            liczba_wystapien+=1
    litera_w_tekscie+=1

print(liczba_wystapien)
