import os
from modules import check_files

if __name__ == "__main__":
    
    # this is the users name
    name = os.getlogin()
    
    file = 'test.txt'
    
    file_status = check_files(file, 'database')
    
    if file_status == 0:
        print(f"Welcome back {name} to Study Watch")
    elif file_status == -1:
        print(
            f"Database file is empty {name}.\n"
            "This might mean a user/system error occured "
            "please setup a new database:\n")
    elif file_status == -2:
        print(f"Welcome to study watch {name}")