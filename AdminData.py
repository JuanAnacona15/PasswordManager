import csv

class AdminData():
    def __init__(self):
        self.filename = "data.csv"
        self.fieldnames = ["name", "password"]
        # Crea el archivo CSV con encabezados si no existe
        try:
            with open(self.filename, 'x', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['name', 'password'])
        except FileExistsError:
            pass

    def Read(self, path):
        # Leer el archivo CSV
        with open(self.filename, mode='r') as file:
            lectorCsv = csv.reader(file)
            for fila in lectorCsv:
                if(fila[0] == path):
                    return fila[1]
            return False

    def readAll(self):
        with open(self.filename, mode='r') as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                print(f"{row[0]} -> {row[1]}")
                
        
    def addPassword(self, newPassword, name):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, newPassword])
        print(f'Password added: {name} -> {newPassword}')
        
    def update(self, name, password):
        rows = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == name:
                    row['password'] = password
                rows.append(row)
        
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
            
    def delete(self, name):
        rows = []
        with open(self.filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] != name:
                    rows.append(row)
        
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(rows)