from excel_edit import updater


def validar_opcion(minimo: int, maximo: int) -> int:
    opcion = int(input("Ingrese un numero de opcion: "))
    while not opcion in range(minimo, maximo + 1):
        print("Error. Intentelo nuevamente.")
        opcion = int(input("Ingrese un numero de opcion: "))
    
    return int(opcion)


def main() -> None:

    path = askopenfilename(title = "Seleccione el archivo que quiere editar")
    path_split = path.split("/") # Crea una lista con las partes del path
    file_name = path_split[-1] # y guarda el último de los elementos en una variable

    continuar = True
    while continuar:
        print(
            """ 
            1) Crear un nuevo excel.
            2) Updatear un archivo excel.
            3) Subir un archivo.
            4) Descargar un archivo.
            5) Sincronizar.
            6) Generar carpetas de una evaluacion.
            7) Actualizar entregas de alumnos vía mail.
            8) Salir. 
            """)
        
        opcion = validar_opcion(1, 8)
        if opcion == 1:
            pass
        elif opcion == 2:
            updater(path)
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            print("Saliendo del programa")
            continuar = False 

main()