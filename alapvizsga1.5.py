felhasznalo_nev = 'bori99'
jelszo = 'Szivecske<3'

while True:
  user = input('Adja meg a felhasználónevét! ')
  password = input('Adja meg a jelszavát! ')
  if user == 'bori99' and password == 'Szivecske<3':
    print('Belépés engedélyezve.')
    break
  else:
    print('Belépés megtagadva.')
