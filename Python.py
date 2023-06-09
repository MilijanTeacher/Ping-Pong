from pygame import *

back = [255,0,255]
window = display.set_mode((700,500))
window.fill(back)

clock = time.Clock()
finis = True

while finis:
    for e in event.get():
        if e.type == QUIT:
            finis = False
    
    display.update()
    clock.tick(60)