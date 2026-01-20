import pygame as pg
from settings import *

class Map:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
            [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
            [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
    
    def coords(self,x,y):
        grid_x = int(x // TS)
        grid_y = int(y // TS)
        return grid_x, grid_y

    def has_wall_at(self, x, y):
        if x < 0 or x > WIN_WIDTH or y < 0 or y > WIN_HEIGHT:
         print("brrr")
         return True
        grid_x = int(x // TS)
        grid_y = int(y // TS)
        try:
            return self.grid[grid_y][grid_x] == 1
        except IndexError:
            return True

    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):

                tile_x = TS * j
                tile_y = TS * i

                if self.grid[i][j] == 0:
                    pg.draw.rect(screen, (255,255,255), (tile_x,tile_y,TS,TS))
                    pass
                elif self.grid[i][j] == 1:
                    pg.draw.rect(screen, (40,40,40), (tile_x,tile_y,TS,TS))

    def show_grid(self,x,y):
        try:
            return self.grid[y][x]
        except (IndexError, TypeError):
            return None
        