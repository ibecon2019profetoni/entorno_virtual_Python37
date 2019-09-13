"""
    TABLA DE MULTIPLICAR
    --------------------
    El usuario nos inserta un número entero y le printamos.
    La tabla de multiplicar de ese número.
"""
from imc import escenario_titulo


def tabla_multiplicar(tabla):
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(tabla, "*", i, "=", i * tabla)


if __name__ == "__main__":
    escenario_titulo('TABLA DE MULTIPLICAR')
    # usuario
    tabla = int(input('¿Qué tabla de múltiplicar necesita?: '))
    # respuesta
    tabla_multiplicar(tabla)
