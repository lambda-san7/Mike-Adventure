######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprites, camera, delta_time
from map import curr_map

######################
# COLLISIONS
######################

class collisions:
    def __init__(self):
        self.ground = False
        self.air = False
        self.under_ground_x = False
        self.under_ground_y = False
    def get(self,target):

        self.ground = False
        self.air = False
        self.under_ground_x = False
        self.under_ground_y = False

        ground = 40

        if target.y + target.h < ground: # Air
            self.air = True
      #  if target.y + target.h == ground: # On ground
       #     self.ground = True
        #if target.y + target.h > ground: # Below Ground
         #   self.under_ground_y = True

        for index_y, y in enumerate(curr_map.matrix):
            for index_x, x in enumerate(curr_map.matrix[index_y]):
                if ((target.x + target.w >= index_x) and
                    (target.x <= index_x + 10) and
                    (target.y + target.h >= index_y) and
                    (target.y <= index_y + 10)):
                        self.under_ground_y = True
        
        return [self.ground,self.air,self.under_ground_x,self.under_ground_y]

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
        self.collisions = collisions()
 
    def handle(self,events):
        camera.x = self.x - ((pygame.display.Info().current_w / camera.scale) / 2)
        camera.y = self.y - ((pygame.display.Info().current_h / camera.scale) / 2)
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
        if self.collisions.get(self)[3]:
            self.x -= self.x_velocity+(self.x_velocity*delta_time)

        if self.x_velocity > 0:
            self.x_velocity -= 1
        if self.x_velocity < 0:
            self.x_velocity += 1
        if math.floor(self.x_velocity) == 0:
            self.x_velocity = 0
        
        self.y -= self.y_velocity+(self.y_velocity*delta_time)

        ground = 40
        
        if self.collisions.get(self)[0]: # On ground
            self.y_velocity = 0

        if self.collisions.get(self)[1]: # Air
            self.y_velocity -= 0.5

        if self.collisions.get(self)[3]: # Below Ground
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