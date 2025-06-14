# Programa con las funciones incluidas, sin tabulate ni librerias importadas

def pedir_num_entero(mensaje):
    num = input(mensaje)
    while not num.isdigit() or int(num)<= 0:
        print("Debe ingresar un número mayor a 0.")
        num = input(mensaje)
    return int(num)

def pedir_num_decimal(mensaje): 
    es_dato_valido = False
    while not es_dato_valido:
        valor_ingresado = input(mensaje)
        
        try:
            numero = float(valor_ingresado)
            if numero > 0:
                es_dato_valido = True
                resultado = numero
            else:
                print("Debe ingresar un número mayor a 0.")
        except ValueError:
            print("Debe ingresar un número mayor a 0.")
    
    return resultado

def ingresar_datos(cantidad_unidades):
    lista_unidades = []
    lista_superficies = []
    i = 0
    while i < cantidad_unidades:
        numero = pedir_num_entero(f"Unidad #{i+1} - Ingrese número de unidad: ")
        if numero in lista_unidades:
            print("Número de unidad ya ingresado. Ingrese otro.")
            continue
        superficie = pedir_num_decimal("Ingrese la superficie en m2: ")
        lista_unidades.append(numero)
        lista_superficies.append(superficie)
        i += 1
    return lista_unidades, lista_superficies


def calcular_promedio(lista_superficies, valor_metro2):
    lista_gastos = [sup * valor_metro2 for sup in lista_superficies]
    promedio_gastos = sum(lista_gastos) / len(lista_superficies)
    return promedio_gastos, lista_gastos


def ordenar_descendente(lista_unidades, lista_superficies, lista_gastos):
    for i in range(len(lista_superficies) - 1):
        for j in range(i + 1, len(lista_superficies)):
            if lista_superficies[i] < lista_superficies[j]:
                lista_superficies[i], lista_superficies[j] = lista_superficies[j], lista_superficies[i]
                lista_unidades[i], lista_unidades[j] = lista_unidades[j], lista_unidades[i]
                lista_gastos[i], lista_gastos[j] = lista_gastos[j], lista_gastos[i]
    return lista_unidades, lista_superficies, lista_gastos


def ordenar_ascendente(lista_unidades, lista_superficies, lista_gastos):
    for i in range(len(lista_superficies) - 1):
        for j in range(i + 1, len(lista_superficies)):
            if lista_superficies[i] > lista_superficies[j]:
                lista_superficies[i], lista_superficies[j] = lista_superficies[j], lista_superficies[i]
                lista_unidades[i], lista_unidades[j] = lista_unidades[j], lista_unidades[i]
                lista_gastos[i], lista_gastos[j] = lista_gastos[j], lista_gastos[i]
    return lista_unidades, lista_superficies, lista_gastos


def mostrar_tabla(lista_unidades, lista_superficies, lista_gastos, titulo_tabla):
    print("\n" + "=" * 70)
    print(f"{titulo_tabla.center(70)}")
    print("=" * 70)
    print(f"+{'-'*10}+{'-'*20}+{'-'*20}+")
    print(f"| {'Unidad':<8} | {'Superficie (m2)':>18} | {'Gasto mensual':>18} |")
    print(f"+{'-'*10}+{'-'*20}+{'-'*20}+")
    for i in range(len(lista_unidades)):
        print(
            f"| {lista_unidades[i]:<8} | {lista_superficies[i]:>18.2f} | ${lista_gastos[i]:>17.2f} |")
    print(f"+{'-'*10}+{'-'*20}+{'-'*20}+")


if __name__ == "__main__":
    cantidad_unidades = pedir_num_entero("Ingrese la cantidad de departamentos. Máximo 20: ")
    while cantidad_unidades <= 0 or cantidad_unidades > 20:
        cantidad_unidades = pedir_num_entero("Ingrese la cantidad de departamentos, tiene que ingresar un número mayor a 0. Máximo 20: ")
    valor_metro2 = pedir_num_decimal("Ingrese el valor de gasto por metro cuadrado: ")
    lista_unidades, lista_superficies = ingresar_datos(cantidad_unidades)
    promedio_gastos, lista_gastos = calcular_promedio(
        lista_superficies, valor_metro2)
    print(f"\nPromedio de gastos del mes: ${promedio_gastos:.2f}")

    # Orden descendente
    unidades_desc, superficies_desc, gastos_desc = ordenar_descendente(
        lista_unidades.copy(), lista_superficies.copy(), lista_gastos.copy()
    )
    mostrar_tabla(unidades_desc, superficies_desc,
                  gastos_desc, "Ordenado de mayor a menor")

    # Orden ascendente
    unidades_asc, superficies_asc, gastos_asc = ordenar_ascendente(
        lista_unidades.copy(), lista_superficies.copy(), lista_gastos.copy()
    )
    mostrar_tabla(unidades_asc, superficies_asc,
                  gastos_asc, "Ordenado de menor a mayor")
