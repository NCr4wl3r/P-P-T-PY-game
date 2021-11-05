import random

# Lista de posibilidades en piedra, papel, tijera
seleccion = ['pi', 'pa', 'ti']

def ganador(jug1, jug2):
    # comprobamos quien tiene la seleccion ganadora
    if jug1 == jug2:
        print ('Empate!')
    elif ((jug1 == 'pi') and (jug2 == 'ti')) or ((jug1 == 'pa') and (jug2 == 'pi')) or ((jug1 == 'ti') and (jug2 == 'pa')):
        print ('Jugador 1 gana!')
    else:
        print ('Jugador 1 pierde!')

def play():
    print("**** Piedra, papel o tijera! ****")
    jugador1 = None
    
    # procuramos que el jugador selecciones una opcion correcta
    while(not jugador1 in seleccion):
        print("A continuacion Jugador1, selecciona: (pi)edra, (pa)pel o (ti)jera:")
        jugador1 = input(':>')   
   
    # Escogemos aleatoriamente una de las selecciones posibles
    jugadorIA = random.choice(seleccion)
    
    ganador(jugador1, jugadorIA)
    print(f'Jugador1 selecciono: {jugador1} vs IA: {jugadorIA}')

play()
