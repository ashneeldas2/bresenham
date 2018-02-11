from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ] # green
for i in range(501): 
    color[0] += 5
    if color[0] > 255: 
        color[0] %= 3
    color[2] += 6
    if color[2] > 255: 
        color[2] %= 2
    draw_line(250, 250, 500-i, abs(250-i), screen, color)
    draw_line(250, 250, 500-i, 500 - abs(250-i), screen, color)
display(screen)
save_extension(screen, 'img.png')

