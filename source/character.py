######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprite, camera, delta_time, colliding
from map import curr_map, blocks

######################
# COLLISIONS
######################

class collisions:
    def __init__(self):
        self.ground = False
        self.air = False
        self.top_ground = False
        self.bottom_ground = False
        self.left_ground = False
        self.right_ground = False
    def get(self,target):

        self.ground = False
        self.air = False
        self.top_ground = False
        self.bottom_ground = False
        self.left_ground = False
        self.right_ground = False

   #     ground = 40

#        if target.y + target.h < ground: # Air
 #           self.air = True
  #      if target.y + target.h == ground: # On ground
   #         self.ground = True
    #    if target.y + target.h > ground: # Below Ground
     #       self.top_ground = True
 
        for index_y, y in enumerate(curr_map.matrix):
            for index_x, x in enumerate(curr_map.matrix[index_y]):
                if x == "#" or x == "&":
                    if colliding.point(
                        ((index_x*blocks.width) - camera.x),
                        ((index_y*blocks.width) - camera.y),
                        blocks.width,
                        blocks.width,
                        (target.x + target.w) / 2,
                        target.y + target.h
                        ):
                        self.top_ground = True
                        self.air = False

                    if colliding.point(
                        ((index_x*blocks.width) - camera.x),
                        ((index_y*blocks.width) - camera.y),
                        blocks.width,
                        blocks.width,
                        (target.x + target.w) / 2,
                        target.y
                        ):
                        self.bottom_ground = True
                        self.air = False

                    if colliding.point(
                        ((index_x*blocks.width) - camera.x),
                        ((index_y*blocks.width) - camera.y),
                        blocks.width,
                        blocks.width,
                        target.x,
                        (target.y + target.h) / 2
                        ):
                        self.left_ground = True
                        self.air = False

                    if colliding.point(
                        ((index_x*blocks.width) - camera.x),
                        ((index_y*blocks.width) - camera.y),
                        blocks.width,
                        blocks.width,
                        target.x + target.w,
                        (target.y + target.h) / 2
                        ):
                        self.right_ground = True
                        self.air = False

                if x == " ":
                    self.air = True
        
        return [self.ground,self.air,self.top_ground,self.bottom_ground,self.left_ground,self.right_ground]

######################
# SPRITE LIST
######################

class sprite_list:
    def __init__(self):
        self.idle = [
            sprite("player/")
        ]

        self.idle = [
            sprite("player/")
        ]

######################
# CHARACTER
######################

class character:
    def __init__(self):
        #self.sprites = sprite_list()
        #self.sprite_list = self.sprites.idle
        self.sprite = sprite("character/mike/idle.gif")
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
        #camera.x = self.x - ((pygame.display.Info().current_w) / 2)
        #camera.y = (pygame.display.Info().current_h) - (50 / 2)
        camera.x = self.x - ((pygame.display.Info().current_w) / 2)
        camera.y = self.y - ((pygame.display.Info().current_h) / 2)
        #camera.y = pygame.display.Info().current_h - 5 
        self.controller(events)
        self.physics()
        self.render()

    def render(self):
        if self.facing == "left":
            flip = False
        if self.facing == "right":
            flip = True
        self.sprite.render(
            flip,
            (self.x - camera.x),
            (self.y - camera.y),
            self.w,
            self.h
        )

    def physics(self):

        if self.x_velocity > 0:
            self.x_velocity -= 1
        if self.x_velocity < 0:
            self.x_velocity += 1
        if math.floor(self.x_velocity) == 0:
            self.x_velocity = 0

        if self.collisions.get(self)[4]: # left Ground
            if self.x_velocity > 0:
                print("colliding block::left")
                self.x_velocity = 0

        if self.collisions.get(self)[5]: # right Ground
            if self.x_velocity < 0:
                print("colliding block::right")
                self.x_velocity = 0
        
        self.x += self.x_velocity+(self.x_velocity*delta_time)

    #    if self.collisions.get(self)[1]: # Air
     #       self.y_velocity -= 0.5

        if self.collisions.get(self)[2]: # top Ground
            if self.y_velocity < 0:
                print("standing on top")
                self.y_velocity = 0

        if self.collisions.get(self)[3]: # bottom Ground
            if self.y_velocity > 0:
                print("hitting bottom of block")
                self.y_velocity = 0

        if self.collisions.get(self)[0]: # On ground
            self.y_velocity = 0

        self.y -= self.y_velocity+(self.y_velocity*delta_time)
            
    def controller(self,events):
        if events[0][pygame.K_w]:
            #self.y_velocity = self.jump
            self.y -= self.jump
        if events[0][pygame.K_a]:
            self.facing = "left"
            self.x_velocity = -self.speed
        if events[0][pygame.K_s]:
            #self.y_velocity = -self.jump
            self.y += self.jump
        if events[0][pygame.K_d]:
            self.facing = "right"
            self.x_velocity = self.speed

player = character()