import random
nevek=[]
for x in range(100):
    print('Ha nem szeretnél több nevet megadni írd be hogy:"n"')
    y=str(input('Ki(k)ről szeretnéd tudni hogy buzi(k):'))
    if y=='n':
        break
    nevek.append(y)
randomfos=[]
for y in range(len(nevek)):
    randomfos.append(random.randrange(0,2))
kaki=0
buzik=[]
nem_buzik=[]
for f in range(len(nevek)):
    if randomfos[kaki]==1:
        buzik.append(nevek[kaki])
    elif randomfos[kaki]==0:
        nem_buzik.append(nevek[kaki])
    kaki=kaki+1
for boti in nem_buzik:
    if boti=='Botond':
        nem_buzik.remove(boti)
        buzik.append(boti)
    elif boti=='Boti':
        nem_buzik.remove(boti)
        buzik.append(boti)
    elif boti=='boti':
        nem_buzik.remove(boti)
        buzik.append(boti)
    elif boti=='botond':
        nem_buzik.remove(boti)
        buzik.append(boti)
if len(buzik)>0:
    print('Ez(ek) az ember(ek) buzik:', buzik)
if len(nem_buzik)>0:
    print('Ez(ek) az ember(ek) nem buzik:', nem_buzik)
asd=input('Press any key to exit')