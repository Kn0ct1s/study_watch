import time

def _convert_time(time_s) -> dict:
    """
    # The purpose of this sub-function is to take a time object
    # and add the correct amount of hours, minutes and seconds into
    # a dictonary
    """
    
    # holds our values
    time = {
        'hours': int(),
        'minutes': float(),
        'seconds': float()
    }
    
    # goes through the time and calculates hours, mins, secs
    while time_s > 0:
        if time_s >= 60:
            time['minutes'] += 1
            time_s -= 60
        elif time_s < 60:
            time['seconds'] = time_s
            time_s = 0
            
        if time['minutes'] == 60:
            time['hours'] += 1
            time['minutes'] = 0
            
    return time

def log_time() -> dict:
    """
    # The purpose of this function is to log how long the user has
    # been studying for.
    # 
    # It waits for user input before passing it to a function to 
    # structure the data correctly and then returns it
    """
    
    # when they started studying
    start_study = time.time()
    
    # wait till the user is done studying
    while True:
        ans = input("Have you finished studying(y/n): --> ")
        ans = ans.strip().lower()
        
        if ans == 'y':
            break
        else:
            continue
    
    end = time.time()
    
    # elapsed time
    elap = end - start_study
    
    time_data = _convert_time(elap)

    return time_data    