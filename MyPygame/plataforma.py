import pygame
from constantes import *
from auxiliar import Auxiliar


class Plataform:
    def __init__(self, x, y,width, height,  type=1,right_collision_width=0):
        self.image_list= Auxiliar.getSurfaceFromSeparateFiles("images/tileset/forest/graveyard/Tiles/Tile ({0}).png",1,25,flip=False,w=width,h=height)
        print(self.image_list)
        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

        self.right_collision_width = right_collision_width
        self.right_collition_rect = pygame.Rect(self.rect)
        self.right_collition_rect = pygame.Rect(self.rect.x + self.rect.width, self.rect.y, right_collision_width, self.rect.height)


    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)

            pygame.draw.rect(screen, (0, 255, 0), self.right_collition_rect)

        
        