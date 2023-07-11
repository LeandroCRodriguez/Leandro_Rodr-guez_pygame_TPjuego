import pygame
from pygame.locals import *
from constantes import *

class Widget:#MASTER SUPERF,POS X,Y/ANCHO W ALTO H/BACK, COLOR FONDO/COLOR BORDE/IMAGEN FONDO/TEXTO, FUENTE, TAMAÑO Y COLOR 
    def __init__(self,master_form,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color):
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        if image_background != None: #VALIDACIONES
            self.image_background = pygame.image.load(image_background)
            self.image_background = pygame.transform.scale(self.image_background,(w, h)).convert_alpha()
        else:
            self.image_background = None
        self._text = text  #TEXTO DEL BOTON
        if(self._text != None): #VALIDACIONES
            pygame.font.init()
            self._font_sys = pygame.font.SysFont(font,font_size) #CREO LA FUENTE. FONT, TIPO DE FUENTE/FONT SIZE,TAMAÑO
            self._font_color = font_color #COLOR DE FUENTE


    def render(self):
        
        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA) #CREO SUPERF/ANCH ALTO W H/SRCALPHA TRANSPARENCIA
        self.slave_rect = self.slave_surface.get_rect() #SACO EL REC DE LA SUP
        self.slave_rect.x = self.x  #UBICO AL RECT EN POS X
        self.slave_rect.y = self.y  #UBICO AL RECT EN POS Y
        self.slave_rect_collide = pygame.Rect(self.slave_rect) #SACO EL REC DEL REC DE LA SUP, ESTE ME SIRVE PARA COLISIONAR CON EL EVENTO DEL MOUSE. EL OTRO REC NO
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y

        if self.color_background:
            self.slave_surface.fill(self.color_background)
        
        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))
        
        if(self._text != None):
            #TEXT ES EL TEXTO A RENDERIZAR/FOND_COLOR:COLOR TEXT/COLOR FONDO
            image_text = self._font_sys.render(self._text,True,self._font_color,self.color_background) 
            self.slave_surface.blit(image_text,[ #FUNDO LA IMAGEN EN LA SUP ESCLAVA
                self.slave_rect.width/2 - image_text.get_rect().width/2, #POSICIONAR LA IMAGEN
                self.slave_rect.height/2 - image_text.get_rect().height/2 #POSICIONAR LA IMAGEN
            ])
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def update(self):
        pass

    def draw(self):
        self.master_form.surface.blit(self.slave_surface,self.slave_rect)
        #DIBUJA SUP SLAVE EN SUP MASTER, EL RECT ES LA POS