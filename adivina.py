import random

def numeroAdivinar(numero, jugador):
    if jugador  == numero :
        print("Has ganado el juego, apuesta los ahorros de tu vida.")
    else:
        print("Has fracasado...como todo en tu vida.")



numero = random.randint(1, 10)


jugador = int(input("Ingrese un numero del 1 al 10: "))


numeroAdivinar(numero, jugador)


