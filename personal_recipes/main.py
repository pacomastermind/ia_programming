from ingredientes import buscar_ingrediente, leer_ingredientes
from platos import leer_platos, guardar_platos, platos

# Menu que interactua con el usuario y los platos
# Nuevo plato, listar platos, salir
def menu():
    while True:
        print("\nMenú de Platos:")
        print("1. Nuevo plato")
        print("2. Listar platos")
        print("3. Guardar platos")
        print("0. Salir")
        option = input("Elige una opción: ")

        if option == "1":
            nombre_plato = input("Nombre del plato: ")
            ingredientes = []
            while True:
                nombre_ingrediente = input("Nombre del ingrediente (o 'fin' para terminar): ")
                if nombre_ingrediente.lower() == 'fin':
                    break
                ingrediente = buscar_ingrediente(nombre_ingrediente)
                if ingrediente:
                    ingredientes.append(ingrediente)
                else:
                    print(f"Ingrediente '{nombre_ingrediente}' no encontrado.")
            platos[nombre_plato] = ingredientes
            guardar_platos()
            print(f"Plato '{nombre_plato}' añadido.")
        elif option == "2":
            print("\nLista de platos:")
            for nombre, ingredientes in platos.items():
                print(f"{nombre}: {', '.join([i[0] for i in ingredientes])}")
        elif option == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Para ejecutar el menú principal
if __name__ == "__main__":
    leer_ingredientes()  # Cargar los ingredientes al iniciar
    leer_platos()  # Cargar los platos al iniciar
    menu()  # Iniciar el menú de interacción con el usuario