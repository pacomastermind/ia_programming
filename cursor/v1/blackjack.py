import random
import time

# Constantes
PALOS = ['♠', '♣', '♥', '♦']
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def crear_baraja():
    return [(valor, palo) for palo in PALOS for valor in VALORES]

def valor_carta(carta):
    valor = carta[0]
    if valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    return int(valor)

def calcular_puntos(mano):
    puntos = 0
    ases = 0
    
    for carta in mano:
        if carta[0] == 'A':
            ases += 1
        puntos += valor_carta(carta)
    
    # Ajustar el valor de los ases si es necesario
    while puntos > 21 and ases:
        puntos -= 10
        ases -= 1
    
    return puntos

def mostrar_mano(mano, ocultar_primera=False):
    cartas = []
    for i, carta in enumerate(mano):
        if i == 0 and ocultar_primera:
            cartas.append('🂠')
        else:
            cartas.append(f'{carta[0]}{carta[1]}')
    return ' '.join(cartas)

def jugar():
    print("\n¡Bienvenido al Blackjack!")
    
    # Inicializar baraja y mezclar
    baraja = crear_baraja()
    random.shuffle(baraja)
    
    # Repartir cartas iniciales
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_dealer = [baraja.pop(), baraja.pop()]
    
    while True:
        # Mostrar las manos
        print(f"\nTu mano: {mostrar_mano(mano_jugador)} ({calcular_puntos(mano_jugador)} puntos)")
        print(f"Mano del dealer: {mostrar_mano(mano_dealer, True)}")
        
        # Verificar si el jugador tiene Blackjack
        if calcular_puntos(mano_jugador) == 21:
            print("¡Blackjack! ¡Has ganado!")
            return
        
        # Turno del jugador
        accion = input("\n¿Quieres otra carta? (s/n): ").lower()
        
        if accion == 's':
            nueva_carta = baraja.pop()
            mano_jugador.append(nueva_carta)
            puntos = calcular_puntos(mano_jugador)
            
            if puntos > 21:
                print(f"\nTu mano: {mostrar_mano(mano_jugador)} ({puntos} puntos)")
                print("¡Te has pasado! Has perdido.")
                return
        else:
            break
    
    # Turno del dealer
    print(f"\nMano del dealer: {mostrar_mano(mano_dealer)} ({calcular_puntos(mano_dealer)} puntos)")
    
    while calcular_puntos(mano_dealer) < 17:
        time.sleep(1)
        nueva_carta = baraja.pop()
        mano_dealer.append(nueva_carta)
        print(f"El dealer toma una carta: {mostrar_mano(mano_dealer)} ({calcular_puntos(mano_dealer)} puntos)")
    
    # Determinar el ganador
    puntos_jugador = calcular_puntos(mano_jugador)
    puntos_dealer = calcular_puntos(mano_dealer)
    
    print(f"\nTus puntos: {puntos_jugador}")
    print(f"Puntos del dealer: {puntos_dealer}")
    
    if puntos_dealer > 21:
        print("¡El dealer se ha pasado! ¡Has ganado!")
    elif puntos_jugador > puntos_dealer:
        print("¡Has ganado!")
    elif puntos_jugador < puntos_dealer:
        print("El dealer gana.")
    else:
        print("¡Empate!")

def main():
    while True:
        jugar()
        if input("\n¿Quieres jugar otra vez? (s/n): ").lower() != 's':
            break
    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    main() 