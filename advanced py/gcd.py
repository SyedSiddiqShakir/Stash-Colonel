def gcd(x: int, y: int):
    x_div = []
    x1 = x
    while x != 0:
        if x%x1 == 0:
            x -= 1
            x_div.append(x)
    
    y_div = []
    y1 = y
    while y != 0:
        if y%y1 == 0:
            y -= 1
            y_div.append(y)
    x_div.sort(reverse = True)
    y_div.sort(reverse = True)
    for i in x_div:
        if i in y_div:
            return i
gcd(18, 48)