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

PPM = 80
VIEW = 1000,600
FPS = 40
TIME_STEP = 1.0/FPS
WHITE = (255,255,255)
BLACK = (0,0,0)

game = True
running = True
art = False

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

world = world(gravity=(0,-10), doSleep=True)

things = []

ground = Thing(world,ground_art,(6,.3),0,BOX,static=True)
things.append(ground)
greatblue = Thing(world,greatblue_art,(5,5),-10,CIRCLE,radius=.3)
things.append(greatblue)



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
