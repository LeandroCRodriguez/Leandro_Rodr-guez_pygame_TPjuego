import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *


class Button(Widget): #MASTER SUPERF,POS X,Y/ANCHO W ALTO H/BACK, COLOR FONDO/COLOR BORDE/TEXTO, FUENTE, TAMAÑO Y COLOR 
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None,text="Button",font="Arial",font_size=14,font_color=C_BLUE,on_click=None,on_click_param=None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click  #CUANDO HACEN CLICK AL BOTON
        self.on_click_param = on_click_param #PARAMETRO DEL BOTON
        self.state = M_STATE_NORMAL
        self.render()  
        
    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) #PINTA LA SUP QUE REPRESENTA EL BOTON
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB)  #PINTA LA SUP QUE REPRESENTA EL BOTON

    def update(self,lista_eventos):#LE LLEGA LA LISTA DE EVENTOS DE PYGAME.
        mousePos = pygame.mouse.get_pos() # DETECTA LA POS DEL MOUSE
        self.state = M_STATE_NORMAL   #MOUSE = 0
        if self.slave_rect_collide.collidepoint(mousePos): #DETERMINA SI LA POS DEL MOUSE ESTA DENTRO DEL RECT
            if(pygame.mouse.get_pressed()[0]): #PREGUNTA SI EL BOTON ESTA APRETADO. (NO DEBERIA SER AL REVES?)
                self.state = M_STATE_CLICK  #MOUSE = 3
            else:
                self.state = M_STATE_HOVER #MOUSE = 1
              
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN: #DETECTA SI SE HIZO CLICK EN EL MOUSE
                if(self.slave_rect_collide.collidepoint(evento.pos)):  #PREGUNTA SI EL RECT DE LA ESCLAVA, COLISIONA (COLLIDEPONIT) CON EL CLICK DEL MOUSE
                    self.on_click(self.on_click_param)    #LLAMO A LA FUNCION ON_CLICK Y LE ENVÍO EL PARAMETRO

        self.render()

    

