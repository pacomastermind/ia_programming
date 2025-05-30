import random

# Valores de las cartas
cartas = {
    'A': 11, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}

# Crear una baraja
def crear_baraja():
    return list(cartas.keys()) * 4

# Calcular el valor de una mano
def calcular_valor(mano):
    valor = sum(cartas[carta] for carta in mano)
    ases = mano.count('A')
    while valor > 21 and ases:
        valor -= 10  # Convertir un As de 11 a 1
        ases -= 1
    return valor

# Mostrar la mano del jugador
def mostrar_manos(jugador, dealer, ocultar_dealer=True):
    print("\nMano del Jugador:", jugador, "| Valor:", calcular_valor(jugador))
    if ocultar_dealer:
        print("Mano del Dealer: [?,", dealer[1], "]")
    else:
        print("Mano del Dealer:", dealer, "| Valor:", calcular_valor(dealer))

# Lógica del juego
def jugar_blackjack():
    baraja = crear_baraja()
    random.shuffle(baraja)

    jugador = [baraja.pop(), baraja.pop()]
    dealer = [baraja.pop(), baraja.pop()]

    mostrar_manos(jugador, dealer)

    # Turno del jugador
    while True:
        opcion = input("¿Quieres 'pedir' o 'plantarte'? ").lower()
        if opcion == 'pedir':
            jugador.append(baraja.pop())
            mostrar_manos(jugador, dealer)
            if calcular_valor(jugador) > 21:
                print("Te pasaste. Pierdes.")
                return
        elif opcion == 'plantarte':
            break
        else:
            print("Opción no válida.")

    # Turno del dealer
    while calcular_valor(dealer) < 17:
        dealer.append(baraja.pop())

    mostrar_manos(jugador, dealer, ocultar_dealer=False)

    valor_jugador = calcular_valor(jugador)
    valor_dealer = calcular_valor(dealer)

    # Resultado
    if valor_dealer > 21 or valor_jugador > valor_dealer:
        print("¡Ganaste!")
    elif valor_jugador < valor_dealer:
        print("Perdiste.")
    else:
        print("Empate.")

# Iniciar juego
if __name__ == "__main__":
    jugar_blackjack()
