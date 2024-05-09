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
print("DB coonection is successful🎉")

print("Hello Word!")
