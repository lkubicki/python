def nasluch2(napis1, napis2):
    suma = 0
    tekst1, tekst2 = list(napis1), list(napis2)
    for i in range(min(len(tekst1), len(tekst2))):
        if tekst1[i] == tekst2[i]:
            suma = suma + 10
            tekst1[i] = '_'
            tekst2[i] = '_'

    for i in range(len(tekst1)):
        if tekst1[i] != '_':
            for j in range(len(tekst2)):
                if tekst1[i] == tekst2[j] and tekst2[j] != '_':
                    suma += 1
                    tekst1[i] = '_'
                    tekst2[j] = '_'
    
    return suma

napis = "aaabbb aabb".split(" ")
print(nasluch2(napis[0], napis[1]))
