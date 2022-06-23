import random

#Változók és típusok
#1.1 feladat

print("Hello")

#2 feladat

#primt("Szia")
#print(szia)
#print"szia"

#Változók
#1 feladat

PI = 3,14
print(PI)

#2 feladat

szo = "szia"
print(szo)

#3 feladat

#szo = 5
    #print(type(szam))

#Műveletek és adatbekérés

#1 feladat


#2 feladat

vezeteknev = input("Mi a vezetekneved?")
keresztnev = input("Mi a keresztneved?")
teljes_nev =(vezeteknev + keresztnev)
print( "Szia" , teljes_nev )

#3 feladat

a = int(input('Írj egy számot'))
a = a + 11 // 5 + 1 // 11 - 10 * 15 % 1
print('A te szerencse számod:', a)

#Másik változat

'''Szerencse szám 1-től 100-ig'''
szam = 1
while szam <= 1:
    szam = szam + 1  
    
    import random
    random_szam = random.randint(1,100)
    print(random_szam)



#Elágazások

#1.1 feladat

valasz = input("Milyen napod volt?")
if  valasz == "Jó":
    print("Az jó")

elif  valasz == "rosz":
    print("Az nem jó")

else: 
    print("Nem értem")


#1.2 feladat
szam1 = int (input("Kérek 1 számot"))

if szam1 % 2 == 0:
    print("A szám páros")

else:
    print("A szám páratlan")

#1.3 feladat
szam2 = int (input("Kérek 1 számot"))   

random_szam = random.randint(1,5)
if random_szam == szam2:
    print("Eltaláltad mert ügyes vagy")
elif random_szam < szam2:
    print("Ez nagyobb")
else:
    print("Ez kisebb")

#Logikai kifejezések
# 1 feladat   
 
szam4 =  int (input("Kérek 1 egész számot"))

if szam4 % 2 == 0:
    print("A szám pozitív páros")

elif szam4 % 3 == 1:
    print("A szám negatív páratlan")    





#Ciklusok
#1. Feladat
 

#2. Feladat

szam = 10
while szam >= 0:
  print(szam)
  szam = szam -1   

#3. Feladat

szam = 9
while szam >= 0:
  print(szam)
  szam = szam -2  

#4. feladat

print ('Hányszor szeretnéd ki írattatni?')
a = input()
print ('Milyen szöveget akarsz ki írtatni?')
b = input()
szamlalo = 1
while szamlalo <= int(a):
    print(b)
    szamlalo = szamlalo + 1


#5. Feladat
szam6 = 1
while szam6 % 2 != 0:
    szam6 = int (input("Írj be 1 páros számot"))
print("Program vége")    


#6. Feladat

szam = 1
while szam <= 20:
    szam = szam + 1  
    
    import random
    random_szam = random.randint(1,12)
    oszthato3 = (random_szam % 3 == 0)
    if oszthato3:
        print(random_szam)



