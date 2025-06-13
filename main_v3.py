# Programa con librerias importadas, libreria tabulate
from tabulate import tabulate

def pedir_num_entero(mensaje):
    num = input(mensaje)
    while not num.isdigit():
        print("Debe ingresar un número entero positivo.")
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

def ingresar_datos(cantidad):
    unidades = []
    superficies = []
    i = 0
    while i < cantidad:
        nro = pedir_num_entero(f"Unidad #{i+1} - Ingrese numero de unidad: ")
        if nro in unidades:
            print("Numero de unidad ya ingresado. Ingrese otro.")
            continue
        sup = pedir_num_decimal("Ingrese la superficie en m2: ")
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


def mostrar_tabla(unidades, superficies):
    tabla = list(zip(unidades, superficies))
    headers = ["Unidad", "Superficie (m2)"]
    print(tabulate(tabla, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    cantidad = pedir_num_entero("Ingrese la cantidad de departamentos (máximo 20): ")
    while cantidad <= 0 or cantidad > 20:
        cantidad = pedir_num_entero("Ingrese la cantidad de departamentos, tiene que ingresar un número mayor a 0. Máximo 20: ")
    valor_m2 = pedir_num_decimal("Ingrese el valor de gasto por metro cuadrado: ")
    unidades, superficies = ingresar_datos(cantidad)
    promedio, gastos = calcular_promedio(superficies, valor_m2)
    print(f"\nPromedio de gastos del mes: ${promedio:.2f}")
    unidades, superficies = ordenar_descendente(unidades, superficies)
    mostrar_tabla(unidades, superficies)
