import math, pygame as pg
from player import Player
from mappy import Map
from settings import *

class Ghost_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 64
        self.colour = (0, 165, 0)
        self.speed = 1
        self.x = 14 * TS
        self.y = 2 * TS
        self.dir_x = 0
        self.dir_y = -1
        # track previous position (tile coords and pixel coords)
        self.prev_tile_x = int(self.x // TS)
        self.prev_tile_y = int(self.y // TS)
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_move = (14, 2)

    def render(self, screen):
        rect = pg.Rect(
            int(self.x) - TS,
            int(self.y) - TS,
            self.size,
            self.size
        )
        pg.draw.rect(screen, self.colour, rect)
    
    def movement(self, player):
        tile_x = int(self.x // TS)
        tile_y = int(self.y // TS)
        print("---------------------------------")
        print("PREV TILE:", (self.prev_tile_x, self.prev_tile_y))
        print("PREV POS:", (self.prev_x, self.prev_y))
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        player_x = int(player.x // TS) + 1
        player_y = int( player.y // TS) + 1
        player_pos = player_x, player_y
        print("PLAYER POS:", player_pos)
        path = []
        pot_move_x = self.x
        pot_move_y = self.y

        pot_move_up = tile_x, tile_y - 1
        pot_move_down = tile_x, tile_y + 1
        pot_move_left = tile_x - 1, tile_y
        pot_move_right = tile_x + 1, tile_y

        self.x_directions = [-1,1]
        self.y_directions = [-1,1]
        self.ok = True
        map = Map()
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]

        above = (tile_x, tile_y - 1)
        below = (tile_x, tile_y + 1)
        left = (tile_x - 1, tile_y)
        right = (tile_x + 1, tile_y)

        self.wall_above = map.show_grid(*above)
        self.wall_below = map.show_grid(*below)
        self.wall_left = map.show_grid(*left)
        self.wall_right = map.show_grid(*right)

        print("ABOVE", above, self.wall_above)
        print("BELOW", below, self.wall_below)
        print("LEFT ", left, self.wall_left)
        print("RIGHT", right, self.wall_right)

        print("GHOST GRID COORDS", tile_x, tile_y)

        moved = False
        
        if tile_x > player_x and not self.wall_left and pot_move_left != self.prev_move:
            self.x -= TS
            moved = True
        elif tile_x < player_x and not self.wall_right and pot_move_right != self.prev_move:
            self.x += TS
            moved = True
        
        if not moved:
            if tile_y > player_y and not self.wall_above and pot_move_up != self.prev_move:
                self.y -= TS
                moved = True
            elif tile_y < player_y and not self.wall_below and pot_move_down != self.prev_move:
                self.y += TS
                moved = True
        
        if not moved:
            if not self.wall_left and pot_move_left != self.prev_move:
                self.x -= TS
            elif not self.wall_right and pot_move_right != self.prev_move:
                self.x += TS
            elif not self.wall_above and pot_move_up != self.prev_move:
                self.y -= TS
            elif not self.wall_below and pot_move_down != self.prev_move:
                self.y += TS
    
        
        print("---------------------------------")
        self.prev_tile_x = int(self.x // TS)
        self.prev_tile_y = int(self.y // TS)
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_move = (self.prev_tile_x, self.prev_tile_y)
        self.last_direction = None  
        print(self.prev_move)
                
    def render(self, screen):
        #pg.draw.circle(screen, self.colour, (int(self.x - TS/2), int(self.y - TS/2)), self.size)
        #pg.draw.rect(screen, self.colour, (int(self.x - TS/2), int(self.y - TS/2)), self.size, self.size)
        rect = pg.Rect(
            int(self.x) - TS,
            int(self.y) - TS,
            self.size,
            self.size
        )
        pg.draw.rect(screen, self.colour, rect)