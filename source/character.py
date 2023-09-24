######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprites, camera, delta_time

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
        self.sprite = sprites.new("character/mike/idle.gif")
        self.x = 0
        self.y = 0
        self.w = 10
        self.h = 10
        self.speed = 2
        self.jump = 5
        self.x_velocity = 0
        self.y_velocity = 0
        self.facing = "right"
 
    def handle(self,events):
        self.controller(events)
        self.physics()
        self.render()

    def render(self):
        if self.facing == "left":
            flip = False
        if self.facing == "right":
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
        self.x += self.x_velocity+(self.x_velocity*delta_time)

        if self.x_velocity > 0:
            self.x_velocity -= 1
        if self.x_velocity < 0:
            self.x_velocity += 1
        if math.floor(self.x_velocity) == 0:
            self.x_velocity = 0
        
        self.y -= self.y_velocity+(self.y_velocity*delta_time)

        ground = 40

        if self.y + self.h < ground: # Air
            self.y_velocity -= 0.5
        if self.y + self.h == ground: # On ground
            self.y_velocity = 0
        if self.y + self.h > ground: # Below Ground
            self.y = ground - self.h
            self.y_velocity = 0
            
    def controller(self,events):
        if events[1] == "w":
            self.y_velocity = self.jump
        if events[0][pygame.K_a]:
            self.facing = "left"
            self.x_velocity = -self.speed
            print()
        if events[0][pygame.K_s]:
            pass
        if events[0][pygame.K_d]:
            self.facing = "right"
            self.x_velocity = self.speed

player = character()