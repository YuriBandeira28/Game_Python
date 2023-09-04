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

altura_labirinto, largura_labirinto = 31, 31
lab = Labirinto(altura=altura_labirinto,largura=largura_labirinto)
labirinto = lab.gera_labirinto()

vidas_player = 3
x_player, y_player = 1.0, 1.0
tamanho_player = 0.4
player = Player(x_player, y_player, tamanho_player, vidas_player)

inimigos = [Inimigo(5, 5), Inimigo(19, 11), Inimigo(11, 5)]


display = (600, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, len(labirinto), len(labirinto), 0)


portal = Portal(5, 5)
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
        #glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24  , ord(c))
        pass
    glPopMatrix()

def troca_fase():
    global altura_labirinto
    global largura_labirinto
    global tempo_inicial
    global player
    global labirinto
    global inimigos
    global portal
    
    altura_labirinto +=2
    largura_labirinto +=2

    x_inimigo = random.randint(6, len(labirinto[0]))
    y_inimigo = random.randint(6, len(labirinto[1]))

    for i in range(labirinto):
        for j in range(labirinto[1]):
            if labirinto[i][j] == 0:
                inimigos.append(Inimigo(x_inimigo, y_inimigo))

    lab = Labirinto(altura=altura_labirinto,largura=largura_labirinto)
    labirinto = lab.gera_labirinto()





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

    inimigos = [Inimigo(5, 5), Inimigo(19, 11), Inimigo(11, 5)]

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
    # portal.desenha_portal()
    # portal.animacao()
    # colidiu_portal = portal.colide_player(player.x, player.y)

    # if colidiu_portal:
    #     troca_fase()

    for inimigo in inimigos:
        inimigo.desenha_player()
        inimigo.move(player.x, player.y, labirinto)

        colidiu = player.colide_inimigo(inimigo.x, inimigo.y) 
        if colidiu:
            pygame.mixer.music.load("teste.mp3")
            pygame.mixer.music.play()
            vidas_player -=1
            reinicia()


    
    pygame.display.flip()
    pygame.time.wait(2)