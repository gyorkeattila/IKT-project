szam = 1
while szam <= 40:
    szam = szam + 1  
    
    import random
    random_szam = random.randint(1,40)
    oszthato3 = (random_szam % 3 == 0)
    if oszthato3:
        print(random_szam)






szam = 1
while szam <= 40:
    szam = szam + 3
    
    import random
    oszthato_szam = random.randint(1,40)
    oszthato3 = (oszthato_szam % 3 == 0)
    if oszthato3:
        print(oszthato_szam)

  




for oszthato in range(40):
    if oszthato % 3 == 0:
        print(oszthato)