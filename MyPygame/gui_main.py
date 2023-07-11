import pygame
from pygame.locals import *
import pygame.mixer #Musica
import sys
from constantes import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import *
from gui_form_menu_game_l3 import *


flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16) # CREAR SUPERFICIE (PANTALLA)
pygame.init()  #INICIA PYGAME
clock = pygame.time.Clock() #RELOJ DE PYGAME
#Musica

pygame.mixer.music.load("music/intro_2.mp3")
pygame.mixer.music.play(loops=-1)
#Musica
form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=C_LILA,color_border=C_PEACH,active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)


                             
while True:     
    lista_eventos = pygame.event.get() #RECORRO LA LISTA DE EVENTOS
    for event in lista_eventos:
        if event.type == pygame.QUIT: #detecta si salis del programa
            pygame.quit()
            sys.exit()  

    if form_game_L1.nivel_completado or form_game_L2.nivel_2_completado or form_game_L3.nivel_3_completado:
        print("Perdi y estoy dentro del menu")
        form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=C_LILA,color_border=(255,0,255),active=True)
        form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
        form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

        form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
        form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
        form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)        

            

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS) #CUANTOS MILISEGUNDOS PASAN DESDE LA ULTIMA VEZ QUE ENTRE AL WHILE

    aux_form_active = Form.get_active()   #ACTIVA EL NIVEL CORRESPONDIENTE
    if(aux_form_active != None):
        aux_form_active.update(lista_eventos,keys,delta_ms)
        aux_form_active.draw()



    pygame.display.flip() #MOSTRARLE AL USUARIO LA ACTUALIZACIÓN HASTA ESE MOMENTO




    


  



