import csv

#Listas:

contactos = []


#Opcion 1
def opcion_1():
    print("AGREGAR CONTACTO\n")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese teléfono: ")
    correo = input("Ingrese correo: ")
        #Diccionario de un contacto:
    contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
        #Agragar contacto a la lista:
    contactos.append(contacto)
    print(">>> Contacto agregado con éxito")

#Opcion 2
def opcion_2():
    if len(contactos) == 0:
        print(">>> No existen contactos")
    else:
        print("LISTA DE CONTACTOS\n")
        for c in contactos:
            print(f"-> NOMBRE: {c['nombre']}")
            print(f"-> TELÉFONO: {c['telefono']}")
            print(f"-> CORREO {c['correo']}\n")

#Opcion 3
def opcion_3():
    if len(contactos) == 0:
        print(">>> No existen contactos")
    else:
        nom_archivo = input("Ingrese nombre del archivo: ")
        with open(nom_archivo+".csv", "w", newline="") as archivo: #Crear archivo CSV
            escritor = csv.DictWriter(archivo,["nombre","telefono","correo"])
            escritor.writeheader() #Nombre de las llaves al principio
            escritor.writerows(contactos) #Escribir cada dic de la lista
        print(">>> Archivo Creado")
#opcion  4

def opcion_4():
    print("Ha salido")
    exit()