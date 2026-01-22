import math, pygame as pg
import random
from mappy import Map
from settings import *

class Ghost_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 64
        self.colour = (255, 0, 0)
        self.speed = 1
        self.x = 14 * TS
        self.y = 3 * TS
        self.dir_x = 0
        self.dir_y = -1

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


    def get_coords(self):
        return (self.x // TS, self.y // TS)
    
    def movement(self):
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.x_directions = [-1,1]
        self.y_directions = [-1,1]
        number = random.randint(0,3)
        self.ok = True
        map = Map()

        #wall above
        self.above_X = int((self.x + TS/2) //TS) - 1
        self.above_Y = int((self.y - TS/2)//TS) - 1
        self.wall_above = map.show_grid(self.above_X, self.above_Y)
        print(self.above_X,self.above_Y)
        print(self.wall_above)
        print("")

        #wall below
        self.below_X = int((self.x + TS/2) //TS) - 1
        self.below_Y = int((self.y - TS/2)//TS) - 1 + 2
        self.wall_below = map.show_grid(self.below_X, self.below_Y)
        print(self.below_X,self.below_Y)
        print(self.wall_below) 
        print("")

        #wall left
        self.left_X = int((self.x + TS/2) //TS) - 2
        self.left_Y = int((self.y - TS/2)//TS) 
        self.wall_left = map.show_grid(self.left_X, self.left_Y)
        print(self.left_X,self.left_Y)
        print(self.wall_left) 
        print("")

        #wall right
        self.right_X = int((self.x + TS/2) //TS) 
        self.right_Y = int((self.y - TS/2)//TS) 
        self.wall_right = map.show_grid(self.right_X, self.right_Y)
        print(self.right_X,self.right_Y)
        print(self.wall_right)
         
        self.ghost_coords = map.coords(self.x, self.y)

        while self.ok:
            self.dir_x,self.dir_y = self.directions[number]

            self.potential_move = (self.ghost_coords[0] + self.dir_x, self.ghost_coords[1] + self.dir_y)

            print("GHOST COORDS",self.ghost_coords)
            print("")

            if self.dir_x == 1 and not self.wall_right:
                self.x += TS
                self.ok = False
            elif self.dir_x == -1 and not self.wall_left:
                self.x -= TS
                self.ok = False
            elif self.dir_y == -1 and not self.wall_above:
                self.y -= TS
                self.ok = False
            elif self.dir_y == 1 and not self.wall_below:
                self.y += TS
                self.ok = False
            else:
                number = random.randint(0,3)
                
            print("")        
