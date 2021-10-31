import pygame as pg 
from  random import  randint
from copy import  deepcopy
from numba import jit
#####################

RES = WIDTH, HEIGHT = 900, 900
TILE = 10
W, H = WIDTH // TILE, HEIGHT // TILE 
FPS = 30

#########
pg.init()
#########

surface = pg.display.set_mode(RES)
clock = pg.time.Clock()

next_field = [[0 for x in range(W)] for j in range(H)]
current_field = [[randint(0, 1) for i in range(W)] for j in range(H)]

###################
@jit(parallel=True)
def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1
    
    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else: 
        if count == 3:
            return 1
        return 0 

while True:
    
    surface.fill(pg.Color('black'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            
    [pg.draw.line(surface, pg.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
    [pg.draw.line(surface, pg.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
    
    for x in range(1, W - 1):
        for y in range(1, H - 1):
            if current_field[y][x]:
                pg.draw.rect(surface, pg.Color('green'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
            next_field[y][x] = check_cell(current_field, x, y)
            
    current_field = deepcopy(next_field)
            
    pg.display.flip()
    clock.tick(FPS)