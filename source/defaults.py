######################
# IMPORTS
######################

import pygame
import os
import time
import random

pygame.init()

##############################
# FILE
##############################

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

######################
# WINDOW
######################

window = pygame.display.set_mode((900,600),pygame.RESIZABLE)

#pygame.mouse.set_visible(False)

running = True

######################
# TIME
######################

clock = pygame.time.Clock()

fps = 60

delta_time = clock.tick(fps)/1000

######################
# EVENT
######################

def event():
    key_down = None
    key_up = None
    mouse_down = None
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            key_down = pygame.key.name(i.key)
        if i.type == pygame.KEYUP:
            key_up = pygame.key.name(i.key)
        if i.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = i.button
    return [pygame.key.get_pressed(),key_down,key_up,mouse_down]
    
######################
# TEXT
######################

class text:
    def __init__(self, size, text, color):
        self.font = pygame.font.Font(f"{dir_path}/assets/font.fon",size)
        self.text = f" {text} "
        self.color = color
        self.object = self.font.render(self.text, True, self.color)
        self.w = self.object.get_size()[0]
        self.h = self.object.get_size()[1]
    def render(self,x,y):
        if x == True:
            x = center.x(self)
        if y == True:
            y = center.y(self) 
        self.border(x,y)
        window.blit(
            self.font.render(self.text, True, self.color),
            (x,y)
        )
    def border(self,x,y):
        text = self.font.render(self.text, True, (0,0,0))

        window.blit(text,(x,y + 2))
        window.blit(text,(x,y - 2))
        window.blit(text,(x - 2,y))
        window.blit(text,(x + 2,y))

        window.blit(text,(x + 2,y + 2))
        window.blit(text,(x - 2,y + 2))
        window.blit(text,(x - 2,y - 2))
        window.blit(text,(x + 2,y - 2))

######################
# BUTTON
######################

class button:
    def __init__(self,w,h,button_text,color,font_color=(255,255,255)):
        self.text = text(32,button_text,font_color)
        if w == True:
            w = self.text.object.get_size()[0]
        if h == True:
            h = self.text.object.get_size()[1]
        self.w = w
        self.h = h
        self.color = color
    def render(self,x,y,events):
        if x == True:
            x = center.x(self)
        if y == True:
            y = center.y(self) 
        self.border(x,y)
        pygame.draw.rect(window, self.color, pygame.Rect(x, y, self.w, self.h))
        self.text.render(x,y)
        return self.click_and_hover(x,y,self.w,self.h,events[3])
    def border(self,x,y):
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x, y + 2, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x, y - 2, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x - 2, y, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x + 2, y, self.w, self.h))

        pygame.draw.rect(window, (0,0,0), pygame.Rect(x + 2, y + 2, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x - 2, y + 2, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x - 2, y - 2, self.w, self.h))
        pygame.draw.rect(window, (0,0,0), pygame.Rect(x + 2, y - 2, self.w, self.h))

    def click_and_hover(self,x,y,w,h,events):
        if((pygame.mouse.get_pos()[0] >= x) and
            (pygame.mouse.get_pos()[1] >= y) and
            (pygame.mouse.get_pos()[0] <= x + w) and
            (pygame.mouse.get_pos()[1] <= y + h)):
            if events[3] == 1:
                return "clicked"
            return "hover"
        
######################
# NOTIFICATIONS
######################

notifications = []

class notification:
    def __init__(self,text,color,seconds):
        self.element = button(True,True,text,color,font_color=(255,255,255))
        self.time = seconds*100
        notifications.append(self)
    def render(self,events):
        self.time -= 1
        if self.time == 0:
            notifications.remove(self)
        match self.element.render(True,10,events[3]):
            case "clicked":
                notifications.remove(self)
            case "hover":
                pass

#########################
# UTILITY
#########################

class center:
    def x(object):
        return ((pygame.display.Info().current_w / 2) - (object.w / 2))
    def y(object):
        return ((pygame.display.Info().current_h / 2) - (object.h / 2))
    
#########################
# SPRITES
#########################

class sprite:
    def __init__(self,file):
        self.img = pygame.image.load(f"{dir_path}/assets/{file}").convert_alpha()
    def render(self,flip,x,y,w,h):
        window.blit(
            pygame.transform.scale(
                pygame.transform.flip(
                    self.img,flip,False
                ),
                (w, h)
            ),
            (x,y)
        )

#########################
# CAMERA
#########################

class camera:
    x = 0
    y = 0
    scale = 5

#########################
# CURSOR
#########################

#class cursor_class:
#    def __init__(self):
#        self.default = sprites.new("cursor.gif")
#        self.curr = self.default
#    def render(self):
#        sprites.render(self.curr, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 20, 20)

#cursor = cursor_class()

#########################
# COLLISION
#########################

class colliding:
    def point(x,y,w,h,px,py):
        if ((px <= x + w) and
            (px >= x) and
            (py <= y + h) and
            (py >= y)
        ):
            return True
        return False