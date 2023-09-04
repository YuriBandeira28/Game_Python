from game import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
import time
import pygame
from pygame.locals import *
import random


tempo_inicial = time.time()


pygame.init()
pygame.mixer.init()

tam_maximo_labirinto = 61

altura_labirinto, largura_labirinto = 11, 11
lab = Labirinto(altura=altura_labirinto,largura=largura_labirinto)
labirinto = lab.gera_labirinto()

vidas_player = 3
x_player, y_player = 1.0, 1.0
tamanho_player = 0.4
player = Player(x_player, y_player, tamanho_player, vidas_player)




inimigos = [Inimigo(len(labirinto) -2, len(labirinto) -2)]

display = (600, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, len(labirinto), len(labirinto), 0)


portal = Portal(labirinto)
def calcula_tempo(temp_ini):
    tempo_atual = time.time() - temp_ini
    minutos = int(tempo_atual // 60)
    segundos = int(tempo_atual % 60)
    tempo_str = f"Tempo: {minutos}m {segundos}s"

    return tempo_str

def desenha_texto(temp_str):
    glColor3f(1, 1, 1)  # Cor do texto
    glRasterPos2f(0.5, 0.5)
    for c in temp_str:
        #glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(c))
        pass
    glPopMatrix()

def troca_fase():
    pygame.quit()

    pygame.init()
    pygame.mixer.init()


    global altura_labirinto
    global largura_labirinto
    global tempo_inicial
    global player
    global lab
    global labirinto
    global inimigos
    global portal
    
    lab = None
    labirinto = None

    player = Player(x_player, y_player, tamanho_player, vidas_player)

    if largura_labirinto >= tam_maximo_labirinto:
        print("tam maximo de labirinto atingido")
        altura_labirinto = tam_maximo_labirinto
        largura_labirinto = tam_maximo_labirinto
    else:
        altura_labirinto += 2
        largura_labirinto += 2
    
    lab = Labirinto(altura=altura_labirinto,largura=largura_labirinto)
    labirinto = lab.gera_labirinto()
    portal = Portal(labirinto)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, len(labirinto), len(labirinto), 0)


    # reseta a posição dos inimigos
    for i in inimigos:
        x_inimigo = random.randint(5, len(labirinto) -1)
        y_inimigo = random.randint(5, len(labirinto) -1)

        if labirinto[x_inimigo][y_inimigo] == 0:
            
            print(f"recolocou um inimigo em X = {x_inimigo} e Y = {y_inimigo}")
            print(f"no labirinto temos essa posição como {labirinto[x_inimigo][y_inimigo]}")
            inimigos[inimigos.index(i)] = Inimigo(x_inimigo, y_inimigo)



    # adiciona um inimigo novo
    while True:
        x_inimigo = random.randint(5, len(labirinto) -1)
        y_inimigo = random.randint(5, len(labirinto) -1)

        if labirinto[x_inimigo][y_inimigo] == 0:
            print(f"colocou um novo inimigo em X = {x_inimigo} e Y = {y_inimigo}")
            print(f"no labirinto temos essa posição como {labirinto[x_inimigo][y_inimigo]}")
            inimigos.append(Inimigo(x_inimigo, y_inimigo))
            break

        else: continue

                    
def reinicia():
    global tempo_inicial
    global player
    global inimigos
    global x_player
    global y_player
    global tamanho_player

    tempo_inicial = time.time()
    x_player, y_player = 1.0, 1.0
    tamanho_player = 0.4
    player = Player(x_player, y_player, tamanho_player, vidas_player)

    tam_inimigos = len(inimigos) + 1
    inimigos = []
    for i in range(tam_inimigos):
        x_inimigo = random.randint(5, len(labirinto) -1)
        y_inimigo = random.randint(5, len(labirinto) -1)

        if labirinto[x_inimigo][y_inimigo] == 0:
            
            print(f"recolocou um inimigo em X = {x_inimigo} e Y = {y_inimigo}")
            print(f"no labirinto temos essa posição como {labirinto[x_inimigo][y_inimigo]}")
            inimigos.append(Inimigo(x_inimigo, y_inimigo))

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    temp_str = calcula_tempo(tempo_inicial)

    keys = pygame.key.get_pressed()
    

    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    lab.desenha_labirinto(labirinto)
    player.desenha_player()
    player.move(keys, labirinto) 
    player.dx, player.dy = 0, 0
    portal.desenha_portal()
    portal.animacao()
    colidiu_portal = portal.colide_player(player.x, player.y)

    if colidiu_portal:
        troca_fase()

    for inimigo in inimigos:
        inimigo.desenha_player()
        #inimigo.move(player.x, player.y, labirinto)

        colidiu = player.colide_inimigo(inimigo.x, inimigo.y) 
        if colidiu:
            # pygame.mixer.music.load("teste.mp3")
            # pygame.mixer.music.play()
            vidas_player -=1
            reinicia()


    
    pygame.display.flip()
    pygame.time.wait(2)