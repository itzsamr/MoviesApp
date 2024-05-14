from tabulate import *


class MovieService:

    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def read_movies(self):
        try:
            self.cursor.execute("Select * from Movies")
            movies_data = [list(row) for row in self.cursor.fetchall()]
            headers = ["MovieId", "Title", "Year", "DirectorId"]
            print(tabulate(movies_data, headers=headers, tablefmt="grid"))
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()
            self.conn.close()

    def create_movie(self, movie):
        self.cursor.execute(
            "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
            (movie.title, movie.year, movie.director_id),
        )
        self.conn.commit()

    def update_movie(self, movie, movie_id):
        self.cursor.execute(
            """
            Update Movies
            Set Title = ?, Year = ?, DirectorId = ?
            where MovieId = ?
            """,
            (movie.title, movie.year, movie.director_id, movie_id),
        )
        self.conn.commit()

    def delete_movie(self, movie_id):
        self.cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
        self.conn.commit()
