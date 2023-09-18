######################
# IMPORTS
######################

import pygame
from defaults import window, clock, running, event, fps, text, button
from character import player

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
    player.handle(events)

scene = game

######################
# LOOP
######################

while running:
    clock.tick(fps)
    events = event()
    window.fill((0,0,0))
    scene(events)
    pygame.display.update()