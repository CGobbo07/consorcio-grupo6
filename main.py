# Programa Final
from utils import (
    ingresar_datos,
    calcular_promedio,
    ordenar_descendente,
    ordenar_ascendente,
    mostrar_tabla,
)

if __name__ == "__main__":
    cantidad_unidades = int(input("Ingrese la cantidad de departamentos: "))
    valor_metro2 = float(
        input("Ingrese el valor de gasto por metro cuadrado: "))

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
