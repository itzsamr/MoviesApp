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
    # movies = cursor.fetchall()
    # for movie in movies:
    #     print(movie)

    # Get data one row at a time
    for row in cursor:
        print(row)


# Task 1
# Get the data from the user
# Clue: Use arguments
def create_movie(Title, Year, DirectorId):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        (Title, Year, DirectorId),
    )
    conn.commit()  # Permanent storing | If no commit then no data


# Task 2
# Delete a movie from the db by getting the id from user
def delete_movie(id):
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", movie_id)
    conn.commit()
    print("Movie deleted successfully.")


if __name__ == "__main__":
    # Title = input("Enter the title of the movie: ")
    # Year = int(input("Enter the year of release: "))
    # DirectorId = int(input("Enter the director ID: "))
    # create_movie(Title, Year, DirectorId)
    read_movies()
    movie_id = int(input("Enter the Movie_Id to be deleted: "))
    delete_movie(movie_id)
