import os,time
from funciones import *

while True:
    os.system("cls")
    print("""
\tMenú Contactos
1. Agregar contacto
2. Mostrar contactos
3. Guardar Archivo
4. Salir""")
    opc = validar_opc([1,2,3,4])
    if opc == 1:
        opcion_1()
    if opc == 2:
        opcion_2()
    if opc == 3:
        opcion_3()
    else:
        pass