"""
    App que pida el peso (en kilogramos) y la altura (en metros).
    De una persona y que calcule su índice de masa corporal (imc).
    El imc se calcula con la fórmula imc = peso / altura
"""
import os
import time


def imc(peso, altura):
    calculo = peso / altura**2
    # calculo = peso / pow(altura, 2)
    # calculo = peso / (altura * altura)
    return calculo


def escenario_titulo(titulo):
    os.system('clear')
    # * Preguntas para el usuario
    print(titulo)
    print('=' * 50, '\n')


# *inicio de script
if __name__ == "__main__":
    escenario_preguntaYrespuesta_usuario(
        "CÁLCULO DE ÍNDICE DE MASA CORPORAL (IMC)")

    peso = float(input('¿Cuál es su peso?: '))
    altura = float(input('¿Cuál es su altura?: '))

    # * Resultado para el usuario
    print('?' * 50)
    time.sleep(2)
    # resolucion del imc
    print(f'Su imc es {imc(peso, altura)}')
    print('Un imc muy ato le puedo provocar problemas coronarios')
    print('Entre 20 y 25, es el límite')
