def pluss(a):
    b= int(input("Anna teine number: "))
    c=a+b
    a=c
    return a

def miinus(a):
    b= int(input("Anna teine number: "))
    c=a-b
    a=c
    return a

def jaga(a):
    b= int(input("Anna teine number: "))
    c=a/b
    a=c
    return a

def korruta(a):
    b= int(input("Anna teine number: "))
    c=a*b
    a=c
    return a

a = int(input("Anna esimene number: "))
while True:
    
    tehe = input("Mis tehet tahad teha (/ * - +):  ")
    if tehe == "+":
        print(pluss(a))
    if tehe == "-":
        print(miinus(a))
    if tehe == "/":
        print(jaga(a))
    if tehe == "*":
        print(korruta(a))
    veel = input("Jätkad (Jah) või alustad uuesti(Ei)?")
    if veel == "Ei":
        a=0
        b=0
        a = int(input("Anna esimene number: "))