import json
platos ={}

#Funcion que abre el fichero platos.json
#Si no existe lo crea
def leer_platos():
    try:
        with open('platos.json', 'r', encoding='utf-8') as file:
            global platos
            platos = json.load(file)
    except FileNotFoundError:
        with open('platos.json', 'w', encoding='utf-8') as file:
            json.dump({}, file)
            platos = {}

#Funcion que guarda todos los platos en el fichero platos.json
def guardar_platos():
    with open('platos.json', 'w', encoding='utf-8') as file:
        json.dump(platos, file, indent=4, ensure_ascii=False)