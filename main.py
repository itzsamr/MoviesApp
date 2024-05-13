import pyodbc
from tabulate import tabulate

server_name = "SAMAR\\MSSQLSERVER01"
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
print("Database connection is successful 🎊")


# Service - Function that talk to DB | Layer that interacts with DB


# Encapsulation
class MovieService:
    def read_movies(self):
        cursor.execute("Select * from Movies")
        # movies = cursor.fetchall() # Get all data
        # for movie in movies:
        #     print(movie)

        # Get data one row at a time
        for row in cursor:
            print(row)

    # Task 1
    # Get the data from the user
    # Clue: Use arguments
    def create_movie(self, movie):
        cursor.execute(
            "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
            (movie.title, movie.year, movie.director_id),
        )
        conn.commit()  # Permanent storing | If no commit then no data

    def update_movie(self, movie, movie_id):
        cursor.execute(
            """
            Update Movies
            Set Title = ?, Year = ?, DirectorId = ?
            where MovieId = ?
            """,
            (movie.title, movie.year, movie.director_id, movie_id),
        )
        conn.commit()  # Permanent storing | If no commit then no data

    # Task 2
    # Delete a movie from the db by getting the id from user
    def delete_movie(self, movie_id):
        cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
        conn.commit()


class DirectorService:
    pass


class ActorService:
    pass


# Entity / Model
# Encapsulation - Movie data
class Movie:
    def __init__(self, title, year, director_id):
        self.title = title
        self.year = year
        self.director_id = director_id


class Director:
    pass


class Actor:
    pass


# Main menu
# 1. Movie Management
# 2. Director Management
# 3. Actor Management
# 4. Exit


# Task 3
# Movie Management Menu
# 1. Add a Movie
# 2. View All Movies
# 3. Update a Movie  (Task 4)
# 4. Delete a Movie
# 5. Back

# C - Create
# R - Read
# U - Update
# D - Delete


def movie_menu():
    movie_service = MovieService()

    while True:
        print(
            """      
        1. Add a Movie
        2. View all Movies
        3. Update a Movie  
        4. Delete a Movie
        5. Back to main menu
                """
        )
        choice = int(input("Please choose from above options: "))

        if choice == 1:
            title = input("Please enter movie title: ")
            year = int(input("Please enter movie year: "))
            director_id = int(input("Please enter movie director's id: "))
            new_movie = Movie(title, year, director_id)
            movie_service.create_movie(new_movie)
        elif choice == 2:
            movie_service.read_movies()
        if choice == 3:
            movie_id = int(input("Please enter movie's id: "))
            title = input("Please enter movie title: ")
            year = int(input("Please enter movie year: "))
            director_id = int(input("Please enter movie director's id: "))
            updated_movie = Movie(title, year, director_id)
            movie_service.update_movie(updated_movie, movie_id)
        elif choice == 4:
            movie_id = int(input("Please tell a movie id to delete: "))
            movie_service.delete_movie(movie_id)
        elif choice == 5:
            break


def director_menu():
    pass


def actor_menu():
    pass


# Task 5 - Keep it in loop
if __name__ == "__main__":
    print("Welcome to the movies app")

    while True:
        print(
            """      
            1. Movie Management
            2. Director Management
            3. Actor Management
            4. Exit
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            movie_menu()
        elif choice == 2:
            director_menu()
        elif choice == 3:
            actor_menu()
        elif choice == 4:
            break

    # Clean up code
    cursor.close()
    conn.close()
