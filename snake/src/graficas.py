import pygame
from pygame.locals import*
import random
pygame.init()

VerdeFondo=(100,140,100)
Verde=(30,40,30)
verdec=(50,60,50)


#secciones=[(80,80),(80,100),(80,120),(80,140)]


ventana = pygame.display.set_mode((800,600))
Fuente_Titulo=pygame.font.Font("Font/PressStart2P.ttf",50)
Fuente_Menu=pygame.font.Font("Font/PressStart2P.ttf",25)
Fuente_Instr=pygame.font.Font("Font/PressStart2P.ttf",15)

Titulo = Fuente_Titulo.render("Snake", True, Verde)
UnJugador = Fuente_Menu.render("Un Jugador", True, Verde)
Creditos = Fuente_Menu.render("Creditos", True, Verde)
Instr = Fuente_Instr.render("Presione x para entrar en la opcion", True, Verde)
Credito = Fuente_Menu.render("Juego de snake", True, Verde)
Credito1 = Fuente_Instr.render("Realizado por blackhat", True, Verde)
Credito2 = Fuente_Instr.render("Derechos reservados", True, Verde)
Credito3 = Fuente_Instr.render("Abril 2017", True, Verde)
Ins = Fuente_Instr.render("Presione z para volver", True, Verde)
Score=Fuente_Instr.render("Score: ", True,Verde)
Final= Fuente_Titulo.render("Game Over", True, Verde)
Return= Fuente_Instr.render("Presiona z para volver al menu y T para salir", True, Verde)


class grafica(object):
    def __init__(self):
        pass
    def Fondo(self):
        ventana.fill(VerdeFondo)

    def reinicio(self):
        self.secciones=[(80,80),(80,100),(80,120),(80,140)]
        
    def Titulo(self, seleccion):
        
        if seleccion==0:
            pygame.draw.rect(ventana, verdec,(110,135,300,50))
        elif seleccion ==1:
            pygame.draw.rect(ventana, verdec,(110,185,300,50))
        ventana.blit(Titulo,(100,50))
        ventana.blit(UnJugador,(120,150))
        ventana.blit(Creditos,(120,200))
        ventana.blit(Instr,(120,500))
        pass
    
    def Creditos(self):
        ventana.blit(Credito,(120,50))
        ventana.blit(Credito1,(120,150))
        ventana.blit(Credito2,(120,200))
        ventana.blit(Credito3,(120,250))
        ventana.blit(Ins,(120,400))
        pass
    
    def DibujarSnake(self, orientacion,Pcomida,puntuacion):
        try:
            contador=0
            for i in self.secciones:
                contador+=1
                if i[0] >= 800 or i[0] <= 0:
                    i[0]=3
                elif i[1]>=600 or i[1]<=0 :
                    i[1]=3
                pygame.draw.rect(ventana, Verde,((i[0]+1),(i[1]+1),18,18))
                if self.secciones.index(i)==len(self.secciones)-1:
                    if orientacion==0:
                        self.secciones.append((i[0]+20,i[1]))
                    elif orientacion==90:
                        self.secciones.append((i[0],i[1]-20))
                    elif orientacion==180:
                        self.secciones.append((i[0]-20,i[1]))
                    elif orientacion==270:
                        self.secciones.append((i[0],i[1]+20))
                    if i!=Pcomida:
                        del self.secciones[0]
                        return (Pcomida,puntuacion)
                    else:
                        puntuacion+=10
                        return ((random.randint(5,35)*20,random.randint(5,25)*20),puntuacion)
                #break
        except Error:
            print "fin"
        
    def comida(self,Pcomida):  
        pygame.draw.rect(ventana, Verde, (Pcomida[0],Pcomida[1],18,18))
        
    def Score(self,puntuacion):
        ventana.blit(Score,(10,10))
        Puntos=Fuente_Instr.render(str(puntuacion), True,Verde)
        ventana.blit(Puntos,(100,10))
        return puntuacion

    def final(self):
        ventana.blit(Final,(50,50))
        ventana.blit(Return,(50,550))


        


