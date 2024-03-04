import psycopg2
import pandas as pd

# Conexión a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="Primera DB",
    user="postgres",
    password="24Chanchito20"
)

# Definir la consulta SQL
sql_query = "SELECT title, first_name||' '||last_name AS autor, name AS editorial FROM books " \
            "INNER JOIN book_authors ON books.book_id = book_authors.book_id " \
            "INNER JOIN authors ON book_authors.author_id = authors.author_id " \
            "INNER JOIN publishers ON publishers.publisher_id = books.publisher_id " \
            "ORDER BY title"

# Ejecutar la consulta y recuperar los resultados
df = pd.read_sql_query(sql_query, conn)

# Cerrar la conexión
conn.close()

# Ahora df contiene los datos de la tabla en un DataFrame
print(df)

# Guardamos la información en un archivo CSV
df.to_csv('datos.csv', index=False)
