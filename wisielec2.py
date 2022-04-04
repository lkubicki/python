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
slowo_do_odgadniecia = slowa[random.randint(0,len(slowa)-1)].upper()
odgadniete = []

for literka in range(0, len(slowo_do_odgadniecia)):
    odgadniete.append('_')

print(slowo_do_odgadniecia)

wygrana = False
liczba_prob = 0

while not wygrana and liczba_prob < len(wisielcy):
    print(odgadniete)
    print(wisielcy[liczba_prob])
    #podaj litere    
    literka = (input("Podaj literkę:"))[0].upper()
    #sprawdz, czy litera wystepuje w slowie i wyswietl wszystkie jej wystapienia
    odgadnieta = False
    for i in range(0, len(slowo_do_odgadniecia)):
        if slowo_do_odgadniecia[i].upper() == literka:
            odgadnieta = True
            odgadniete[i] = literka            
    #jesli literki nie ma w slowie - dorysuj kawalek wisielca
    if not odgadnieta:
        liczba_prob = liczba_prob + 1
    #jesli slowo zostalo odgadniete - koniec - wygrales
    wygrana = (''.join(odgadniete).upper() == slowo_do_odgadniecia)
    #jesli wisielec narysowany caly - koniec - porazka
    print(liczba_prob)
    print(len(wisielcy))
if wygrana:
    print("BRAWO!")
else:
    print("No cóż...")
