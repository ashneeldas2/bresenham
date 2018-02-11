from display import *

def draw_line( x0, y0, x1, y1, screen, color):
    if (x0 > x1): 
        temp = x0
        x0 = x1
        x1 = temp 
        temp = y0
        y0 = y1
        y1 = temp 
    
    x = x0 
    y = y0
    a = y1-y0
    b = -(x1-x0)

    if (b == 0): 
        if y0<y1: 
            while y <= y1: 
                plot(screen, color, x, y)
                y += 1
        else: 
            while y >= y1: 
                plot(screen, color, x, y)
                y -= 1
        return
    
    m = -1.0 * a/b

    if m <= 1 and m >= 0:
        d = 2 * a + b        
        while (x <= x1) :
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * b
            x += 1
            d += 2 * a
    elif m >= -1 and m < 0:
        d = 2 * a - b
        while (x <= x1) :
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a
    elif (m > 1):
        d = a + 2 * b
        while (y <= y1) :
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * a
            y += 1
            d += 2 * b
    elif (m < -1):
        d =  a - 2 * b
        while (y >= y1) :
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * a
            y -= 1
            d -= 2 * b

# 3 is 7 but in reverse
# 4 is 8 but in reverse
# 5 is 1 but in reverse
# 6 is 2 but in reverse

    
    

