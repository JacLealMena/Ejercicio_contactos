import csv

#Listas:

contactos = []

#Opcion 1
def opcion_1():
    print("AGREGAR CONTACTO\n")
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
        #Diccionario de un contacto:
    contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
        #Agragar contacto a la lista:
    contactos.append(contacto)
    print(">>> Contacto agregado con éxito")

#Opcion 2
def opcion_2():
    if validar_contactos():
        print("LISTA DE CONTACTOS\n")
        for c in contactos:
            print(f"-> NOMBRE: {c['nombre']}")
            print(f"-> TELÉFONO: {c['telefono']}")
            print(f"-> CORREO {c['correo']}\n")

#Opcion 3
def opcion_3():
    if validar_contactos():
        nom_archivo = validar_nom_archivo()
        with open(nom_archivo+".csv", "w", newline="") as archivo: #Crear archivo CSV
            escritor = csv.DictWriter(archivo,["nombre","telefono","correo"])
            escritor.writeheader() #Nombre de las llaves al principio
            escritor.writerows(contactos) #Escribir cada dic de la lista
        print(">>> Archivo Creado")

#opcion  4
def opcion_4(): 
    print("Ha salido")
    exit()

#Funciones de Validaciones

def validar_opc(lista_opciones):
    while True:
        try:
            opc = int(input("> Opción: "))
            if opc in lista_opciones:
                return opc
            else:
                print(">>> Opción inválida")
        except:
            print(">>> Error! Debe ingresar un número.")
def validar_nombre():
    while True:
        nombre = input("> Ingrese nombre: ")
        if len(nombre) >= 3 and nombre.isalpha():
            return nombre
        else:
            print(">>> Error! El nombre debe tener al menos 3 letras!")
def validar_telefono():
    while True:
        try:
            telefono = int(input("> Ingrese teléfono: "))
            if len(str(telefono))==9 and str(telefono)[0]=="9":
                return telefono
            else:
                print(">>> Error! El teléfono debe comenzar con 9 y tener 9 dígitos".)
        except:
            print(">>> Error! Debe ingresar un número entero!")
def validar_correo():
    while True:
        #pattern
        correo = input("> Ingrese correo: ")
        if correo.lower().endswith("@gmail.com") and len(correo.strip())>=13:
            return correo
        else:
            print(">>> Error! correo inválido.")
def validar_contactos():
    if len(contactos)==0:
        print("No existen contactos, agregue usando la opción 1")
        return False
    return True
def validar_nom_archivo():
    nom_archivo = input("> Ingrese nombre del archivo: ")
    if len(nom_archivo.strip())>=3:
        return nom_archivo