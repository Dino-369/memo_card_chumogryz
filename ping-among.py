print("Hello  print")
from pygame import *

from pygame import *
from random import randint
from time import time as timer#as timer чтобы не конфликтовал с pygame   time(delay)

plaueyuyer_img = "ufo.png"
ballerino_sharino = "asteroid.png"

font.init()
font1 = font.SysFont("Calibri",90)
font2 = font.SysFont("Calibri",45)#шрифт  none
YOU_WON = font1.render("YOU WON", True,(2,90,13))
YOU_LOSEr = font1.render("YOU LOSEr", True,(90,13,2))
back = (250,125,72.5)


goal = 25
FPS = 30
max_lost = 5


win_width = 700
win_heigth = 500

window = display.set_mode((win_width,win_heigth))
display.set_caption("Закат и расвет3")
#background = transform.scale(image.load(img_back),(win_width,win_heigth))#transform -  маштабировать
window.fill(back)

finish = False
game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
    display.update()
    clock.tick(FPS)

print("Good bue print")