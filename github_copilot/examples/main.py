aliments = [
    {"name": "Apple", "calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2},
    {"name": "Banana", "calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3},
    {"name": "Carrot", "calories": 41, "protein": 0.9, "carbs": 10, "fat": 0.2},
    {"name": "Doughnut", "calories": 452, "protein": 4.3, "carbs": 51, "fat": 25.2},
    {"name": "Egg", "calories": 155, "protein": 13, "carbs": 1.1, "fat": 11},
]

# Menu interact with the user to select an aliment
def menu():

    print("Select an aliment:")
    for i, aliment in enumerate(aliments):
        print(f"{i + 1}. {aliment['name']} - {aliment['calories']} calories")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 0:
        return None
    elif 1 <= choice <= len(aliments):
        return aliments[choice - 1]
    else:
        print("Invalid choice, please try again.")
        return menu()

        def main_menu():
            while True:
                print("\nMain Menu:")
                print("1. Nuevo alimento")
                print("2. Listar alimentos")
                print("3. Nuevo plato")
                print("0. Salir")
                option = input("Elige una opción: ")

                if option == "1":
                    name = input("Nombre del alimento: ")
                    calories = float(input("Calorías: "))
                    protein = float(input("Proteína: "))
                    carbs = float(input("Carbohidratos: "))
                    fat = float(input("Grasas: "))
                    aliments.append({
                        "name": name,
                        "calories": calories,
                        "protein": protein,
                        "carbs": carbs,
                        "fat": fat
                    })
                    print(f"Alimento '{name}' añadido.")
                elif option == "2":
                    print("\nLista de alimentos:")
                    for aliment in aliments:
                        print(f"{aliment['name']} - {aliment['calories']} cal, {aliment['protein']}g proteína, {aliment['carbs']}g carbs, {aliment['fat']}g grasa")
                elif option == "3":
                    print("Funcionalidad de 'Nuevo plato' aún no implementada.")
                elif option == "0":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        # Para ejecutar el menú principal
        if __name__ == "__main__":
            main_menu()