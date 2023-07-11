import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet
import pygame.mixer #Musica

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:

        #IMAGENES DE MI PERSONAJE
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/1_IDLE_({0}).png",1,4,flip=False,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/1_IDLE_({0}).png",1,4,flip=True,scale=p_scale)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/4_JUMP_({0}).png",1,4,flip=False,scale=p_scale)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/4_JUMP_({0}).png",1,4,flip=True,scale=p_scale)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/3_RUN_({0}).png",1,4,flip=False,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/3_RUN_({0}).png",1,4,flip=True,scale=p_scale)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/5_ATTACK_({0}).png",1,4,flip=False,scale=p_scale,repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/5_ATTACK_({0}).png",1,4,flip=True,scale=p_scale,repeat_frame=2)
        self.hurt_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/6_HURT_({0}).png",1,4,flip=False,scale=p_scale,repeat_frame=1)
        self.hurt_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/6_HURT_({0}).png",1,4,flip=True,scale=p_scale,repeat_frame=1)
        self.die_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/7_DIE_({0}).png",1,4,flip=False,scale=p_scale,repeat_frame=1)
        self.die_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/warrior_woman_03/7_DIE_({0}).png",1,4,flip=True,scale=p_scale,repeat_frame=1)
        
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r  #DIRECCIÓN INICIAL, SE QUEDA QUIETO A LA DER
        self.direction = DIRECTION_R  #DIRECCIÓN INICIAL MIRA A LA DER
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_hurt = False    #Hurt
        self.is_dead = False

        self.tiempo_transcurrido_shoot = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.music_arrow = pygame.mixer.Sound("music/arrow.wav")
        self.dead_timer = 0
        self.dead_frame_duration = 500
        self.dead_frame = 0 
        self.music_hurt = pygame.mixer.Sound("music/hurt_player.wav")   


    def walk(self,direction):  #METODO PARA CAMINAR (DER O IZQ)
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction #CONSERVO LA DIRECCION HACIA DONDE SE ESTA MOVIENDO. QUEDA QUIETO EN ESA DIREC
            if(direction == DIRECTION_R): #PREGUNTO SI LA DIRECCION ES A LA DER
                self.move_x = self.speed_walk  #MOVIMIENTO 
                self.animation = self.walk_r   #ANIMACIÓN
            else:                              #SINO CAMINO A LA IZQ
                self.move_x = -self.speed_walk  #MOVIMIENTO 
                self.animation = self.walk_l   #ANIMACIÓN

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):#SI ESTOY DISPARANDO Y NO ESTOY SALTANDO NI CAYENDO
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l 
      

    def receive_shoot(self):
        print("Estoy en shott")
        self.hurt(True)
        self.lives -= 1
        self.music_hurt.play()
        if(self.lives == 0):
            self.is_dead = True
 

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R): #SI ESTA SALTANDO A LA DER
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)  #SI ESTA SALTANDO A LA IZQ
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0 
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

#Hurt
    def hurt(self,on_off = True):
        print("Estoy en hurt") #Llego acá pero no me genera la imagen hurt en el juego
        if(on_off and self.is_hurt == False and self.is_fall == False):            
            if(self.direction == DIRECTION_R): 
                self.animation = self.hurt_r
                print("Estoy en hurt dentro del if") 
            else:
                self.animation = self.hurt_l
            self.frame = 0 
            self.is_hurt = True
        if(on_off == False):
            self.is_hurt = False
            self.stay()
#Hurt


    def stay(self):
        if(self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R): #SI ESTA QUIETO A LA DER
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l  #SI ESTA QUIETO A LA IZQ
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        if self.is_dead:
            return
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if self.is_dead:
                if self.direction == DIRECTION_L:
                    if self.dead_frame < len(self.die_l) -1:
                        self.dead_frame += 1
                    else:
                        self.dead_frame = len(self.die_l) - 1    
                else:
                    if self.dead_frame < len(self.die_r) -1:
                        self.dead_frame += 1
                    else:
                        self.dead_frame = len(self.die_r) - 1  
            else:
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else: 
                    self.frame = 0
     
 
    def update(self,delta_ms,plataform_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        if self.is_dead:
            if self.direction == DIRECTION_L:
                self.image = self.die_l[self.dead_frame]
            else:
                self.image = self.die_r[self.dead_frame]
        else:
            self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

        
        font = pygame.font.Font(None, 50)  # Fuente para el texto de las vidas
        text = font.render("Vidas: " + str(self.lives), True, C_BLACK)  # Renderiza el texto de las vidas
        screen.blit(text, (500, 60))  # Dibuja el texto en la posición (10, 10) de la pantalla
        font = pygame.font.Font(None, 50)  # Fuente para el texto de la puntuacion
        text = font.render("Puntuación: " + str(self.score), True, C_BLACK)  # Renderiza el texto de la puntuacion
        screen.blit(text, (700, 60))  # Dibuja el texto en la posición (10, 10) de la pantalla

        

    def events(self,delta_ms,keys,bullet_list):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
                self.music_jump =pygame.mixer.Sound("music/jump.WAV")
                self.music_jump.play()


        if(keys[pygame.K_a]):
            self.tiempo_transcurrido_shoot += delta_ms
            if(self.tiempo_transcurrido_shoot >= SHOOT_MS):
                self.tiempo_transcurrido_shoot = 0
                if(self.direction == DIRECTION_R):
                    bullet_list.append(Bullet(self,x_init=self.rect.x+50,y_init=self.rect.y+80,x_end=ANCHO_VENTANA,y_end=self.rect.y+80, speed=50,path="images/flecha_der.png",frame_rate_ms=150,move_rate_ms=50,width=50,height=8))
                    self.music_arrow.play()
                else:
                    bullet_list.append(Bullet(self,x_init=self.rect.x+50,y_init=self.rect.y+80,x_end=0,y_end=self.rect.y+80, speed=50,path="images/flecha_izq.png",frame_rate_ms=150,move_rate_ms=50,width=50,height=8))
                    self.music_arrow.play()  




  