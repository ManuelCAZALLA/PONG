import pygame as pg
class Pelota :
    def __init__(self,pos_x,pos_y,radio = 10,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        
    def dibujar (self,pantalla) :
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)   
        
class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=100,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
    
    def dibujar (self,pantalla) :
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.w//2),self.w,self.h) )        