import streamlit as st
import pyodbc


def connect_to_database():
    server_name = "SAMAR\\MSSQLSERVER01"
    database_name = "MoviesDB"

    conn_str = (
        f"Driver={{SQL Server}};"
        f"Server={server_name};"
        f"Database={database_name};"
        f"Trusted_Connection=yes;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn, cursor
    except pyodbc.Error as e:
        st.error("Failed to connect to the database.")
        st.error(e)
        return None, None


def read_movies(cursor):
    cursor.execute("SELECT * FROM Movies")
    movies = cursor.fetchall()
    return movies


def create_movie(cursor, conn, title, year, director_id):
    cursor.execute(
        "INSERT INTO Movies (Title, Year, DirectorId) VALUES (?, ?, ?)",
        (title, year, director_id),
    )
    conn.commit()


def delete_movie(cursor, conn, movie_id):
    cursor.execute("DELETE FROM Movies WHERE MovieId = ?", (movie_id,))
    conn.commit()


def update_movie(cursor, conn, movie_id, new_title, new_year, new_director_id):
    cursor.execute(
        "UPDATE Movies SET Title = ?, Year = ?, DirectorId = ? WHERE MovieId = ?",
        (new_title, new_year, new_director_id, movie_id),
    )
    conn.commit()


def main():
    st.title("Movies Application")

    conn, cursor = connect_to_database()
    if conn is None:
        st.stop()

    st.sidebar.write("Navigation")
    menu_choice = st.sidebar.radio(
        "Go to", ["Read Movies", "Create Movie", "Update Movie", "Delete Movie"]
    )

    if menu_choice == "Read Movies":
        st.header("Read Movies")
        movies = read_movies(cursor)
        for movie in movies:
            st.write(movie)
    elif menu_choice == "Create Movie":
        st.header("Create Movie")
        title = st.text_input("Enter the title of the movie")
        year = st.number_input(
            "Enter the year of release", min_value=1900, max_value=2100
        )
        director_id = st.number_input("Enter the director ID", min_value=1)
        if st.button("Create"):
            create_movie(cursor, conn, title, year, director_id)
            st.success("Movie created successfully.")
    elif menu_choice == "Update Movie":
        st.header("Update Movie")
        movie_id = st.number_input("Enter the Movie_ID to be updated")
        new_title = st.text_input("Enter the new title of the movie")
        new_year = st.number_input(
            "Enter the new year of release", min_value=1900, max_value=2100
        )
        new_director_id = st.number_input("Enter the new director ID", min_value=1)
        if st.button("Update"):
            update_movie(cursor, conn, movie_id, new_title, new_year, new_director_id)
            st.success("Movie updated successfully.")
    elif menu_choice == "Delete Movie":
        st.header("Delete Movie")
        movie_id = st.number_input("Enter the Movie_ID to be deleted")
        if st.button("Delete"):
            delete_movie(cursor, conn, movie_id)
            st.success("Movie deleted successfully.")


if __name__ == "__main__":
    main()
