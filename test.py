def bresenham(x1=0, y1=0, x2=0, y2=0, speed = 0):
    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0: dx = -dx
    if dy < 0: dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    list_line = []
    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        list_line.append((x,y))
    return iter(list_line)
a =  bresenham(x1=0, y1=0, x2=10, y2=10, speed = 3)


x, y = next(a)
print(x,y)
x, y = next(a)
print(x,y)


def angle_nearest(first_angle,last_angle):
