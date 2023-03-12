import os
import time

from database_managment import DataBase
from time_reader import log_time

def intro() -> None:
    """
    # The purpose of this function is to provide an
    # introduction to the program and tell the user how to
    # set up a database
    """

if __name__ == "__main__":
    
    # this is the users name
    name = os.getlogin()
    
    # this is the data base object
    datab = DataBase()
    
    # welcome messages
    if datab.status_code == 0:
        print(f"Welcome to Study Watch {name}")
    # returning msg
    elif datab.status_code == 1:
        print(f"Welcome back to Study Watch {name}")
    # error message ----------------------------------REVIST               
    elif datab.status_code == -1:
        print(
            f"{name} possible user/system error encountered\n"
            "No data in database file.")
    
    subject = input("What subject are you studying: ").strip()
    subject = subject.title()
    
    print("Type 'start' to start or 'quit' to quit ")
    
    ans = input("--> ").strip()
    ans = ans.lower()

    # if they type quit exit the program
    if ans == 'quit':
        exit()
    elif ans == 'start':
        
        # get the amount of time they have been studying
        study_time = log_time()
        
        # get the day name i.e monday 
        day = time.strftime("%A", time.gmtime())
        
        # insert the data
        datab.insert_study_time(name, subject, study_time, day)
        
        