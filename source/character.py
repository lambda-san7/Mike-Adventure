######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprites, camera

######################
# SPRITE LIST
######################

class sprite_list:
    def __init__(self):
        self.idle = [
            sprites.new("player/")
        ]

        self.idle = [
            sprites.new("player/")
        ]

######################
# CHARACTER
######################

class character:
    def __init__(self):
        #self.sprites = sprite_list()
        #self.sprite_list = self.sprites.idle
        self.sprite = sprites.new("player/testing.png")
        self.x = 0
        self.y = 0
        self.w = 10
        self.h = 10
        self.speed = 0.25
        self.x_velocity = 0
        self.facing = "right"
 
    def handle(self,events):
        self.controller(events)
        self.physics()
        self.render()

    def render(self):
        flip = False
        match self.facing:
            case "left":
                flip = True
        window.blit(
            pygame.transform.scale(
                pygame.transform.flip(
                    self.sprite,flip,False
                ),
                (self.w * camera.scale, self.h * camera.scale)
            ),
            ((self.x - camera.x) * camera.scale,(self.y - camera.y) * camera.scale)
        )

    def physics(self):
        self.x += self.x_velocity
        if self.x_velocity > 0:
            self.x_velocity -= 1
        if self.x_velocity < 0:
            self.x_velocity += 1
        if math.floor(self.x_velocity) == 0:
            self.x_velocity = 0
            
    def controller(self,events):
        if events[0][pygame.K_w]:
            pass
        if events[0][pygame.K_a]:
            self.x_velocity = -self.speed * camera.scale
            print()
        if events[0][pygame.K_s]:
            pass
        if events[0][pygame.K_d]:
            self.x_velocity = self.speed * camera.scale

player = character()