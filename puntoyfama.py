import random


def aleatorio(opciones):
    opciones = list(opciones)
    while True:
        r = random.choice(opciones)
        opciones.remove(r)
        yield int(r)


gen = aleatorio("1234567890")

L1 = next(gen)
L2 = next(gen)
L3 = next(gen)
L4 = next(gen)
NP = [L1, L2, L3, L4]
print(NP)


punto = 0
fama = 0
intentosOrg = 5
intentos = 1


def bPuntosFamas(numero):
    pun = 0
    fam = 0
    l = len(numero)
    for i in range(0, l, 1):
        if(int(NP[i]) == int(numero[i])):
            fam += 1
        else:
            for j in range(0, 4, 1):
                if(int(NP[j]) == int(numero[i])):
                    pun += 1

    return [pun, fam]


print('\033[1;36m'+'BIENVENIDO A PUNTO Y FAMA'+'\033[1;35m')
print('\033[0;37m'+'Tiene 5 intentos para ganar(Se gana con 4 famas)')

while intentos <= intentosOrg and fama == 0:
    puntos = 0
    famas = 0
    num = list(
        input('\033[1;35m'+f'Ingrese un numero (\033[1;33m Intento #{intentos} \033[1;35m):  \033[1;37m'))
    if(len(num) == 4):
        p = bPuntosFamas(num)
        intentos += 1
        print(
            '\033[0;37m' +
            f'Puntos: \033[0;32m {p[0]} \033[0;37m / ' +
            f'Famas: \033[0;32m {p[1]} \033[0;37m  ' +
            '\033[1;37m'
        )
        if(int(p[1]) == 4):
            fama = 1
    else:
        print('\033[1;31m'+'Ingrese solo 4 numeros'+'\033[1;37m')

if(fama == 1):
    print('\033[1;32m'+'GANO EL JUEGO')
else:
    print('\033[1;31m'+'PERDIO EL JUEGO')
