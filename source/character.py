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
        self.under_ground = False
    def get(self,target):

        self.ground = False
        self.air = False
        self.under_ground = False

        ground = 40

        if target.y + target.h < ground: # Air
            self.air = True
        if target.y + target.h == ground: # On ground
            self.ground = True
        if target.y + target.h > ground: # Below Ground
            self.under_ground = True
 
        for index_y, y in enumerate(curr_map.matrix):
            for index_x, x in enumerate(curr_map.matrix[index_y]):
                if x == "#" or x == "&":
                    if ((target.x <= (index_x * 10) + 10) and
                        (target.x + target.w >= (index_x * 10)) and

                        (target.y < (index_y * 10) + 10) and
                        (target.y + target.h > (index_y * 10))
                        ):
                            target.y = (index_y * 10) - target.h
                            target.y_velocity = 0
                            self.ground = True
                if x == " ":
                    pass
        
        return [self.ground,self.air,self.under_ground]

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
        camera.y = 50 / camera.scale
        #camera.y = ((pygame.display.Info().current_h / camera.scale) - (5 * camera.scale))
        print(camera.x)
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

        ground = 40

        self.y -= self.y_velocity+(self.y_velocity*delta_time)

        #print(self.collisions.get(self)[2])        
        
        if self.collisions.get(self)[1]: # Air
            self.y_velocity -= 0.5

        if self.collisions.get(self)[2]: # Below Ground
            self.y = ground - self.h
            self.y_velocity = 0

        if self.collisions.get(self)[0]: # On ground
            self.y_velocity = 0
            
    def controller(self,events):
        if events[1] == "w":
            self.y_velocity = self.jump
        if events[0][pygame.K_a]:
            self.facing = "left"
            self.x_velocity = -self.speed
            #print()
        if events[0][pygame.K_s]:
            pass
        if events[0][pygame.K_d]:
            self.facing = "right"
            self.x_velocity = self.speed

player = character()