import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        ######CREACION DE BOTONES#####MASTER SUPERF,POS X,Y/ANCHO W ALTO H/BACKGR,COLOR FONDO/COLOR BORDE/IMAGEN FONDO/                                               ON_CLICK LLAMA A LA FUNC. APRETO O NO EL BOT/PARAM DEL BOTON/              TEXTO, FUENTE, TAMAÑO Y COLOR 
        self.boton1 = Button(master=self,x=20,y=20,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_L_07.png",on_click=self.on_click_boton3,on_click_param="form_game_L3",text="nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=20,y=80,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_L_07.png",on_click=self.on_click_boton3,on_click_param="form_game_L2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=20,y=140,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_L_07.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_L_07.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="SQL",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton5 = Button(master=self,x=20,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_L_07.png",on_click=self.on_click_boton3,on_click_param="form_menu_C",text="Vector",font="Verdana",font_size=30,font_color=C_WHITE)
                                
        self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_XL_07.png",text="Text",font="Verdana",font_size=30,font_color=C_BLACK)
        self.pb1 = ProgressBar(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Glitch_Border/Bars/Bar_Background02.png",image_progress="images/gui/set_gui_01/Data_Border/Bars/Bar_Segment06.png",value = 3, value_max=8) #INSTANCIA ALGO DE LA CLASE PROGRES BAR. SE MUESTRA EN EL MENU UNA BARRITA,DONDE SUMAS O RESTAS ALGO
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.txt1,self.pb1]

    def on_click_boton1(self, parametro): 
        self.pb1.value += 1 #AUMENTA LA BARRITA EN EL MENU A
 
    def on_click_boton2(self, parametro):
        self.pb1.value -= 1 #DISMINUYE LA BARRITA EN EL MENU A
    
    def on_click_boton3(self, parametro): 
        self.set_active(parametro)  #llama al metodo de la clase Form, le envía "form_game_L1" y activa este level
                       
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()