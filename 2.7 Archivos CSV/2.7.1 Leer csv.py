

import csv

with open("archivos\\datos.cvs") as archivo:
    print(csv.reader(archivo))
    for row in reader:
        print(row)
    
