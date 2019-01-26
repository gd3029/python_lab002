import random

with open("slowa.txt","r") as f:
    slowa = f.read().splitlines()
slowo = random.choice(slowa).upper()

uzyte = {}

for i in range(5):
    litera = input("Podaj literę:").upper()
    while litera in uzyte.keys():
        print("Już wykorzystałeś literę", litera)
        litera = input("Wprowadź literę:").upper()

    if litera in slowo:
        print("Litera",litera,"znajduje się w zagadkowym słowie.")
        uzyte[litera] ="tak"
    else:
        print("Litera",litera,"nie znajduje się w zagadkowym słowie.")
        uzyte[litera] = "nie"
    print("Użyłeś następujących liter", uzyte)

odp = input("Podaj prawidłową odpowiedź: ").upper()

if odp == slowo:
    print("Zgadłeś! Wygrywasz!")
else:
    print("Porażka, nie tym razem!")
    print("Zagatkowe słowo to:", slowo)
