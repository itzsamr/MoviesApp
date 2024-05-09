import pyodbc

server_name = "SAMAR\MSSQLSERVER01"
database_name = "MoviesDB"

conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={server_name};"
    f"Database={database_name};"
    f"Trusted_Connection=yes;"
)

print(conn_str)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

cursor.execute("Select 1")
print("DB connection is successful🎉")


def read_movies():
    cursor.execute("Select * from Movies")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie)


read_movies()
