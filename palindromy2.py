def ispalindrom(napis):
    dlugosc = len(napis)
    for i in range(int(dlugosc/2)):
        if napis[i] != napis[dlugosc - i - 1]:
            return False
    return True

def znajdz_ostatni_palindrom(napis):
    dlugosc = len(napis)
    p1 = dlugosc
    for i in range(dlugosc):
        if ispalindrom(napis[i:dlugosc]):
            return i - 1
    return p1 - 1

def palindrom_od_konca(napis):
    tekst = ''
    p1 = znajdz_ostatni_palindrom(napis)
    for i in range(p1, -1, -1):
        tekst = tekst + napis[i]
    return(napis + tekst)

def znajdz_pierwszy_palindrom(napis):
    dlugosc = len(napis)
    p1 = 0
    for j in range(dlugosc):
        if ispalindrom(napis[:j]):
            p1 = j
    return p1

def palindrom_od_poczatku(napis):
    tekst = ''
    p1 = znajdz_pierwszy_palindrom(napis)
    for i in range(p1, len(napis)):
        tekst = napis[i] + tekst
    return(tekst + napis)


def roz(napis):
    if ispalindrom(napis):
        return napis
    else:
        palindromy = []
        palindromy.append(palindrom_od_poczatku(napis))
        palindromy.append(palindrom_od_konca(napis))
        if len(palindromy[0]) < len(palindromy[1]):
            return palindromy[0]
        elif len(palindromy[0]) > len(palindromy[1]):
            return palindromy[1]
        else:
            palindromy.sort()
            return palindromy[0]
        

print(roz("ko"))
print(roz("abba"))
print(roz("abbaca"))
