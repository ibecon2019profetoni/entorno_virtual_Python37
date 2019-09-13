"""
    FORMATEAR NÚMERO TELÉFONO
    -------------------------
    usuario: 666112255 y pais
    (+34)666-112-255
    (+34)666 112 255
"""
from escenarios import escenario_titulo


prefijos_del_mundo = {
    'E': '+34',
    'I': '+39',
    'R': '+86'
}



def prefijo(pais):
    if pais == 'E':
        pass
    elif pais == 'I':
        pass
    elif pais == 'R':
        pass
    else:
        print('Pais no encontrado!')


def formatear(tel_usuario, pais_tel):
    # *Esto es un Comprehension
    numero = [i for i in tel_usuario]
    # *Comprobar el prefijo del pais
    format_pais = prefijo(pais_tel)
    # *Insertamos los nuevos carácteres
    numero.insert(0, f'({format_pais})')
    numero.insert(4, '-')
    numero.insert(8, '-')
    # *Cambiamos a cadena
    numero_cadena = ''.join(numero)
    # *Cambiamos los guiones por espacios
    numero_espacios = numero_cadena.replace('-', ' ')
    # *Visualizar el resultado
    print(''.join(numero))
    print(numero_espacios)


def run():
    escenario_titulo('F O R M A T E A R  N Ú M E R O  T E L É F O N O')
    # usuario
    tel_usuario = input('Introducir el número telefónico: ')
    pais_tel = input("[E]spaña [I]talia [R]usia : ")
    # resultado
    print('\n', '*' * 25, 'FORMATEADO', '*' * 25, '\n')
    # logica
    formatear(tel_usuario, pais_tel)


# *inicio script
if __name__ == "__main__":
    run()
