body = []
body.append("'           _______           '")
body.append("'          |  o o  |          '")
body.append("'          |   __  |          '")
body.append("'          |_______|          '")
body.append("'              |              '")
body.append("'             /|\             '")
body.append("'            / | \            '")
body.append("'           /  |  \           '")
body.append("'              |              '")
body.append("'             /|\             '")
body.append("'            / | \            '")
body.append("'           /  |  \           '")


def exitLet(letra):
    ext = 0
    exitos = 0
    l = len(palabraOrg)
    for i in range(0, l, 1):
        if(str(palabraOrg[i]) == str(letra)):
            ext = 1
            palabraAd[i] = palabraOrg[i]
        elif(ext==0):
            ext = 0
        
        if(str(palabraAd[i]) != '_'):
          exitos +=1

    return [ext,exitos]

print('\033[1;35m'+'BIENVENIDO AL QUEMADO'+'\033[1;35m')
print('\033[0;37m'+'Tiene 6 intentos para ganar(Se gana adivinando la palabra)')

palabraOrg = list(input('\033[1;35mIngrese una palabra:  \033[1;37m'))
palabraAd = []
for i in range(0, len(palabraOrg), 1):
  palabraAd.append('_')

intentosOrg = 6
intentosErr = 1
coincidencias = 0

for i in range(0, len(body), 1):
  print(body[i])

print("")
print(palabraAd)

while intentosErr <= intentosOrg and coincidencias<len(palabraOrg):
  letra = input('\033[1;35m'+f'Ingrese una letra (\033[1;33m Te quedan #{intentosOrg-intentosErr+1} Intentos \033[1;35m):  \033[1;37m')
  p = exitLet(letra)
  coincidencias = int(p[1])
  print(coincidencias)
  if(p[0]==1):
    print("")
    print(palabraAd)
  else:
    for i in range(12-(intentosErr*2), 12, 1):
      body[i] = "###############################"
    
    intentosErr +=1

    for i in range(0, len(body), 1):
      print(body[i])

    print("")
    print(palabraAd)


if(coincidencias == len(palabraOrg)):
  print('\033[1;32m'+'GANO EL JUEGO')
else:
  print('\033[1;31m'+'PERDIO EL JUEGO')