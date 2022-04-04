import random

wisielcy = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
slowa = ['automat', 'python', 'programowanie','warszawa','frytki','szkoła','miód']

random.seed()
slowo_do_odgadniecia = slowa[random.randint(0,len(slowa)-1)]
odgadniete = []

for literka in range(0, len(slowo_do_odgadniecia)):
    odgadniete.append('_')

print(slowo_do_odgadniecia)

koniec = False
bledy = 0

while not koniec and bledy < len(wisielcy) - 1:
    #podaj litere
    blad = True
    koniec = True
    print(odgadniete)
    literka = (input("Podaj literkę:"))[0].upper()
    #sprawdz, czy litera wystepuje w slowie i wyswietl wszystkie jej wystapienia
    for i in range(0, len(slowo_do_odgadniecia)):
        if slowo_do_odgadniecia[i].upper() == literka:
            odgadniete[i] = literka            
            blad = False
    #jesli literki nie ma w slowie - dorysuj kawalek wisielca
    if blad:
        bledy = bledy + 1
    for i in range(0, len(slowo_do_odgadniecia)):
        if odgadniete[i] == '_':
            koniec = False
    if blad:
        print(wisielcy[bledy])
print(slowo_do_odgadniecia)
