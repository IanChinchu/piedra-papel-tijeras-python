# Pedir nombres de los jugadores
nombre1 = input("Player 1, como te llamas? ")
nombre2 = input("Player 2, como te llamas? ")

# Jugar 3 turnos
for turno in range(1, 4):
    print(f"\nTurno {turno}:")
    
    # Pedir elección de los jugadores
    jugador1 = input(f"{nombre1}, elegí: Piedra, Papel o Tijeras?: ").lower()
    jugador2 = input(f"{nombre2}, elegí: Piedra, Papel o Tijeras?: ").lower()
    
    # Condiciones para ganar
    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
    
    # Evaluar el resultado del turno
    if jugador1 == jugador2:
        print("Empate!")
    elif condicion1 or condicion2 or condicion3:
        print(f"Ganó {nombre1} este turno!")
    else:
        print(f"Ganó {nombre2} este turno!")

# Mensaje final
print("\n¡El juego de 3 turnos ha terminado!")
