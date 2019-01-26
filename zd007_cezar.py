def encrypt(string):
    cypherText = ""
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            cypherText += chr(65 + (ord(string[i])-62) % 26)
        else:
            cypherText += string[i]
    return cypherText

def decrypt(string):
    deCypherText = ""
    for i in range(len(string)):
        if string[i] >= 'A' and string[i] <= 'Z':
            deCypherText += chr(65 + (ord(string[i])-42) % 26)
        else:
            deCypherText += string[i]
    return deCypherText

plainText = input("Podaj tekst to zaszyfrowania: ").upper()
encrypted = encrypt(plainText)
print(encrypted)
print(decrypt(encrypted))


