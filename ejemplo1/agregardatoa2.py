import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ruta del archivo CSV
csv_file_path = "data/saludos_mundo.csv"

# Leer el archivo CSV y agregar los datos a la base de datos
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    leer = csv.DictReader(file, delimiter='|')
    for row in leer:
        # Crear un objeto Saludo con los datos del CSV
        miSaludo = Saludo2(
            mensaje=row['saludo'],
            tipo=row['tipo'],
            origen=row['origen']
        )
        # Agregar el objeto a la sesión
        session.add(miSaludo)

# Confirmar las transacciones
session.commit()
