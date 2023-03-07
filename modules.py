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
    # If they do it returns 0 for success this users is logging
    # back on
    # 
    # If they do but the file is empty it returns -1
    # indicating possible user/system error
    # 
    # If they dont exist it returns -2
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
            
            # return -2
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
        