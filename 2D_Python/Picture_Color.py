
import pygame as pg
import math as mth
import random

pg.display.set_caption("Don Queasly")
char_L = pg.image.load('./Pictures/don_left.png') # 64 X 64
char_R = pg.image.load('./Pictures/don_right.png')
chklg_L = pg.image.load('./Pictures/chkleg_L.png') # 31 X 20
chklg_R = pg.image.load('./Pictures/chkleg_R.png')
Slug = pg.image.load('./Pictures/slug.png')    # 33 X 20 
Ghost_L = pg.image.load('./Pictures/ghost_L.png')
Ghost_R = pg.image.load('./Pictures/ghost_R.png')
#background = pg.image.load('Background.jpg')  #1080 X 610
sbackground = pg.image.load('./Pictures/Scroll1.png')  #1100 * 550


set_width = 1100
set_height = 550
ground = 500
window = pg.display.set_mode((set_width,set_height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

