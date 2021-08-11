import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

path = askopenfilename(title = "Seleccione el archivo que quiere editar")
path_split = path.split("/") # Crea una lista con las partes del path
file_name = path_split[-1] # y guarda el último de los elementos en una variable

DIC_TIERS = {"TIER_1": [1, 10],"TIER_2": [5, 15],"TIER_3": [10, 20],"TIER_4": [15, 35],"TIER_5": [20, 42], }

def get_header(path):
    with open (path, "r", newline="") as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
        header = rows[0]
        return header

def writer(header, data, path):
    with open ("new_Excel", "w", newline = "") as f:
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        writer.writerows(data)
    
def choose_column(path) -> tuple:
    header = get_header(path)
    for i in range(len(header)):
        print(f"{i + 1} - {header[i]}")
    choice = int(input("Elija la Columna que desea editar: "))
    column = header[choice - 1]
    return (header, column)

def choose_column_free_day(path) -> tuple:
    header = get_header(path)
    for i in range(len(header)):
        print(f"{i + 1} - {header[i]}")
    choice = int(input("Elija la Columna que contenga los años de antiguedad: "))
    column = header[choice - 1]
    return (header, column)   

def updater(path):
    header, column = choose_column(path)
    with open(path, newline= "") as f:
        readData = [row for row in csv.DictReader(f)]
        for i in range(len(readData)):
            newValue = input("Ingrese el Nuevo Valor: ")
            readData[i][column] = newValue
    writer(header, readData, path)

def free_day_update(path):
    header, column_years = choose_column_free_day(path)
    with open(path, newline= "") as f:
        readData = [row for row in csv.DictReader(f)]
        for i in range(len(readData)):
            if int(readData[i][column_years]) < DIC_TIERS["TIER_1"]:
               pass #Falta la condicion de que los dias no hayan sido cambiados. 


updater(path)
