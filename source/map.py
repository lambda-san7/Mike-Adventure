######################
# IMPORTS
######################

import pygame
import math
from defaults import window, sprites, camera, delta_time

######################
# CHARACTER
######################

class map:
    def __init__(self):
        self.ground = sprites.new("grass.gif")
        self.matrix = [
            [" "," "," "," "," "," "," "," ",],
            [" "," "," "," "," "," "," ","#",],
            [" "," "," "," "," "," ","#","#",],
            [" "," "," "," "," ","#","#","#",],
            ["#","#","#","#","#","#","#","#",],
        ]
    def render(self):
        for index_y, y in enumerate(self.matrix):
            for index_x, x in enumerate(self.matrix[index_y]):
                if x == " ":
                    continue
                if x == "#":
                    window.blit(
                        pygame.transform.scale(
                            self.ground,
                            (10 * camera.scale, 10 * camera.scale)
                        ),
                        (((index_x*10) - camera.x) * camera.scale,((index_y*10) - camera.y) * camera.scale)
                    )

testing = map()

curr_map = testing