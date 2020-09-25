import pygame
import random
import Box2D
from Box2D.b2 import (world, polygonShape, circleShape,
    staticBody, dynamicBody, pi, globals)

#TO DO:
# EXAMPLE ART SO I DONT HAVE TO REWRITE DRAW LATER
#DEFINE CLASSES, INIT AND DRAW METHODS FIRST
#CLASSES: BIRD, ENEMY(PIG), SCENERY, LEVEL - WHAT SHOULD SLINGSHOT BE?


from anger_sprites import *

PPM = 100
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

#need to redo all art at the end
background_art = pygame.image.load("anger_art/background.png").convert_alpha()
redwing_art = pygame.image.load("anger_art/redwing.png").convert_alpha()
greatblue_art = pygame.image.load("anger_art/greatblue.png").convert_alpha()
blackcap_art = pygame.image.load("anger_art/blackcap.png").convert_alpha()
ground_art = pygame.image.load("anger_art/ground.png").convert_alpha()
log_long_art = pygame.image.load("anger_art/log_long.png").convert_alpha()
log_short_art = pygame.image.load("anger_art/log_short.png").convert_alpha()
slingshot_art = pygame.image.load("anger_art/slingshot2.png").convert_alpha()

world = world(gravity=(0,-10), doSleep=True)

things = []
birds = []

ground = Thing(world,ground_art,(5,0),0,BOX,static=True)
things.append(ground)
redwing = Bird(world,redwing_art,(2.2,5),-10,CIRCLE,scale=.8)
things.append(redwing)
birds.append(redwing)
blackcap = Bird(world,blackcap_art,(4,5),-10,CIRCLE,scale=.8)
things.append(blackcap)
birds.append(blackcap)
slingshot = Slingshot(slingshot_art,(1.5,1.1),world,scale = 1)
things.append(slingshot)
#a_log = Thing(world,log_long_art,(4,5),20,BOX)
#things.append(a_log)

def make_log(pos,rotation,size):
    if size == 0:
        a_log = Thing(world,log_short_art,pos,rotation,BOX,scale=.8)
    elif size == 1:
        a_log = Thing(world,log_long_art,pos,rotation,BOX,scale=.8)
    things.append(a_log)

logs = [((8.0,1),90,1),((9.0,1),90,1),((8.5,2),0,1),((8.2,2.5),90,0),
    ((8.7,2.5),90,0),((8.5,3.0),0,0)]
for log in logs:
    make_log(log[0],log[1],log[2])


in_sling = None
time_shot = -1000
clicked = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = pos[0]/PPM,(600-pos[1])/PPM
            if in_sling != None:
                if in_sling.fix.TestPoint(pos):
                    clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            in_sling.launch(screen,world,slingshot)
            birds.remove(in_sling)
            in_sling = None
            time_shot = pygame.time.get_ticks()

    if in_sling == None:
        if len(birds)>0 and pygame.time.get_ticks()-time_shot >= 1000:
            birds[0].load(world,slingshot)
            in_sling = birds[0]
            birds[0].body.awake = False
    else:
        if clicked:
            pos = pygame.mouse.get_pos()
            pos = pos[0]/PPM,(600-pos[1])/PPM
            in_sling.body.transform = (pos,in_sling.body.angle)


    world.Step(TIME_STEP, 10, 10) #always do before drawing!!
    if art:
        screen.fill((147,211,246))
        screen.blit(background_art,(0,-50))
        slingshot.draw(screen)
        for each in things:
            each.draw(screen)
    elif not art:
        screen.fill((0,0,0))
        for each in things:
            each.draw_shape(screen)
        if in_sling != None:
            pygame.draw.line(screen,WHITE,(slingshot.anchora.position[0]*PPM,
                600-slingshot.anchora.position[1]*PPM),
                (in_sling.body.position[0]*PPM,
                600-in_sling.body.position[1]*PPM))
            pygame.draw.line(screen,WHITE,(slingshot.anchorb.position[0]*PPM,
                600-slingshot.anchorb.position[1]*PPM),
                (in_sling.body.position[0]*PPM,
                600-in_sling.body.position[1]*PPM))
        else:
            pygame.draw.line(screen,WHITE,(slingshot.anchora.position[0]*PPM,
                600-slingshot.anchora.position[1]*PPM),
                (slingshot.anchorb.position[0]*PPM,
                600-slingshot.anchorb.position[1]*PPM))

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
