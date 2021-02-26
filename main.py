def close10(x, y):
    if abs(x-10) < abs(y-10):
        return x 

    elif abs(10-x) > abs(y-10):
        return y 

    else:  
        return 0
print (close10(4,8))