def ingresar_datos(cantidad):
    unidades = []
    superficies = []
    i = 0
    while i < cantidad:
        nro = int(input(f"Unidad #{i+1} - Ingrese numero de unidad: "))
        if nro in unidades:
            print("Numero de unidad ya ingresado. Ingrese otro.")
            continue
        sup = float(input("Ingrese la superficie en m2: "))
        unidades.append(nro)
        superficies.append(sup)
        i += 1
    return unidades, superficies


def calcular_promedio(superficies, valor_m2):
    gastos = [sup * valor_m2 for sup in superficies]
    promedio = sum(gastos) / len(superficies)
    return promedio, gastos


def ordenar_descendente(unidades, superficies):
    for i in range(len(superficies) - 1):
        for j in range(i + 1, len(superficies)):
            if superficies[i] < superficies[j]:
                superficies[i], superficies[j] = superficies[j], superficies[i]
                unidades[i], unidades[j] = unidades[j], unidades[i]
    return unidades, superficies


def ordenar_ascendente(unidades, superficies):
    for i in range(len(superficies) - 1):
        for j in range(i + 1, len(superficies)):
            if superficies[i] > superficies[j]:
                superficies[i], superficies[j] = superficies[j], superficies[i]
                unidades[i], unidades[j] = unidades[j], unidades[i]
    return unidades, superficies


def mostrar_tabla(unidades, superficies, titulo):
    print(f"\n{titulo}")
    print(f"{'Unidad':<10} {'Superficie (m2)':>20}")
    print("-" * 30)
    for i in range(len(unidades)):
        print(f"{unidades[i]:<10} {superficies[i]:>20.2f}")


if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad de departamentos: "))
    valor_m2 = float(input("Ingrese el valor de gasto por metro cuadrado: "))
    unidades, superficies = ingresar_datos(cantidad)
    promedio, gastos = calcular_promedio(superficies, valor_m2)
    print(f"\nPromedio de gastos del mes: ${promedio:.2f}")

    # Mostrar descendente
    unidades_desc, superficies_desc = ordenar_descendente(
        unidades.copy(), superficies.copy())
    mostrar_tabla(unidades_desc, superficies_desc,
                  "Listado ordenado por superficie (mayor a menor):")

    # Mostrar ascendente
    unidades_asc, superficies_asc = ordenar_ascendente(
        unidades.copy(), superficies.copy())
    mostrar_tabla(unidades_asc, superficies_asc,
                  "Listado ordenado por superficie (menor a mayor):")
