import sqlite3

from modules import check_files

class DataBase:
    """
    # This is the class that controls the database
    # operations.
    """
    
    def __init__(
        self,
        filename='study_times.db',
        directo='database',
        ) -> None:
        
        # full path to the database
        full_path = directo + '/' + filename
        
        # this is the database being made and checked
        self.status_code = check_files(filename, directo)
        
        # the connection to the database
        self.connection = sqlite3.connect(full_path)
        
        # cursor object
        self.cursor = self.connection.cursor()
        
        # check if we need to set up the database
        if self.status_code == -1 or self.status_code == 0:
            self._database_setup()
        
        
    def _database_setup(self) -> None:
        """
        # This class function creates a database with
        # the correct rows if their is no database to work with
        """
        
        self.cursor.execute(
            "CREATE TABLE study_times(user, time, day)"
        )
        
    def insert_study_time(
        self,
        username: str,
        time: int,
        day: str,
        ):
        """
        # This function inserts the users name,
        # how long they studied and what day it is
        # into the data base
        """
        # the data to insert
        data = [username, time, day]
        
        self.cursor.execute("""
            INSERT INTO study_times VALUES
            (?, ?, ?)
        """, data)
        
        self.connection.commit()