import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
connection_string = "postgres://bambi_user:VNw81hK03f5A2pvNlyexCWdffjrb6vPj@dpg-cnitbq8l5elc73feo090-a.frankfurt-postgres.render.com/bambi"
engine = create_engine(connection_string)

            # Intentar establecer la conexión a la base de datos
try:
    with engine.connect() as connection:
        # Realizar operaciones en la base de datos aquí
        print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function


# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
