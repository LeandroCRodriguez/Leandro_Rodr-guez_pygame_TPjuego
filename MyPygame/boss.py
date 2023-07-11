from player import *
from constantes import *
from auxiliar import Auxiliar
import pygame.mixer 
import random

class Boss():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/WALK/_WALK_({0}).png",0,6,scale=p_scale, enlarge = True)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/WALK/_WALK_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/IDLE/_IDLE_({0}).png",0,6,scale=p_scale, enlarge =  True)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/IDLE/_IDLE_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/DIE/_DIE_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/DIE/_DIE_({0}).png",0,6,scale=p_scale, enlarge =  True)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/JUMP/_JUMP_({0}).png",0,6,scale=p_scale, enlarge =  True)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/JUMP/_JUMP_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/RUN/_RUN_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/RUN/_RUN_({0}).png",0,6,scale=p_scale, enlarge =  True)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/ATTACK/_ATTACK_({0}).png",0,6,flip=True,scale=p_scale, enlarge =  True)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images/knight_axe/ATTACK/_ATTACK_({0}).png",0,6,scale=p_scale, enlarge =  True)
        
        
        self.contador = 0
        self.frame = 0
        self.lives = 50
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
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
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

        self.bandera_colision = False
        #DEAD ANIMACION
        self.dead_timer = 0
        self.dead_frame_duration = 500
        self.is_dead = False
        self.dead_frame = 0
        #DEAD ANIMACION
        self.music_hurt = pygame.mixer.Sound("music/hurt_enemy.wav")
        self.music_dead = pygame.mixer.Sound("music/dead_enemy.wav")
        self.tiempo_transcurrido_move_type = 0

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
        self.tiempo_transcurrido_move += delta_ms  #CADA CIERTOS MS ENTRA AL IF
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            if(not self.is_on_plataform(plataform_list)):
                self.is_fall = True
                self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 30:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.direction = DIRECTION_L
                elif self.contador <= 50:
                    self.move_x = 0
                    self.animation = self.attack_l
                    self.direction = DIRECTION_L
                elif self.contador <= 80:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.direction = DIRECTION_R
                elif self.contador <= 100:
                    self.move_x = 0
                    self.animation = self.attack_r
                    self.direction = DIRECTION_R
                elif self.contador <= 120:
                    self.move_x = -self.speed_run
                    self.animation = self.run_l
                    self.direction = DIRECTION_L
                elif self.contador <= 140:
                    self.move_x = 0
                    self.animation = self.attack_l
                    self.direction = DIRECTION_L
                elif self.contador <= 160:
                    self.move_x = self.speed_run
                    self.animation = self.run_r
                    self.direction = DIRECTION_R
                elif self.contador <= 180:
                    self.move_x = 0
                    self.animation = self.attack_r
                    self.direction = DIRECTION_R
                elif self.contador <= 200:
                    self.move_x = -self.speed_walk
                    self.animation = self.jump_l
                    self.direction = DIRECTION_L
                elif self.contador <= 230:
                    self.move_x = self.speed_walk
                    self.animation = self.jump_r
                    self.direction = DIRECTION_R
                elif self.contador <= 240:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l 
                    self.direction = DIRECTION_L
                else:
                    self.contador = 0
                self.contador += 1
                    
                 
    
    def is_on_plataform(self, plataform_list):
        retorno = False
        
        if self.ground_collition_rect.bottom >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in plataform_list:
                if self.ground_collition_rect.colliderect(plataforma.ground_collition_rect):
                    retorno = True
                    break                 
        return retorno


    def do_animation(self, delta_ms):                         
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0        
            if self.is_dead:   
                if(self.direction == DIRECTION_R): 
                    print("muerte lado derecho")        
                    if self.dead_frame < len(self.dead_r) - 1:
                        self.dead_frame += 1
                    else:
                        self.dead_frame = len(self.dead_r) - 1
                elif(self.direction == DIRECTION_L):
                    print("muerte lado izquierdo")
                    if self.dead_frame < len(self.dead_l) - 1:
                        self.dead_frame += 1
                    else:
                        self.dead_frame = len(self.dead_l) - 1                        
            else:                
                if self.frame < len(self.animation) - 1:
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
            if self.direction == DIRECTION_R:
                self.image = self.dead_r[self.dead_frame]
            else:
                self.image = self.dead_l[self.dead_frame]
        else:
            self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1
        self.music_hurt.play()
        if(self.lives == 0):
            self.is_dead = True
            self.music_dead.play(loops=2)          

    def collision(self, player_rect,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if self.rect.colliderect(player_rect):
                return True                
