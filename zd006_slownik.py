import csv
from pathlib import Path

def writeDictionary(dictionary, fileName):
    with open(fileName, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,lineterminator='\n', delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for key, val in dictionary.items():
            row = [key]
            for item in val:
                row.append(item.strip())
            writer.writerow(row)

def readDictionary(fileName):
    dictionary = {}
    with open(fileName,'r',newline='') as csvfile:
        reader = csv.reader(csvfile, lineterminator='\n', delimiter=',', quotechar='"')
        for row in reader:
            dictionary[row[0]] = row[1:]
    return dictionary

def showDictionary(fileName):
    file = Path(fileName)
    if file.is_file():
        print("Obecna zawartość słownika:")
        wordDictionary = readDictionary(fileName)
        print(readDictionary(fileName))
    else:
        print("Słownik jeszcze nie istnieje!")
        wordDictionary = {}
    return wordDictionary

fileName = "dictionary.csv"


print("Słownik wyrazów obcych")
print("Nowe wyrazy i ich znaczenia podawaj w następującym formacie: wyraz obcy: znaczenie1, znaczenie2, ... itd.")
print("Pobieranie danych kończy wpsanie słowa koniec.")
wordDictionary = showDictionary(fileName)
userInput = input("Podaj dane: ")

while userInput != "koniec":
    if (":" in userInput and "," in userInput and ":," not in userInput):
        key = userInput.split(":")[0]
        val = userInput.split(":")[1:][0].split(",")
        val = [i for i in val if i.strip()]
        if key.strip() and len(val) > 0:
            wordDictionary[key] = val
            print("Zapis dodany prawidłowo")
            writeDictionary(wordDictionary, fileName)
            showDictionary(fileName)
        else:
            print("Słowo i znaczenie nie może być puste!")
        userInput = input("Podaj dane: ")
    else:
        print("Wprowadziłeś nieprawidłowy format danych!")
        userInput = input("Podaj dane: ")


