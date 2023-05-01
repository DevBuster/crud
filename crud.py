# Importamos la biblioteca PrettyTable
from prettytable import PrettyTable
import os
import random

# Creamos una tabla vacía con las columnas que deseamos mostrar
tabla = PrettyTable(['ID', 'Nombre', 'Edad', 'Sexo', 'Teléfono', 'Correo electrónico'])

# Definimos la variable id y le asignamos un valor inicial
id = 1

# Creamos una carpeta para almacenar los archivos
if not os.path.exists('personas'):
    os.makedirs('personas')

def generarDatosAleatorios(n):
    """
    Esta función toma como argumento el número n de datos aleatorios que deseas generar. Esta funcion genera nombres, 
    edades, sexos, teléfonos y correos electrónicos aleatorios para cada persona utilizando las funciones random.choice y 
    random.randint del módulo random. Luego, se agrega la información a la tabla y se escribe en un archivo de texto. 
    Puedes llamar a esta función con n=100 para generar 100 datos aleatorios o cualquier dato cambiando el rango n:
    """

    global id
    nombres = ['Juan', 'Pedro', 'María', 'Ana', 'Carlos', 'Lucía', 'Miguel', 'Sofía', 'Javier', 'Laura']
    sexos = ['Masculino', 'Femenino']

    for i in range(n):

        # Creamos un diccionario vacío para almacenar la información de la persona
        persona = {}

        # Generamos información aleatoria para la persona
        persona['id'] = str(id).zfill(2) # zfill para agregar ceros a la izquierda del ID
        persona['nombre'] = str(random.choice(nombres))
        persona['edad'] = random.randint(18, 80)
        persona['sexo'] = str(random.choice(sexos))
        persona['telefono'] = int(''.join([str(random.randint(0, 9)) for _ in range(10)]))
        persona['correo'] = persona['nombre'].lower() + str(random.randint(1, 100)) + '@ejemplo.com'

        # Agregamos la información a la tabla
        tabla.add_row([persona['id'], persona['nombre'], persona['edad'], persona['sexo'], persona['telefono'], persona['correo']])
        
        # Incrementamos el ID para la siguiente persona
        id += 1

        # Escribimos los datos del diccionario en un archivo
        with open('personas/' + str(persona['id']).zfill(2) + '.txt', 'w') as archivo:
            for clave, valor in persona.items():
                archivo.write(clave + ': ' + str(valor) + '\n')

generarDatosAleatorios(50)

# agregar informacion
def agregarInformacion():

    global id
    # Creamos un diccionario vacío para almacenar la información de la persona
    persona = {}

    while True:
        try:
            # Solicitamos al usuario que ingrese información sobre la persona
            persona['id'] = str(id).zfill(1)
            persona['nombre'] = str(input("Ingrese el nombre: "))
            persona['edad'] = int(input("Ingrese la edad: "))
            persona['sexo'] = str(input("Ingrese el sexo: "))
            persona['telefono'] = int(input("Ingrese el teléfono: "))
            persona['correo'] = input("Ingrese el correo electrónico: ")

            # Agregamos la información a la tabla
            tabla.add_row([persona['id'], persona['nombre'], persona['edad'], persona['sexo'], persona['telefono'], persona['correo']])

            # Incrementamos el ID para la siguiente persona
            id += 1

            # Escribimos los datos del diccionario en un archivo
            with open('personas/' + str(persona['id']).zfill(2) + '.txt', 'w') as archivo:
                for clave, valor in persona.items():
                    archivo.write(clave + ': ' + str(valor) + '\n')
            break
        except:
            print("\nAlgo salió mal, verifique que los datos esten bien diligenciados\n")

# ver la informacion de todos los ficheros
def verInformacion():

    global id

    # Limpiamos la tabla para evitar duplicados
    tabla.clear_rows()
    
    # Leemos los datos del archivo y los agregamos a la tabla
    id = 1

    # Leemos los datos del archivo y los agregamos a la tabla
    for archivo in os.listdir('personas'):
        with open('personas/' + archivo, 'r') as archivo_lectura:
            persona = {}
            for linea in archivo_lectura:
                clave, valor = linea.strip().split(': ')
                persona[clave] = valor
            tabla.add_row([persona['id'], persona['nombre'], persona['edad'], persona['sexo'], persona['telefono'], persona['correo']])

            id += 1
    
    # Imprimimos la tabla en la consola
    print("\n", tabla,  "\n")

# ver la informacion de un fichero en especifico
def verInformacionEspecifica():

    # Solicitamos al usuario que ingrese el id de la persona que desea ver
    id_persona = input("\nIngrese el id de la persona que desea ver: \n")

    # Verificamos si existe un archivo con el id de la persona
    if os.path.exists('personas/' + str(id_persona) + '.txt'):
        # Leemos los datos del archivo y los imprimimos en la consola
        with open('personas/' + str(id_persona) + '.txt', 'r') as archivo_lectura:
            print(archivo_lectura.read())
    else:
        print("No se encontró a la persona.")

# actualizar la informacion de un fichero en especifico
def actualizarInformacion():

    try:
        # Solicitamos al usuario que ingrese el id de la persona que desea actualizar
        id_persona = input("\nIngrese el id de la persona que desea actualizar: \n")

        # Verificamos si existe un archivo con el id de la persona
        if os.path.exists('personas/' + str(id_persona) + '.txt'):
            # Creamos un diccionario vacío para almacenar la información de la persona
            persona = {}

            # Solicitamos al usuario que ingrese la nueva información sobre la persona
            persona['id'] = str(id_persona)
            persona['nombre'] = str(input("Ingrese el nuevo nombre: "))
            persona['edad'] = int(input("Ingrese la nueva edad: "))
            persona['sexo'] = str(input("Ingrese el nuevo sexo: "))
            persona['telefono'] = input("Ingrese el nuevo teléfono: ")
            persona['correo'] = input("Ingrese el nuevo correo electrónico: ")

            # Escribimos los datos del diccionario en un archivo
            with open('personas/' + str(id_persona) + '.txt', 'w') as archivo:
                for clave, valor in persona.items():
                    archivo.write(clave + ': ' + str(valor) + '\n')
        else:
            print("\nNo se encontró a la persona.\n")
    except:
        print("\nAlgo salió mal, verifique que los datos esten bien diligenciados\n")

# eliminar infomacion de un fichero en especifico
def eliminarInformacion():

    # Solicitamos al usuario que ingrese el id de la persona que desea eliminar
    id_persona = input("\nIngrese el id de la persona que desea eliminar: ")

    # Verificamos si existe un archivo con el id de la persona
    if os.path.exists('personas/' + str(id_persona) + '.txt'):
        # Eliminamos el archivo
        os.remove('personas/' + str(id_persona) + '.txt')
    else:
        print("No se encontró a la persona.")

def eliminarTodo():
    for archivo in os.listdir('personas'):
        os.remove('personas/' + archivo)

while True:

    # Mostramos el menú de opciones al usuario
    print("1. Agregar información")
    print("2. Ver información")
    print("3. Ver información de una persona en específica")
    print("4. Actualizar información")
    print("5. Eliminar información")
    print("6. Eliminar toda la infomacion")
    print("7. Salir")
    
    try:
        # Solicitamos al usuario que elija una opción
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            agregarInformacion()
        elif opcion == 2:
            verInformacion()
        elif opcion == 3:
            verInformacionEspecifica()
        elif opcion == 4:
            actualizarInformacion()
        elif opcion == 5:
            eliminarInformacion()
        elif opcion == 6:
            eliminarTodo()
        elif opcion == 7:
            break
        else:
            print("\nEl numero que ingresó esta fuera de rango\n")
    except:
        print("\nSolo se permite entradas numericas, vuelva a intentar\n")