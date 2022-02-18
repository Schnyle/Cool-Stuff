import numpy as np

def check_prime(val):
    """

    Parameters
    ----------
    val : any number

    Returns
    -------
    bool: whetheer val is prime or not

    """
    
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

def find_divisors(val):
    """
    

    Parameters
    ----------
    val : any number

    Returns
    -------
    result : list of divisors of val
        in ascending order

    """
    
    result = []
    
    try:
        val = int(val)
    except:
        print('not an integer')
        return
    
    
    half_val = int( val/2 )
    
    
    for i in range(1, half_val+1):
        if val%i == 0:
            result.append(i)
    
    return result
    
    
