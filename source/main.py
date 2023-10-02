######################
# IMPORTS
######################

import pygame
import defaults
from defaults import window, clock, running, event, fps, text, button
from character import player
from map import curr_map

######################
# SCENES
######################

def menu(events):
    window.fill((50,50,50))
    y_coor = 200
    text(32,"Mike's Adventure",(255,255,255)).render(True,y_coor)
    y_coor += 50
    match button(True,True,"Play",(255,255,0)).render(True,y_coor,events):
        case "clicked":
            print("clicked")
        case "hover":
            button(True,True,"Play",(255,255,150)).render(True,y_coor,events)
    y_coor += 25
    match button(True,True,"Exit",(255,255,0)).render(True,y_coor,events):
        case "clicked":
            pygame.quit()
        case "hover":
            button(True,True,"Exit",(255,255,150)).render(True,y_coor,events)
 
def game(events):
    window.fill((50,50,50))
    curr_map.backdrop()
    player.handle(events)
    curr_map.render()

scene = game

######################
# LOOP
######################

while 1:
    defaults.delta_time = clock.tick(fps)/1000
    events = event()
    scene(events)
    pygame.display.update()