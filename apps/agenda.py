"""
    AGENDA 11 PRO
    -------------
    v1.0 (datos en memoria)
    v2.0 (datos en disco)
"""
import os

# * *****************************
# * ******* CLASES
# * *****************************


class Ficha:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class Agenda:
    # *constructor
    def __init__(self):
        self._contactos = []

    # *métodos
    # añadir contacto
    def nuevo(self, name, phone, email):
        # el nuevo objeto contacto
        contacto = Ficha(name, phone, email)
        # añadir introducción de datos del usuario a la lista
        self._contactos.append(contacto)
        print("""
                Contacto añadido correctamente
        """)

    # mostrar todos los contactos
    def mostrar_todo(self):
        for contacto in self._contactos:
            # como imprimir los contactos en pantalla
            self._mostrar(contacto)

    def _mostrar(self, contacto):
        print('--- * ----' * 10)
        print('Nombre: {}'.format(contacto.name))
        print('Teléfono: {}'.format(contacto.phone))
        print(f'Email: {contacto.email}')
        print('--- * ----' * 10)

    def borrar(self, name):
        for idx, contacto in enumerate(self._contactos):
            if contacto.name.lower() == name.lower():
                del self._contactos[idx]
                break

    def buscar(self, name):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                self._mostrar(contacto)
                break
        else:
            self._no_encontrado()

    # Actualizar contacto

    def actualizar(self, name, phone, email):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                contacto.phone = phone
                contacto.email = email
                break
        else:
            self._no_encontrado()

        print("""
                Actualización correcta
        """)

    def _no_encontrado(self):
        print('*' * 30)
        print('¡NO encontrado!')
        print('*' * 30)

# * *****************************
# * ******* FUNCIONES
# * *****************************


def run():
    # limpiar terminal
    os.system('clear')
    # crear objeto
    agenda_de_toni = Agenda()
    # bucle infinito
    while True:
        # menu para el usuario
        print(f'B I E N V E N I D O  A  LA  A G E N D A  DE  T O N I')
        menu = input("""

                ¿Qué quieres hacer ahora?

                [a]ñadir contacto
                [ac]tualizar contacto
                [b]uscar contacto
                [e]liminar contacto
                [l]istar contactos
                    [s]alir

        """)

        # Si el usuario pulsa la a de Añadir contacto
        if menu.lower() == 'a':
            # Se le piden los datos necesarios al usuario
            nombre = input('Escribe el nombre de contacto: ')
            telefono = input('Escribe el telelfono de contacto: ')
            email = input('Escribe el email de contacto: ')
            # Se llama al método de añadir contacto
            agenda_de_toni.nuevo(nombre, telefono, email)

        # Si el usuario pulsa la ac de Actualizar contacto
        if menu.lower() == 'ac':
            # Se le piden los datos necesarios al usuario
            nombre = input('Escribe el nombre de contacto: ')
            telefono = input('Escribe el telelfono de contacto: ')
            email = input('Escribe el email de contacto: ')
            # Se llama al método de añadir contacto
            agenda_de_toni.actualizar(nombre, telefono, email)

        # Si el usuario pulsa la b de buscar contacto
        elif menu.lower() == 'b':
            nombre = input('Escribe el nombre de contacto: ')

            # Se llama al método de buscar contacto
            agenda_de_toni.buscar(nombre)

        # Si el usuario pulsa la e de borrar contacto
        elif menu.lower() == 'e':
            nombre = input('Escribe el nombre de contacto: ')

            # Se llama al método de buscar contacto
            agenda_de_toni.borrar(nombre)

        # Si el usuario pulsa la l de Añadir contacto
        elif menu.lower() == 'l':
            # Se llama al método de mostrar todos los contacto
            agenda_de_toni.mostrar_todo()

        # Si el usuario pulsa la s de salir de la app
        elif menu.lower() == 's':
            break
            # el usuario a introducido una opción que no existe
        else:
            print('Comando no encontrado. Vuelva a intentarlo')


# * *****************************
# * ******* INICIO DE SCRIPT
# * *****************************
if __name__ == "__main__":
    run()
