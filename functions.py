import numpy as np

def check_prime(val):
    
    try:
        val = int(val)
    except:
        print('not an integer')
        return
    
    if val == 0:
        return False
    
    if val == 1:
        return False
    
    if val == -1:
        return False
    
    sqrt_val = int( np.sqrt(val) )
    for i in range(2, sqrt_val+1):
        if (val % i) == 0:
            return False
    return True
