#1
import re


lista = [0, 1, 2, 3, 4, 5]


def karakteszterszama(a):
        with open(a, "r") as f:
            adat = f.read()
        return len(adat)


#2
def sorokszama(b):
    return len(b.split("/n"))




#3
def asd(c):
    return c.count("x")


#4
def elsoketto(d):
    return d[0,2]

                               


#5
def szorzas(r):
    a = 1
    for c in r:
        a *=c
    return a 



#6
#with open("soccer.txt", "r", encoding ="UTF-8") as fajl:



def lista_elemek_szama(d):
    a = 0
    for elem in d:
        a += elem
    return a

def szorzat(e):
    x = 1, 2
    for szam in e:
        x*= szam
    return x


def legnagyobb(r):
    j = r[0]
    for nagy in r:
        if e < nagy:
            e = nagy
    return e        




def parosok_szama(g):
    a = 0
    for szam in g:
        if szam % 2 == 0:
            a += 1 
    return a        

def elso_utolso(asd):
    return [asd[0], asd[-1]]


















































def paros_szamok(lista):
    x = 0
    for i in lista:
        if i % 2 == 0:
            x += 1
    
    return x     







