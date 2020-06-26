import pygame as pg
pg.init()
music = pg.mixer.music.load('./Sounds/Ghosts.MP3')
shoot_sound = pg.mixer.Sound('./Sounds/bullet.wav')
njump_sound = pg.mixer.Sound('./Sounds/normjump.wav')
sjump_sound = pg.mixer.Sound('./Sounds/bigjump.wav')
hit_sound = pg.mixer.Sound('./Sounds/hit.wav')
