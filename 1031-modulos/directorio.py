import csv
import os

# Nombre de los archivos para abrir
ARCHIVO_DIRECTORIO="directorio.csv"

def mostrar():
    archivo = open(ARCHIVO_DIRECTORIO,"r")
    lector = csv.reader(archivo)
    contador = 1
    print("----  Directorio ----------")
    print("{:<5s}{:<30s}{:>15s} {:<30s}".format("No.", "Nombre", "Telefono", "Dirección"))
    for fila in lector:
        if fila[0] == "Nombre":
            continue
        print("{:<5d}{:<30s}{:>16s} {:<30s}".format(contador, fila[0], fila[1], fila[2]))
        contador = contador + 1
    archivo.close()


def agregar ():
    nombre = input("Escrie el nombre: ")
    telefono = input("Escribe el telefono: ")
    direccion = input("Escribe la dirección: ")
    archivo = open(ARCHIVO_DIRECTORIO,"a")
    archivo.write(nombre + ", " + telefono + ", "+ direccion + "\n")
    archivo.close()


def borrar(numero):
    archivo = open(ARCHIVO_DIRECTORIO,"r")
    archivo_temporal = open("temporal.csv","w", newline="")

    lector = csv.reader(archivo)
    escritor = csv.writer(archivo_temporal)

    contador = 0
    for fila in lector:
        if numero == contador:
            contador = contador + 1
            continue
        escritor.writerow(fila)
        contador = contador + 1

    archivo.close()
    archivo_temporal.close()
    os.remove(ARCHIVO_DIRECTORIO)
    os.rename("temporal.csv", ARCHIVO_DIRECTORIO)

def menu():
    print("-------- Menu ---------")
    print("1: Agregar")
    print("2: Mostrar")
    print("3: Eliminar")
    print("4: Salir")
    opcion = eval(input("Opcion: "))
    return opcion

opcion_menu = 0

while opcion_menu != 4:
    opcion_menu = menu()
    if opcion_menu == 1:
        agregar()
    elif opcion_menu == 2:
        mostrar()
    elif opcion_menu == 3:
        mostrar()
        numero = eval(input("Escribe el número para eliminar: "))
        si_borrar = input("Estas seguro (S/n): ")
        if si_borrar.lower()[0] == "s":
            borrar(numero)
    elif opcion_menu == 4:
        pass
    else:
        print("Opción Invalida")
















