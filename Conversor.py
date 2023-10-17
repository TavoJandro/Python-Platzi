def conversor(tipo_moneda, valor_dolar):
    moneda = input("¿Cuántos " + tipo_moneda +  " quiere cambiar?: ")
    moneda = float(moneda)
    dólares = moneda / valor_dolar
    dólares = round(dólares, 2)
    dólares = str(dólares)
    print("Tienes $" + dólares + " dólares") 

menu= """
    Bienvenido al conversor de monedas de Tavo 🤑

Aquí podras convetir las siguientes monedas a dólares

1 - Pesos argentinos
2 - Pesos uruguayos
3 - Reales

Por favor, elige una de las opciones anteriores para continuar: """

opcion = int(input(menu))

if opcion == 1:
    conversor("pesos argentinos", 144.51)

elif opcion == 2:
    conversor("pesos uruguayos", 51.15)

elif opcion == 3:
    conversor("reales", 5.15)

else:
    print("Por favor, elegí una de las opciones del menú")