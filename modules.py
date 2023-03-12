# This is the file that will have peices of code that i use
# often in modular form

import os

def check_files(
    file: str,
    dir_path=None
    ) -> int:
    """
    # This function takes a filename and an optional directory path
    # and checks if both the file and directory exist
    # 
    # if they do but the file is empty returns -1
    # indicating possible user/system error
    #
    # if they don't exist it returns 0 
    # indicating that they are new to the program
    """
    
    # if they need a directory made
    if dir_path != None:
        
        # new path for the file
        filepath = dir_path + '/' + file
        
        # try to make the dir
        try:
            os.mkdir(dir_path)
        # if the dir exists
        except FileExistsError:
            # the dir exists
            None
        
        # try to open the file
        try:
            with open(filepath):
                None
            # check if its empty
            if os.path.getsize(filepath) == 0:
                # return -1
                # (might be user/system error)
                return -1
            else:
                # everything is ok 
                # return 0 to indicate success
                return 1
        except FileNotFoundError:
            # if the file does not exist make it
            with open(filepath, 'w') as f:
                f.close()
            
            # this indicates this is most likely a new user
            return 0

    # try to open the main file
    try:
        with open(file):
            None
        
        # if the file exists but is empty
        # (might indicate user/system error)
        if os.path.getsize(file) == 0:
            return -1
        # the file has data to read
        else:
            # return success
            return 1
    except FileNotFoundError:
        # if they want it in a directory
        # make the file otherwise
        with open(file, 'w') as f:
            f.close()
        
        # file is empty but means its most likly first run of the
        # program
        return 0

def clear_screen() -> None:
    
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')