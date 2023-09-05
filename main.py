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
chave = Chave(labirinto)
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


def posicao_valida(x, y, labirinto):
    # Verifique se as coordenadas (x, y) estão dentro dos limites do labirinto
    if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]):
        # Verifique se a célula do labirinto na posição (x, y) não é uma parede (valor 0)
        if labirinto[int(x)][int(y)] == 0:
            return True  # A posição é válida (não é uma parede)
    return False 



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
    global chave

    

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
    chave = Chave(labirinto)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, len(labirinto), len(labirinto), 0)

    tam_inimigos = len(inimigos) + 1
    inimigos = []

    while len(inimigos) <= tam_inimigos -1:

        # reseta a posição dos inimigos
        for i in inimigos:
            x_inimigo = random.randint(5, len(labirinto) -1)
            y_inimigo = random.randint(5, len(labirinto) -1)

            if posicao_valida(x_inimigo, y_inimigo, labirinto):
                inimigos.append(Inimigo(x_inimigo, y_inimigo))



    # adiciona um inimigo novo
    while True:
        x_inimigo = random.randint(5, len(labirinto) -1)
        y_inimigo = random.randint(5, len(labirinto) -1)

        if posicao_valida(x_inimigo, y_inimigo, labirinto):
            # print(f"colocou um novo inimigo em X = {x_inimigo} e Y = {y_inimigo}")
            # print(f"no labirinto temos essa posição como {labirinto[x_inimigo][y_inimigo]}")
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
    global chave
    global portal

    tempo_inicial = time.time()
    x_player, y_player = 1.0, 1.0
    tamanho_player = 0.4
    player = Player(x_player, y_player, tamanho_player, vidas_player)
    chave = Chave(labirinto)
    portal = Portal(labirinto)
    tam_inimigos = len(inimigos) + 1
    inimigos = []

    while len(inimigos) <= tam_inimigos -1:
        for i in range(tam_inimigos):
            x_inimigo = random.randint(5, len(labirinto) -1)
            y_inimigo = random.randint(5, len(labirinto) -1)

            if posicao_valida(x_inimigo, y_inimigo, labirinto):

                # print(f"recolocou um inimigo em X = {x_inimigo} e Y = {y_inimigo}")
                # print(f"no labirinto temos essa posição como {labirinto[x_inimigo][y_inimigo]}")
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
    player.desenha_vidas()
    player.move(keys, labirinto) 
    player.dx, player.dy = 0, 0
    portal.desenha_portal()
    portal.animacao()
    chave.desenha_chave()

    colidiu_chave  = chave.colide_player(player.x, player.y)
    if colidiu_chave:
        portal.liberado = True
        chave.x = -1
        chave.y = -1

    colidiu_portal = portal.colide_player(player.x, player.y)
    if colidiu_portal:
        troca_fase()


    for inimigo in inimigos:
        inimigo.desenha_player()
        inimigo.move(player.x, player.y, labirinto)

        colidiu_inimigo = player.colide_inimigo(inimigo.x, inimigo.y) 
        if colidiu_inimigo:
            # pygame.mixer.music.load("teste.mp3")
            # pygame.mixer.music.play()
            vidas_player -=1
            reinicia()


    
    pygame.display.flip()
    pygame.time.wait(2)