import sqlite3

from modules import check_files

class DataBase:
    """
    # This class controls all operations 
    # relating to the database of the application
    #
    # It also has features that let other part of the program 
    # know if there was an error with the database
    """
    
    def __init__(self) -> None:
        
        # this is the path to the database
        database_folder = 'database'
        database_name = 'study_times.db'
        
        # full path to the database
        database_path = database_folder + '/' + database_name
        
        # this is a status code telling us information about
        # the database
        self.status_code = check_files(database_name, database_folder)
        
        # this establishes a connection to the database
        self.connection = sqlite3.connect(database_path)
        
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