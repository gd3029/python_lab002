import random
slowa = {}

with open("slowa_l.txt") as file:
    for line in file:
        (key, val) = line.strip().split(":")
        slowa[key.strip()] = [x.strip() for x in val.split(",")]

word = random.choice(list(slowa.keys()))

poprawnie = word
pomie = ""
while word:
    position = random.randrange(len(word))
    pomie += word[position]
    word = word[:position] + word[(position + 1):]
print(pomie)
print("""
Witaj w grze 'Wymieszane litery'!
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.
""")
print("Zgadnij, jakie to słowo:", pomie)
podpowiedz = input("Czy chcesz korzystać z podpowiedzi?(T/N):")
podpowiedz_pozycja = 0
punkty = 10
proba = 0
if(podpowiedz.upper() == "T" ):
    print(slowa[poprawnie][podpowiedz_pozycja])
    podpowiedz_pozycja += 1
    punkty -= 1+podpowiedz_pozycja*1
zgaduj = input("\nTwoja odpowiedź:")
while zgaduj != poprawnie and zgaduj !="" and proba < 2:
    print("Niestety, to nie to słowo.")
    podpowiedz = input("Czy chcesz korzystać z podpowiedzi?(T/N):")
    if(podpowiedz.upper() == "T" ):
        print(slowa[poprawnie][podpowiedz_pozycja])
        podpowiedz_pozycja += 1
        punkty -= 1+podpowiedz_pozycja*1
    zgaduj = input("\nTwoja odpowiedź:")
    proba +=1
if zgaduj == poprawnie:
    print("Zgadza się! Zgadłeś\nZdobyłeś",punkty,"punktów.")
else:
    print("Niestety tym razem nie odgadłeś słowa, poprawna odpoweidź to:", poprawnie)
print("Dziękuję za udział w grze.")
