import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from items import *
import pygame.mixer #Musica
from boss import *
from trampas import *

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        # --- GUI WIDGET ---######CREACION DE BOTONES###### MASTER SUPERF,POS X,Y/ANCHO W ALTO H/BACKGR, COLOR FONDO/COLOR BORDE/IMAGEN FONDO/ON_CLICK LLAMA A LA FUNC. APRETO O NO EL BOT/PARAM DEL BOTON/TEXTO, FUENTE, TAMAÑO Y COLOR 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Sand/Buttons/Button_L_08.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Consolas",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Sand/Buttons/Button_L_08.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Consolas",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Sand/Buttons/Button_L_08.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Consolas",font_size=30,font_color=C_WHITE)
        self.pb_lives = ProgressBar(master=self,x=600,y=0,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Sand/Bars/Bar_Background03.png",image_progress="images/gui/set_gui_01/Sand/Bars/Bar_Background03.png",value = 5, value_max=5)
        
        self.paused = False
        self.tiempo_transcurrido = 0
        #bala
        self.tiempo_transcurrido_shoot_bullet = 0    
        self.music_arrow = pygame.mixer.Sound("music/arrow.wav")   
        #bala

        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/set_bg_01/forest/2_game_background.png")

        self.player_1 = Player(x=0,y=490,speed_walk=10,speed_run=12,gravity=14,jump_power=70,frame_rate_ms=100,move_rate_ms=50,jump_height=250,p_scale=0.2,interval_time_jump=300)
        
        self.enemy_list = []
        self.enemy_list.append(Boss(x=500,y=0,speed_walk=10,speed_run=12,gravity=14,jump_power=150,frame_rate_ms=100,move_rate_ms=50,jump_height=250,p_scale=0.2,interval_time_jump=300))


        self.plataform_list = []
        self.plataform_list.append(Plataform(x=0,y=200,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=50,y=200,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=100,y=200,width=50,height=50,type=2))
        self.plataform_list.append(Plataform(x=150,y=200,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=200,y=200,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=250,y=200,width=50,height=50,type=2))              
        self.plataform_list.append(Plataform(x=200,y=430,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=250,y=430,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=300,y=430,width=50,height=50,type=2))
        self.plataform_list.append(Plataform(x=400,y=300,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=450,y=300,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=500,y=300,width=50,height=50,type=2))   
        self.plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=5))
        self.plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=6))
        self.plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=7))
        self.plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=8))

        self.trampa_list = []
        self.trampa_list.append(Trampas(x=80,y=150,width=40,height=40,frame_rate_ms = 20))
        self.trampa_list.append(Trampas(x=300,y=390,width=40,height=40,frame_rate_ms = 20))
        self.trampa_list.append(Trampas(x=500,y=250,width=40,height=40,frame_rate_ms = 20))
        self.trampa_list.append(Trampas(x=900,y=310,width=40,height=40,frame_rate_ms = 20))
        

        self.bullet_list = []



        #Musica
        pygame.mixer.music.stop()
        self.music_find = pygame.mixer.Sound("music/mus_find.wav")
        self.music_hurt = pygame.mixer.Sound("music/hurt_player.wav")      
        # #Musica        
        #Image win or lose
        self.image_game_over = pygame.image.load("images/gui/set_gui_01/Comic/Text/GAME_OVER.png")
        self.image_win = pygame.image.load("images/gui/set_gui_01/Comic/Text/WINNER.png")
        #Image win or lose
        self.play_intro_music()
        self.nivel_3_completado = False
        self.tiempo_transcurrido_win_lose = 0


    def play_intro_music(self):
        pygame.mixer.music.load("music/boss.mp3")
        pygame.mixer.music.play(loops=-1)

    def play_win_music(self):
        self.music_win = pygame.mixer.music.load("music/win.mp3")
        pygame.mixer.music.play(loops=-1)

    def play_lose_music(self):
        self.music_lose = pygame.mixer.music.load("music/lose.OGG")
        pygame.mixer.music.play(loops=-1)
#Musica  
      

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
        
    def paused_mode(self,delta_ms): #Me quedo horrible pero funciona
        self.tiempo_transcurrido += delta_ms
        if(self.tiempo_transcurrido >= 100):
            self.tiempo_transcurrido = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                if self.paused:
                    self.paused = False  # Salir del modo pausa
                    self.play_intro_music()                     
                else:
                    self.paused = True  # Entrar al modo pausa
                    pygame.mixer.music.load("music/paused.mp3")
                    pygame.mixer.music.play()


    def update(self, lista_eventos,keys,delta_ms): 
        keys = pygame.key.get_pressed()            
        if keys[pygame.K_p]:              
            self.paused_mode(delta_ms)
            return            
        elif not self.paused:
            self.tiempo_transcurrido += delta_ms
            for aux_widget in self.widget_list:
                aux_widget.update(lista_eventos)

            for bullet_element in self.bullet_list:
                bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)    
                    
            for trampa in self.trampa_list:
                trampa.update(delta_ms)  
                trampa.collision(self.player_1.rect)  
                if trampa.bandera_colision:
                    self.player_1.lives -= 1
                    self.trampa_list.remove(trampa) 
                    self.music_hurt.play()    
            
            for enemy_element in self.enemy_list:
                enemy_element.update(delta_ms,self.plataform_list) 
                if enemy_element.collision(self.player_1.rect,delta_ms) and enemy_element.is_dead == False:
                    self.tiempo_transcurrido += delta_ms
                    if(self.tiempo_transcurrido >= COLISION_ENEMY):
                        self.tiempo_transcurrido = 0
                        self.player_1.lives -= 1
                        self.player_1.hurt(True) #LLAMO AL HURT EN MI METODO PRINCIPAL
                        self.music_hurt.play()
                self.tiempo_transcurrido_shoot_bullet += delta_ms
                if(self.tiempo_transcurrido_shoot_bullet >= TIME_SHOOT_BOSS):
                    self.tiempo_transcurrido_shoot_bullet = 0
                    self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images/flecha_der.png",frame_rate_ms=100,move_rate_ms=20,width=150,height=35))
                    self.music_arrow.play()

                       

            self.player_1.events(delta_ms,keys,self.bullet_list)
            self.player_1.update(delta_ms,self.plataform_list)

            self.pb_lives.value = self.player_1.lives  


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)

        for trampa in self.trampa_list:
            trampa.draw(self.surface)            

        
        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)


        if self.paused:#PAUSA
            font = pygame.font.SysFont("Consolas", 50)
            text = font.render("PAUSE", True, (255, 255, 255))
            text_rect = text.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
            self.surface.blit(text, text_rect)
            
        font = pygame.font.SysFont("Consolas", 30) #TIEMPO
        tiempo_texto = font.render("Tiempo: " + str(self.tiempo_transcurrido / 1000), True, (255, 255, 255))
        self.surface.blit(tiempo_texto, (50, 50))
        if self.tiempo_transcurrido / 1000 >= TIEMPO_LIMITE or self.player_1.lives == 0: 
            self.surface.blit(self.image_game_over, (50, 200)) 
            self.play_lose_music()
            self.tiempo_transcurrido_win_lose += 50
            if(self.tiempo_transcurrido_win_lose >= TIME_WIN_LOSE):
                self.tiempo_transcurrido_win_lose = 0                
                self.nivel_3_completado = True 
        elif self.tiempo_transcurrido / 1000 <= TIEMPO_LIMITE:
            all_dead = True
            for enemy_element in self.enemy_list:
                if not enemy_element.is_dead:
                    all_dead = False
                    break
            if all_dead:                    
                self.surface.blit(self.image_win, (150, 200))
                self.play_win_music() 
                self.tiempo_transcurrido_win_lose += 20
                if(self.tiempo_transcurrido_win_lose >= TIME_WIN_LOSE):
                    self.tiempo_transcurrido_win_lose = 0                
                    self.nivel_3_completado = True
                
        self.player_1.draw(self.surface) 
