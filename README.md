# :department_store: Administradora de Consorcios – Sistema de Cálculo de Expensas :department_store:

## Descripción

Este proyecto implementa un sistema sencillo en [Python](https://www.python.org/) para una administradora de consorcios que gestiona las expensas de un edificio de 20 departamentos.

Permite ingresar los números de unidad y sus superficies, calcula el gasto mensual de expensas según el valor del metro cuadrado, informa el promedio general y presenta un listado ordenado de mayor a menor según la superficie de cada unidad.

## Funcionalidades principales

- :white_check_mark: Ingreso de datos validados (sin duplicados).

- :white_check_mark: Cálculo automático de gasto mensual por unidad.

- :white_check_mark: Cálculo del promedio general de gastos.

- :white_check_mark: Ordenamiento manual descendente por superficie usando método burbuja.

- :white_check_mark: Visualización clara de resultados en consola.

## Conceptos técnicos implementados

- Estructuras de datos: listas paralelas (`unidades`, `superficies`).

- Estructuras de control: bucles `while`, `for`.

- Validación de datos con `if`.

- Operaciones matemáticas sobre listas (cálculo de gastos y promedios).

- Algoritmo de ordenamiento manual (burbuja).

- Salida formateada en consola (`print` con decimales).

## :hammer_and_wrench: Requisitos :hammer_and_wrench:

- Python 3.9.6

## Estructura del proyecto

En la rama `main` se encuentra la versión final del proyecto que tiene la siguiente estructura:

| Programa   |                                                     |
| ---------- | --------------------------------------------------- |
| main_v1.py | Programa en python                                  |
| README.md  | Archivo con instrucciones y guia de usuario         |
| utils.py   | Funciones auxiliares para el desarrollo de programa |

En la rama `test` se incluyen tres versiones en las cuales resolvimos el programa.

### Manual de uso

1. Clonar el repositorio o descargar los archivos.

2. Ejecutar el programa

- `python main_v1.py`

3. Cargar los datos y correr el programa

4. Para ver las diferentes versiones cambiar de rama con `git checkout test`.

5. En la rama `test`, es necesario para el archivo `main_v3.py` agregar las dependencias externas:

- `pip install -r requerimientos.txt`

6. Elegir la versión a probar.

### Autores: Grupo 8

- Gobbo Carlos Lautaro
- Ejarque Sasha Armin
- Kidyba Lautaro Agustin
- Cairo Mariana
