
 
import random
 
def PintaTriki(borde):
    
    print('   |   |')
    print(' ' + borde[1] + ' | ' + borde[2] + ' | ' + borde[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + borde[4] + ' | ' + borde[5] + ' | ' + borde[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + borde[7] + ' | ' + borde[8] + ' | ' + borde[9])
    print('   |   |')
 
def escogerLetra():
   
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Elija un simbolo, X - O')
        letter = input().upper()
 
   
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def turno():
    
    if random.randint(0, 1) == 0:
        return 'maquina'
    else:
        return 'jugador'
 
def jugarDenuevo():
  
    print('Nueva Partida (y o n)')
    return input().lower().startswith('y')
 
def mover(borde, letter, move):
    borde[move] = letter
 
def isGanador(bo, le):
    
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 
 
def copiaTriki(borde):
    
    dupeBoard = []
 
    for i in borde:
        dupeBoard.append(i)
 
    return dupeBoard
 
def isLibre(borde, move):
   
    return borde[move] == ' '
 
def movimientoJugador(borde):
    
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isLibre(borde, int(move)):
        print('Siguiente Movimiento? (1-9)')
        move = input()
    return int(move)
 
def numeroPosible(borde, movesList):
    
    possibleMoves = []
    for i in movesList:
        if isLibre(borde, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def movimientoMaquina(borde, letra):
    
    if letra == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
 
    
    for i in range(1, 10):
        copy = copiaTriki(borde)
        if isLibre(copy, i):
            mover(copy, letra, i)
            if isGanador(copy, letra):
                return i
 
    for i in range(1, 10):
        copy = copiaTriki(borde)
        if isLibre(copy, i):
            mover(copy, playerLetter, i)
            if isGanador(copy, playerLetter):
                return i
 

    move = numeroPosible(borde, [1, 3, 7, 9])
    if move != None:
        return move
 
    
    if isLibre(borde, 5):
        return 5
 
    
    return numeroPosible(borde, [2, 4, 6, 8])
 
def isTableroLleno(borde):
    
    for i in range(1, 10):
        if isLibre(borde, i):
            return False
    return True
 
 

print('\033[1;36m'+'BIENVENIDO A TRIKI'+'\033[1;35m')
# print('\033[0;37m'+')')
 
while True:
    
    theBoard = [' '] * 10
    playerLetter, letra = escogerLetra()
    turn = turno()
    print( turn + ' esta en turno.')
    gameIsPlaying = True
 
    while gameIsPlaying:
        if turn == 'jugador':
            
            PintaTriki(theBoard)
            move = movimientoJugador(theBoard)
            mover(theBoard, playerLetter, move)
 
            if isGanador(theBoard, playerLetter):
                PintaTriki(theBoard)
                print('Jugador gana')
                gameIsPlaying = False
            else:
                if isTableroLleno(theBoard):
                    PintaTriki(theBoard)
                    print('Empate')
                    break
                else:
                    turn = 'maquina'
 
        else:
            move = movimientoMaquina(theBoard, letra)
            mover(theBoard, letra, move)
 
            if isGanador(theBoard, letra):
                PintaTriki(theBoard)
                print('La maquina gana.')
                gameIsPlaying = False
            else:
                if isTableroLleno(theBoard):
                    PintaTriki(theBoard)
                    print('Empate')
                    break
                else:
                    turn = 'jugador'
 
    if not jugarDenuevo():
        break