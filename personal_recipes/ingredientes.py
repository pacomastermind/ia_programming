import csv
ingredientes = {}

#Funcion que lee fichero ingredientes_comunes_nutricionales.csv
#y lo almacena en un diccionario
def leer_ingredientes():
    with open('ingredientes_comunes_nutricionales.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nombre = row['nombre']
            calorias = float(row['calorias'])
            proteinas = float(row['proteinas'])
            grasas = float(row['grasas'])
            carbohidratos = float(row['carbohidratos'])
            ingredientes[nombre] = {
                'calorias': calorias,
                'proteinas': proteinas,
                'grasas': grasas,
                'carbohidratos': carbohidratos
            }  

#Funcion que busca un ingrediente por nombre
#y devuelve una lista del resultado
def buscar_ingrediente(nombre):
    if nombre in ingredientes:
        return [nombre, ingredientes[nombre]['calorias'], 
                ingredientes[nombre]['proteinas'], 
                ingredientes[nombre]['grasas'], 
                ingredientes[nombre]['carbohidratos']]
    else:
        return None
