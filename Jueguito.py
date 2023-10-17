def main():
    intentos = 0
    
    print("El juego consiste en que adivines en que letra estoy pensando del nombre Gustavo. Muchas suerte!")

    while intentos < 5: 
        letra = input('¿Cuál es la letra secreta?: ')
        intentos+=1
        if letra == 's':
            print("Adivinaste! La letra que estaba pensando era la S. Solo te tomó " + str(intentos) + " intentos.")
            break
        
        if letra != 's':
            print("Ups, lo siento. Te equivocaste. Te quedan " + str(5 - intentos) + " intentos")

        if intentos == 5:
            print('Lo siento. Te quedaste sin intentos')
            break


if __name__ == "__main__":
    main()