def division(x,y):
    try:
        x = float(x)
        y = float(y)
        c = y / x

    except ZeroDivisionError:
        c = 0
    return c