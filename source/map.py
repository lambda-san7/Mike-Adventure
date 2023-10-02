######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprite, camera, delta_time

######################
# BLOCKS
######################

class blocks_class:
    def __init__(self):
        self.grass = sprite("grass.gif")
        self.dirt = sprite("dirt.gif")

class backdrops_class:
    def __init__(self):
        self.sky = sprite("sky.gif")

blocks = blocks_class()
backdrops = backdrops_class()

######################
# MAP
######################

class map:
    def __init__(self):
        self.matrix = [
            [" "," "," "," "," "," "," "," "," "," "," "," "],
            [" "," ","#"," "," "," "," ","#"," "," "," "," "],
            [" "," "," "," "," "," ","#","&"," "," "," "," "],
            [" "," "," "," "," ","#","&","&"," "," "," "," "],
            ["#","#","#","#","#","&","&","&","#","#","#","#"],
        ]
    def backdrop(self):
        backdrops.sky.render(
            False,
            0,
            0,
            pygame.display.Info().current_w,
            pygame.display.Info().current_w
        )
    def render(self):
        for index_y, y in enumerate(self.matrix):
            for index_x, x in enumerate(self.matrix[index_y]):
                if x == " ":
                    continue
                if x == "#":
                    blocks.grass.render(
                        False,
                        ((index_x*10) - camera.x) * camera.scale,
                        ((index_y*10) - camera.y) * camera.scale,
                        10 * camera.scale,
                        10 * camera.scale
                    )
                if x == "&":
                    blocks.dirt.render(
                        False,
                        ((index_x*10) - camera.x) * camera.scale,
                        ((index_y*10) - camera.y) * camera.scale,
                        10 * camera.scale,
                        10 * camera.scale
                    )

testing = map()

curr_map = testing