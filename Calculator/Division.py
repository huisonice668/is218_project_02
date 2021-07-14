def division(x,y):
    c = 0
    try:
        x = float(x)
        y = float(y)
        c = y / x
    except ZeroDivisionError:
        print('Can not divide by zero')

    return c