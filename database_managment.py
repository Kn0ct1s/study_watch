import sqlite3

from modules import check_files

class DataBase:
    """
    # This is the class that controls the database
    # operations.
    """
    
    def __init__(self) -> None:
        
        check_files('study_times.db', 'database')
        
        connection = sqlite3.connect('database/study_times.db')
        
x = DataBase()