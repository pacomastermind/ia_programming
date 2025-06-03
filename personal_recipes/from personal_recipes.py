from personal_recipes.ingredientes import buscar_ingrediente, ingredientes

# Prueba ingrediente existente
resultado_existente = buscar_ingrediente('Manzana')
if resultado_existente == ['Manzana', 52.0, 0.3, 0.2, 14.0]:
    print("TEST ingrediente existente: OK")
else:
    print("TEST ingrediente existente: ERROR", resultado_existente)

# Prueba ingrediente no existente
resultado_no_existente = buscar_ingrediente('Platano')
if resultado_no_existente is None:
    print("TEST ingrediente no existente: OK")
else:
    print("TEST ingrediente no existente: ERROR", resultado_no_existente)