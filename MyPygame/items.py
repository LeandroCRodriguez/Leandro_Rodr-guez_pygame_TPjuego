import pygame
from constantes import *
from auxiliar import Auxiliar
 
class Items():
    def __init__(self,x,y,width,height,frame_rate_ms):
        self.coin_list = Auxiliar.getSurfaceFromSeparateFiles("images/gem_sapphire/coin ({0}).png",1,2,flip=False,w=width,h=height) 
        self.frame = 0
        self.image = self.coin_list[self.frame]        
        self.rect = self.image.get_rect()     
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.bandera_disappear = False #DESAPARECER FRUTA
       
    def draw(self,screen):
        self.image = self.coin_list[self.frame]            
        screen.blit(self.image,self.rect)

    def update(self,delta_ms):
        self.do_animation(delta_ms)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.coin_list) - 1):
                self.frame += 1 
                # print(self.frame)
            else: 
                self.frame = 0
                
    def collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            self.bandera_disappear = True
            print("colisiono fruta y player")
