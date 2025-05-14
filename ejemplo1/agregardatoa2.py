import csv
from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2 as Saludo_dos
from configuracion import engine

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Ruta del archivo CSV
csv_file_path = "data/saludos_mundo.csv"

# Leer el archivo CSV y agregar los datos a la base de datos
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='|')
    saludos = [Saludo_dos(mensaje=row['saludo'], tipo=row['tipo'], origen=row['origen']) for row in reader]
    session.add_all(saludos)

# Confirmar las transacciones
session.commit()
