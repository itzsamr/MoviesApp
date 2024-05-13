import pyodbc
from tabulate import tabulate
from Entity.movie import *
from DAO.movie_service import *

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
# cursor = conn.cursor()
# cursor.execute("Select 1")
# print("Database connection is successful 🎊")


def movie_menu():
    movie_service = MovieService(conn)

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

    cursor.close()
    conn.close()
