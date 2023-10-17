import random
respuesta = random.randint(1,20)


def juego(num):
    oportunidades = 4
    while num != respuesta and oportunidades != 0 or num <= 0 or num >= 21:
        oportunidades -= 1
        if num < respuesta and num >= 1:
            print("Te quedaste corto, el número que estoy pensando es más alto. Volvé a intentarlo.")
        if num > respuesta and num < 20:
            print("Te pasaste, el número que estoy pensando es más bajo. Volvé a intentarlo.")
        if num >= 21 or num <= 0:
            oportunidades += 1
            print("Por favor, elige un número entre el 1 y el 20")
        num= int(input("Puedes elegir otro número: "))


    if num == respuesta: 
        print("¡GANASTE!" + " Y solo te tomó " + str(5 - oportunidades) + " intento(s) ¡¡¡CRACK!!!")
    if num != respuesta and oportunidades <= 0:
        print("Ups! Te quedaste sin oportunidades. F")


menu = """
                Hola! Este es mi primer minijuego! :)

El juego consiste en adivinar el número que está pensando el programa
Veamos si puedes ganarle a la máquina, tienes 5 intentos...

(Te doy una pista pero no digas nada... Es un número del 1 al 20)

Suerte!
"""


def run():
    print(menu)
    num = int(input("Por favor, escribe un número: "))
    juego(num)
    print("¡Gracias por utilizar mi primer juego! Te quiero uwu")
    

if __name__ == "__main__":
    run()