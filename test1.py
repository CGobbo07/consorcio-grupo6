# Creacion de listas
unidades = []
superficies = []
CANTIDAD = 20

# Ingreso de datos: valor metro cuadrado
valor_m2 = float(input("Ingrese el valor de gasto por metro cuadrado: "))

# Ingreso de datos
print("Ingrese los datos de las unidades:")
i = 0
while i < CANTIDAD:
    nro = int(input(f"Unidad #{i+1} - Ingrese numero de unidad: "))
    if nro in unidades:
        print("Numero de unidad ya ingresado. Ingrese otro.")
        continue
    sup = float(input("Ingrese la superficie en m2: "))

    unidades.append(nro)
    superficies.append(sup)
    i += 1

# Calcular los gastos
gastos = [superficies[i] * valor_m2 for i in range(CANTIDAD)]
promedio = sum(gastos) / CANTIDAD
print(f"\nPromedio de gastos del mes: ${promedio:.2f}")

# Ordenar de forma descendente
for i in range(CANTIDAD - 1):
    for j in range(i + 1, CANTIDAD):
        if superficies[i] < superficies[j]:
            superficies[i], superficies[j] = superficies[j], superficies[i]
            unidades[i], unidades[j] = unidades[j], unidades[i]

# Mostrar datos ordenados
print("\nListado ordenado por superficie (mayor a menor):")
for i in range(CANTIDAD):
    print(f"Unidad {unidades[i]} - Superficie: {superficies[i]} m2")
