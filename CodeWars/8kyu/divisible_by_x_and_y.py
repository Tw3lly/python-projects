def is_divisible(n,x,y):
    """Checks if n is cleanly divisible by x and y using modulo, if remainder is 0, it's cleanly divisible and will return True"""
    return n % x == 0 and n % y == 0
