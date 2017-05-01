import pygame
from pygame.locals import*
import sys 
import graficas
import time
import socket


pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption ("Snake")
g=graficas.grafica()

fase=0
seleccionmenu=0
orientacion=0
Pcomida=(200,200)
puntuacion=0

while True:
    if fase==-1:
        g.Fondo()
        g.final()
    if fase==0:
        g.Fondo()
        g.Titulo(seleccionmenu)
        g.reinicio()
        puntuacion=0
        orientacion=0
    elif fase==1:
        g.Fondo()
        try:
            Pcomida,puntuacion=g.DibujarSnake(orientacion,Pcomida,puntuacion)
        except:
            fase = -1
        g.comida(Pcomida)
        g.Score(puntuacion)
    elif fase==2:
        g.Fondo()
        g.Creditos()
        
    for evento in pygame.event.get():
        if (evento.type== QUIT):
            pygame.quit()
            print 'ser'
            sys.exit()
            pass
        elif evento.type==KEYDOWN:
            if (pygame.key.name(evento.key)=='t'):
                pygame.quit()
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server_address = ('localhost', 8887)
                    s.connect(server_address)
                finally:
                    print 'conexion exitosa'
                try:
                    mensaje=str(puntuacion)
                    s.send(mensaje)
                    s.close()
                finally:
                    print puntuacion
                    print 'mensaje enviado'
                print 'ser'
                sys.exit()
            if (evento.key==pygame.K_DOWN)or(pygame.key.name(evento.key)=='s'):
                if seleccionmenu<1:
                    seleccionmenu+=1
                else:
                    seleccionmenu=0
        elif evento.type==KEYUP:
            if (evento.key==pygame.K_UP)or(pygame.key.name(evento.key)=='w'):
                if seleccionmenu>0:
                    seleccionmenu-=1
                else:
                    seleccionmenu=1
            if (pygame.key.name(evento.key)=='x') and seleccionmenu==1:
                fase=2
            elif (pygame.key.name(evento.key)=='x') and seleccionmenu==0:
                fase=1
            if (pygame.key.name(evento.key)=='z'):
                fase=0
            if fase==1 :
                if ((evento.key==pygame.K_DOWN)or(pygame.key.name(evento.key)=='s'))and orientacion !=90:
                    orientacion=270
                if ((evento.key==pygame.K_UP)or(pygame.key.name(evento.key)=='w'))and orientacion !=270:
                    orientacion=90
                if ((evento.key==pygame.K_LEFT)or(pygame.key.name(evento.key)=='a'))and orientacion !=0:
                    orientacion=180
                if ((evento.key==pygame.K_RIGHT)or(pygame.key.name(evento.key)=='d'))and orientacion !=180:
                    orientacion=0
        pass
        
            
        
    pygame.display.update()
    time.sleep(0.08)
    pass




print "xxx"
