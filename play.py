print('\033[1;32m'+'BIENVENIDO A JUEGOS DE CONSOLA')
print('\033[1;32m'+'1. TRIKI')
print('\033[1;32m'+'2. PUNTO Y FAMA')
print('\033[1;32m'+'3. EL QUEMADO')

opcion = int(input('\033[1;33m'+'Ingrese una opcion: \033[1;37m'))

if(opcion == 1):
  import triki

if(opcion == 2):
  import puntoyfama

if(opcion == 3):
  import quemado