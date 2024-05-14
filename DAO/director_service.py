# Encapsulation
from Util.DBconn import DBConnection


class DirectorService(DBConnection):
    def read_directors(self):
        try:
            self.cursor.execute("Select * from Directors")
            directors = self.cursor.fetchall()  # Get all data
            for director in directors:
                print(director)
        except Exception as e:
            print(e)

    def create_director(self, director):
        try:
            self.cursor.execute(
                "INSERT INTO Directors (Name) VALUES (?)",
                (director.name),
            )
            self.conn.commit()  # Permanent storing | If no commit then no data
        except Exception as e:
            print(e)
