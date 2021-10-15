import pygame as pg 
from  random import  randint
from copy import  deepcopy

RES = WIDTH, HEIGHT = 1300, 900
TILE = 50 
W, H = WIDTH // TILE, HEIGHT // TILE 
FPS = 10     

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

next_field = [[0 for x in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

while True:
    
    surface.fill(pg.Color('black'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    [pg.draw.line(surface, pg.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pg.draw.line(surface, pg.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
            
    pg.display.flip()
    clock.tick(FPS)