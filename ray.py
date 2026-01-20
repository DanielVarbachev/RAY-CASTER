import math
import pygame as pg

from settings import *

def brrAngle(angle):
    angle = angle % (2 * math.pi)
    if angle < 0:
        angle = (2 * math.pi) + angle
    return angle

class Ray:
    def __init__(self, angle, player,map):
        self.rayAngle = brrAngle(angle)
        self.player = player
        self.map = map
        self.faceDOWN = self.rayAngle > 0 and self.rayAngle < math.pi
        self.faceUP = not self.faceDOWN
        self.faceRIGHT = (self.rayAngle < 0.5 * math.pi) or (self.rayAngle > 1.5 * math.pi)
        self.faceLEFT = not self.faceRIGHT

        self.darkness = 0
        self.min_darkness = 0
        self.max_darkness = 200

        self.hitX = 0
        self.hitY = 0

        self.distance = 0
    
    def cast(self):
        self.foundHORIWALL = False
        self.Hori_HitX = 0
        self.Hori_HitY = 0

        self.firstINTX = None
        self.firstINTY = None

        if abs(math.sin(self.rayAngle)) > 0.000001:
            if self.faceUP:
                self.firstINTY = ((self.player.y) // TS) * TS - 1
            else:
                self.firstINTY = ((self.player.y) // TS) * TS + TS

            try:
                self.firstINTX = self.player.x + (self.firstINTY - self.player.y) / math.tan(self.rayAngle)
            except Exception:
                self.firstINTX = self.player.x

            nextHoriX = self.firstINTX
            nextHoriY = self.firstINTY

            y_step = TS if self.faceDOWN else -TS
            tan_a = math.tan(self.rayAngle)
            if abs(tan_a) < 0.000001:
                x_step = 0
            else:
                x_step = y_step / tan_a

            while (0 <= nextHoriX <= WIN_WIDTH) and (0 <= nextHoriY <= WIN_HEIGHT):
                checkY = nextHoriY - 1 if self.faceUP else nextHoriY
                if self.map.has_wall_at(nextHoriX, checkY):
                    self.foundHORIWALL = True
                    self.Hori_HitX = nextHoriX
                    self.Hori_HitY = nextHoriY
                    break
                else:
                    nextHoriX += x_step
                    nextHoriY += y_step

        found_VERTWALL = False
        self.Vert_HitX = 0
        self.Vert_HitY = 0

        if abs(math.cos(self.rayAngle)) > 0.000001:
            if self.faceRIGHT:
                firstVertX = ((self.player.x) // TS) * TS + TS
            else:
                firstVertX = ((self.player.x) // TS) * TS - 1

            try:
                firstVertY = self.player.y + (firstVertX - self.player.x) * math.tan(self.rayAngle)
            except Exception:
                firstVertY = self.player.y

            nextVertX = firstVertX
            nextVertY = firstVertY

            x_step = TS if self.faceRIGHT else -TS
            tan_a = math.tan(self.rayAngle)
            y_step = x_step * tan_a

            while (0 <= nextVertX <= WIN_WIDTH) and (0 <= nextVertY <= WIN_HEIGHT):
                checkX = nextVertX if self.faceRIGHT else nextVertX - 1
                if self.map.has_wall_at(checkX, nextVertY):
                    found_VERTWALL = True
                    self.Vert_HitX = nextVertX
                    self.Vert_HitY = nextVertY
                    break
                else:
                    nextVertX += x_step
                    nextVertY += y_step

        self.hitX = 0
        self.hitY = 0
        if self.foundHORIWALL and found_VERTWALL:
            dx_h = self.Hori_HitX - self.player.x
            dy_h = self.Hori_HitY - self.player.y
            dist_h = math.hypot(dx_h, dy_h)

            dx_v = self.Vert_HitX - self.player.x
            dy_v = self.Vert_HitY - self.player.y
            dist_v = math.hypot(dx_v, dy_v)

            if dist_v < dist_h:
                self.hitX, self.hitY = self.Vert_HitX, self.Vert_HitY
                self.distance = dist_v
            else:
                self.hitX, self.hitY = self.Hori_HitX, self.Hori_HitY
                self.distance = dist_h

        elif self.foundHORIWALL:
            self.hitX, self.hitY = self.Hori_HitX, self.Hori_HitY
            dx = self.hitX - self.player.x
            dy = self.hitY - self.player.y
            self.distance = math.hypot(dx, dy)
        elif found_VERTWALL:
            self.hitX, self.hitY = self.Vert_HitX, self.Vert_HitY
            dx = self.hitX - self.player.x
            dy = self.hitY - self.player.y
            self.distance = math.hypot(dx, dy)
        else:
            self.distance = float('inf')
        
        self.distance *= math.cos(self.player.angle - self.rayAngle) 
        
    def render(self, screen):
        if self.hitX != 0 or self.hitY != 0:
            end_x, end_y = self.hitX, self.hitY
        else:
            end_x = self.player.x + math.cos(self.rayAngle) * 50
            end_y = self.player.y + math.sin(self.rayAngle) * 50
        pg.draw.line(screen, (0, 255, 0), (self.player.x, self.player.y), (end_x, end_y))
