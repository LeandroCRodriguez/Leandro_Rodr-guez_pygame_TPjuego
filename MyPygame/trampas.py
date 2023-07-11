import pygame
from constantes import *
from auxiliar import Auxiliar
 
class Trampas():
    def __init__(self,x,y,width,height,frame_rate_ms):
        self.trampas_list = Auxiliar.getSurfaceFromSeparateFiles("images/beaker/beaker__({0}).png",0,1,flip=False,w=width,h=height) 
        self.frame = 0
        self.image = self.trampas_list[self.frame]        
        self.rect = self.image.get_rect()     
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.bandera_colision = False
       
    def draw(self,screen):
        self.image = self.trampas_list[self.frame]            
        screen.blit(self.image,self.rect)

    def update(self,delta_ms):
        self.do_animation(delta_ms)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.trampas_list) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    def collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            self.bandera_colision = True
            print("colisiono trampa y player")
