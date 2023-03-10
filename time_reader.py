import time

def _convert_time(time_s) -> dict:
    
    time = {
        'hours': int(),
        'minutes': float(),
        'seconds': float()
    }
    
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
    
    # when they started studying
    start_study = time.time()
    
    while True:
        ans = input("Have you finished studying(y/n): --> ")
        ans = ans.strip().lower()
        
        if ans == 'y':
            break
        else:
            continue
    
    end = time.time()
    
    elap = end - start_study
    
    time_data = _convert_time(elap)

    return time_data    