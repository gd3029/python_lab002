import math
def srednia(lista):
    """ Zwraca średnią z podanej listy wartości """
    suma = 0.0000
    for liczba in range(len(lista)):
        suma += lista[liczba]
    return suma/len(lista)

def mediana(lista):
    """ Zwraca medianę z podanej listy wartości """

    lista_sort = lista.copy()
    lista_sort.sort()

    med = 0.0000
    if len(lista_sort)%2:
        med = lista_sort[int((len(lista_sort)+1)/2)-1]
    else:
        med = (lista_sort[int(len(lista_sort)/2)-1] + lista_sort[int(len(lista_sort)/2+1)-1])/2
    return med

def odchylenieStandardowe(lista):
    suma = 0.0000
    m = srednia(lista)
    for i in range(len(lista)):
        suma += math.pow((lista[i] - m),2)
    wariancja = suma/len(lista)

    return math.sqrt(wariancja)

