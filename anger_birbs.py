import pygame
import random
import Box2D
from Box2D.b2 import (world, polygonShape, circleShape,
    staticBody, dynamicBody, pi, globals)

#TO DO:
# EXAMPLE ART SO I DONT HAVE TO REWRITE DRAW LATER
#DEFINE CLASSES, INIT AND DRAW METHODS FIRST
#CLASSES: BIRD, ENEMY(PIG), SCENERY, LEVEL - WHAT SHOULD SLINGSHOT BE?

#what I learned 9/22:
#rotation is destructive, each rotation should reference the og image
# bird designs must be more circular!!

#bird radius is .2 m standard - ??

from anger_sprites import *

PPM = 100
VIEW = 1000,600
FPS = 40
TIME_STEP = 1.0/FPS
WHITE = (255,255,255)
BLACK = (0,0,0)

game = True
running = True
art = True

rotate = 0

pygame.init()

screen = pygame.display.set_mode((VIEW[0],VIEW[1]),0,32)
pygame.display.set_caption("anger birbs")
clock = pygame.time.Clock()

background_art = pygame.image.load("anger_art/background.png").convert_alpha()
redwing_art = pygame.image.load("anger_art/redwing.png").convert_alpha()
greatblue_art = pygame.image.load("anger_art/greatblue.png").convert_alpha()
blackcap_art = pygame.image.load("anger_art/blackcap.png").convert_alpha()
ground_art = pygame.image.load("anger_art/ground.png").convert_alpha()
log_long_art = pygame.image.load("anger_art/log_long.png").convert_alpha()
log_short_art = pygame.image.load("anger_art/log_short.png").convert_alpha()

world = world(gravity=(0,-10), doSleep=True)

things = []

ground = Thing(world,ground_art,(5,.3),0,BOX,static=True)
things.append(ground)
greatblue = Thing(world,greatblue_art,(8,5),-10,CIRCLE,radius=.25)
things.append(greatblue)
#a_log = Thing(world,log_long_art,(4,5),20,BOX)
#things.append(a_log)

def make_log(pos,rotation,size):
    if size == 0:
        a_log = Thing(world,log_short_art,pos,rotation,BOX)
    elif size == 1:
        a_log = Thing(world,log_long_art,pos,rotation,BOX)
    things.append(a_log)

logs = [((1.5,1.4),90,1),((2.5,1.4),90,1),((2.0,2.4),0,1),((2.25,3.0),90,0),
    ((1.75,3.0),90,0),((2.0,3.4),0,0)]
for log in logs:
    make_log(log[0],log[1],log[2])






while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if art == True:
                    art = False
                elif art == False:
                    art = True
    world.Step(TIME_STEP, 10, 10) #always do before drawing!!
    if art:
        screen.blit(background_art,(0,0))
        for each in things:
            each.draw(screen)
    elif not art:
        screen.fill((0,0,0))
        for each in things:
            each.draw_shape(screen)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
