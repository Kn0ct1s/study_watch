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
        # the correct rows if there is no database to work with
        # or if its the users first time opening the application
        """
        
        self.cursor.execute(
            "CREATE TABLE study_times(user, subject, "
            "time_h, time_m, time_s, day)"
        )
        
    def insert_study_time(
        self,
        username: str,
        subject: str,
        study_time: dict,
        day: str,
        ):
        """
        # This function inserts the users name,
        # how long they studied, what day it is (mon, tue)
        # and what week of their studying it is
        # into the data base
        """
        
        time_h = study_time['hours']
        time_m = study_time['minutes']
        time_s = round(study_time['seconds'], 2)
        
        # the data to insert
        data = [username, subject, time_h, time_m, time_s, day]
        
        
        
        self.cursor.execute("""
            INSERT INTO study_times VALUES
            (?, ?, ?, ?, ?, ?)
        """, data)
        
        self.connection.commit()