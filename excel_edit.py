import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

path = askopenfilename(title = "Seleccione el archivo que quiere editar")
path_split = path.split("/") # Crea una lista con las partes del path
file_name = path_split[-1] # y guarda el último de los elementos en una variable

def get_header(path):
    with open (path, "r", newline="") as f:
        csv_reader = csv.reader(f)
        rows = list(csv_reader)
        header = rows[0]
        return header

def writer(header, data, path):
    with open (path, "w", newline = "") as f:
        writer = csv.DictWriter(f, fieldnames = header)
        writer.writeheader()
        writer.writerows(data)

def updater(path):
    header = get_header(path)
    with open(path, newline= "") as f:
        readData = [row for row in csv.DictReader(f)]
        for i in range(len(readData)):
            newRating = float(input("Ingrese el Nuevo Valor: "))
            readData[i]["Rating"] = newRating
    writer(header, readData, path)

updater(path)
