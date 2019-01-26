import math
def checkIfTriangle(a,b,c):
    p = (a+b+c)/2
    check = p*(p-a)*(p-b)*(p-c)
    if check > 0:
        return True
    else:
        return False

def checkIfRightTriangle(a,b,c):
    list = [a, b, c]
    list.sort()
    if math.pow(list[0], 2) + math.pow(list[1], 2) == math.pow(list[2], 2):
        return True
    else:
        return False

def calculateTriangleCuircuit(a,b,c):
    return a + b + c

def calculateTriangleArea(a,b,c):
    p = (a+b+c)/2
    check = p*(p-a)*(p-b)*(p-c)
    area = math.sqrt(check)
    return area


userInput = input("Podaj długości boków trójkąta rozdzielone znakiem spacji: ")
boki = [float(x.replace(",",".")) for x in userInput.split(" ")]

if checkIfTriangle(boki[0], boki[1], boki[2]):
    print("Podane boki tworzą trójkąt na tej samej płaszczyźnie.")
    if checkIfRightTriangle(boki[0], boki[1], boki[2]):
        print("Trójkąt jest prostokątny.")
    else:
        print("Trójkąt nie jest prostokątny.")
    print("Obwód wynosi:",calculateTriangleCuircuit(boki[0], boki[1], boki[2]))
    print("Pole wynosi:",calculateTriangleArea(boki[0], boki[1], boki[2]))
else:
   print("Podane boki nie tworzą trójkąt na tej samej płaszczyźnie.")

