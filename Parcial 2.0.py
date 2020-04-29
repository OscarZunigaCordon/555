listaClientes = []
listaProyecto = []
listaDepaMuni = []
import os
import sys

def clear():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

############################## GESTION DE CLIENTES #############################

def ingresarCliente(Codigo, Nombre, Direccion, Telefono):
    listaClientes.append([Codigo, Nombre, Direccion, Telefono])
    print("Cliente Ingresado Con Exito")

def mostrarclientes():
    listaClientes.sort()
    print("\n".join(i[0] + " - " + str(i[1]) + " - " + str(i[2]) + " - " + str(i[3]) for i in listaClientes))
    os.system("PAUSE")
    clear()


def menuClientes():
    opcion = 0

    while opcion != 8:
        print("GESTION DE CLIENTES")
        print("1. Registrar Clientes")
        print("2. Mostrar Clientes")
        print("3. Regresar al Menu principal")
        opcion = int(input("Digite Opcion:"))
        clear()

        if opcion == 1:
            print("PORFAVOR INGRESAR LOS DATOS DEL CLIENTE")
            Codigo = input("Ingrese El Codigo:   ")
            Nombre = input("Ingrese el Nombre  ")
            Direccion = input("Ingrese la Direccion  ")
            Telefono = input("Ingrese la Telefono  ")
            ingresarCliente(Codigo, Nombre, Direccion, Telefono)
            os.system("PAUSE")
            clear()

        elif opcion == 2:
            print(mostrarclientes())

        elif opcion == 3:
            menu()

############################## GESTION DE DEPARTAMENTOS Y MUNICIPIOS #############################

def ingresarLugar(Codigo, Depa, Muni):
    listaDepaMuni.append([Codigo, Depa, Muni])
    print("Lugar Ingresado Con Exito")

def mostrarLugar():
    listaDepaMuni.sort()
    print("-------------------------------------------------------")
    print("\n".join(i[0] + " - " + str(i[1]) + " - " + str(i[2]) for i in listaDepaMuni))
    os.system("PAUSE")
    clear()



def menuLugar():
    opcion = 0

    while opcion != 8:
        print("GESTION DE DEPARTAMENTOS Y MUNICIPIOS")
        print("1. Registrar Departamentos y Municipios")
        print("2. Mostrar Lugares")
        print("3. Regresar al Menu principal")
        opcion = int(input("Digite Opcion:"))
        clear()

        if opcion == 1:
            print("PORFAVOR INGRESAR LOS DATOS")
            Codigo = input("Ingrese el Numero de Departamento:   ")
            Depa = input("Ingrese el Nombre del Departamento:   ")
            Muni = input("Ingrese el Nombre del Municipio:   ")
            ingresarLugar(Codigo, Depa, Muni)
            os.system("PAUSE")
            clear()

        elif opcion == 2:
            print(mostrarLugar())

        elif opcion == 3:
            menu()

############################## GESTION DE PROYECTOS #############################

def ingresarProyecto(Codigo, Descripcion, Fecha, Estado):
    listaProyecto.append([Codigo, Descripcion, Fecha, Estado])
    print("Proyecto Ingresado Con Exito")

def mostrarProyecto():
    listaProyecto.sort()
    print("\n".join(i[0] + " - " + str(i[1]) + " - " + str(i[2]) + " - " + str(i[3]) for i in listaProyecto))
    os.system("PAUSE")
    clear()


def menuProyectos():
    opcion = 0

    while opcion != 8:
        print("GESTION DE PROYECTOS")
        print("1. Registrar Proyecto")
        print("2. Mostrar Proyectos")
        print("3. Regresar al Menu principal")
        opcion = int(input("Digite Opcion:"))
        clear()

        if opcion == 1:
            print("PORFAVOR INGRESAR LOS DATOS DEL PROYECTO")
            Codigo = input("Ingrese el Codigo:   ")
            Descripcion = input("Ingrese la Descripcion:   ")
            Fecha = input("Ingrese la Fecha:   ")
            Estado = "Activo"
            ingresarProyecto(Codigo, Descripcion, Fecha, Estado)
            os.system("PAUSE")
            clear()

        elif opcion == 2:
            print(mostrarProyecto())

        elif opcion == 3:
            menu()


def menu():
    opcion = 0

    while opcion != 4:

        print("1. Gestion de Clientes")
        print("2. Gestion de Departamentos y Municipios")
        print("3. Gestion de Proyectos")
        print("4. Salir del Programa")
        opcion = int(input("Digite Opcion:"))
        clear()

        if opcion == 1:
            menuClientes()
            os.system("PAUSE")
            clear()

        elif opcion == 2:
            menuLugar()
            os.system("PAUSE")
            clear()

        elif opcion == 3:
            menuProyectos()
            os.system("PAUSE")
            clear()

        elif opcion == 4:
            print("USTED HA SALIDO DEL PROGRAMA")
            sys.exit()


menu()




