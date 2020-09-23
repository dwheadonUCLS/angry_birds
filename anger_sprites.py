import pygame
import Box2D
import math
from Box2D.b2 import (world, polygonShape, circleShape,
    staticBody, dynamicBody, pi)

CIRCLE = 0
BOX = 1
PPM = 80

class Thing():
    def __init__(self,world,img,pos,rotation,shape,radius=0,static=False):
        self.img = img
        angle = rotation * (pi/180)
        self.shape = shape
        if static:
            self.body = world.CreateStaticBody(position=(pos),angle=angle)
        else:
            self.body = world.CreateDynamicBody(position=(pos),
                fixedRotation=False,angle=angle)
        if shape == CIRCLE:
                self.fix = self.body.CreateCircleFixture(radius=radius,
                    density=4,friction=0.3,restitution=.3)
                self.radius = radius
        elif shape == BOX:
                dimensions = (self.img.get_rect().width/(2*PPM),
                    self.img.get_rect().height/(2*PPM))
                self.dimensions = dimensions
                self.fix = self.body.CreatePolygonFixture(box=dimensions,
                    density=4,friction=0.3,restitution=.3)
    def draw(self,screen):
        angle = self.body.angle * (180/pi)
        r_img = pygame.transform.rotate(self.img,angle)
        center = self.body.position[0]*PPM,600-(self.body.position[1]*PPM)
        rect = self.img.get_rect(center = center)
        screen.blit(r_img,(rect.topleft))
    def draw_shape(self,screen):
        pos = self.body.position[0]*PPM,600-(self.body.position[1]*PPM)
        if self.shape == BOX:
            width,height = self.dimensions[0]*2*PPM,self.dimensions[1]*2*PPM
            rect =  self.img.get_rect(center = pos)
            pygame.draw.rect(screen,(255,255,255),
                (pos[0]-width/2,pos[1]-height/2,width,height))
        elif self.shape == CIRCLE:
            radius = int(self.radius*PPM)
            pos = int(pos[0]),int(pos[1])
            pygame.draw.circle(screen,(255,255,255),pos,radius)
            x = pos[0]+radius*math.cos(self.body.angle)
            y = pos[1]-radius*math.sin(self.body.angle) 
            point = x,y
            pygame.draw.line(screen,(0,0,0),pos,point)
