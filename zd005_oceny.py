import stat_func

print("Program oblicza średnią, medianę oraz odchylenie standardowe.")
userInput = input("Podaj liczby rozdzielając je znakiem spacji: ")
liczby = [float(x.replace(",",".")) for x in userInput.split(" ")]
print("Dla podanych liczb ",liczby," wyniki są następujące:")
print("Średnia:",stat_func.srednia(liczby))
print("Mediana:",stat_func.mediana(liczby))
print("Odchylenie standardowe",stat_func.odchylenieStandardowe(liczby))
