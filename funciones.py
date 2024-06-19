#Listas:

contactos = []


#Opcion 1
def opcion_1():
    print("Agregar contacto")
    nombre = input("Ingrese nombre: ")
    telefono = input("Ingrese teléfono: ")
    correo = input("Ingrese correo: ")

    contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
        #Agragar a la lista:
    contactos.append(contacto)
    print("Contacto agregado con éxito")

#Opcion 2
def opcion_2():
    if len(contactos) == 0:
        print("No existen contactos")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELÉFONO: {c['telefono']}")
            print(f"CORREO {c['correo']}\n")
#Opcion 3

def opcion_3():
    pass

#opcion  4

def opcion_4():
    pass