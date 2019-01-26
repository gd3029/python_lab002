start = int(input("Poaj początek przedziału: "))
stop = int(input("Poaj koniec przedziału: "))
krok = int(input("Poaj krok: "))

przedzial = range(start,stop+1,krok)

for i in przedzial:
    print(i)
