# Encapsulation
from Util.DBconn import DBConnection


class MovieService(DBConnection):
    def read_movies(self):
        try:
            self.cursor.execute("Select * from Movies")
            movies = self.cursor.fetchall()  # Get all data
            for movie in movies:
                print(movie)
        except Exception as e:
            print(e)

    # Task 1
    # Get the data from the user
    # Clue: Use arguments
    def create_movie(self, movie):
        try:
            self.cursor.execute(
                "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
                (movie.title, movie.year, movie.director_id),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)

    def update_movie(self, movie, movie_id):
        self.cursor.execute(
            """
            Update Movies
            Set Title = ?, Year = ?, DirectorId = ?
            where MovieId = ?
            """,
            (movie.title, movie.year, movie.director_id, movie_id),
        )
        self.conn.commit()  # Permanent storing | If no commit then no data

    # Task 2
    # Delete a movie from the db by getting the id from user
    def delete_movie(self, movie_id):
        self.cursor.execute("Delete from Movies Where MovieId = ?", movie_id)
        self.conn.commit()
