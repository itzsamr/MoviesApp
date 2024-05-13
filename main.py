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
print("DB connection is successful🎉")


def read_movies():
    cursor.execute("Select * from Movies")
    movies_data = [list(row) for row in cursor.fetchall()]
    headers = ["MovieId", "Title", "Year", "DirectorId"]
    print(tabulate(movies_data, headers=headers, tablefmt="grid"))


def create_movie():
    Title = input("Enter the title of the movie: ")
    Year = int(input("Enter the year of release: "))
    DirectorId = int(input("Enter the director ID: "))

    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        (Title, Year, DirectorId),
    )
    conn.commit()


def delete_movie():
    movie_id = int(input("Enter the Movie_Id to be deleted: "))
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (movie_id,))
    conn.commit()
    print("Movie deleted successfully.")


def update_movie():
    movie_id = int(input("Enter the Movie_Id to be updated: "))
    new_title = input("Enter the new title of the movie: ")
    new_year = int(input("Enter the new year of release: "))
    new_director_id = int(input("Enter the new director ID: "))

    cursor.execute(
        "UPDATE Movies SET Title = ?, Year = ?, DirectorId = ? WHERE MovieId = ?",
        (new_title, new_year, new_director_id, movie_id),
    )
    conn.commit()
    print("Movie updated successfully.")


if __name__ == "__main__":
    print("\nWelcome to the Movies Application🎉")
    while True:
        print("\n1. Read Movies")
        print("2. Create Movie")
        print("3. Update Movie")
        print("4. Delete Movie")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            read_movies()
        elif choice == "2":
            create_movie()
        elif choice == "3":
            update_movie()
        elif choice == "4":
            delete_movie()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a valid option.")
