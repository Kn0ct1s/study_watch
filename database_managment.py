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
            "time_h, time_m, time_s, day, week, year)"
        )
        
    def insert_study_time(
        self,
        data: dict,
        ):
        """
        # This function inserts the users name,
        # how long they studied, what day it is (mon, tue)
        # and what week of their studying it is
        # into the data base
        """
        
        # this is unpacking the data we sent it
        username = data['username']
        subject = data['subject']
        
        study_time = data['study_time']
        time_h = study_time['hours']
        time_m = study_time['minutes']
        time_s = round(study_time['seconds'], 2)
        
        # unpack the nested dict into the correct variables
        date_info = data['date_info']
        day = date_info['day']
        week = date_info['week']
        year = date_info['year']
        
        # the data to insert
        data = [username, subject, time_h, time_m, time_s,
                day, week, year]
        
        # insert our values
        self.cursor.execute("""
            INSERT INTO study_times VALUES
            (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        
        # commit the change to the database
        self.connection.commit()