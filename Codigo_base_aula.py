import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time  # Importe a biblioteca de tempo
import random

# Inicialize o tempo
tempo_inicial = time.time()

# Matriz 11x11 representando o labirinto
def gerar_labirinto(largura, altura):
    # Inicializa o labirinto com paredes
    labirinto = [[1] * largura for _ in range(altura)]
    # Inicializa a matriz de visitados
    visitados = [[False] * largura for _ in range(altura)]
    # Escolhe uma célula inicial aleatória com coordenadas ímpares
    x, y = random.randint(0, (largura - 3) // 2) * 2 + 1, random.randint(0, (altura - 3) // 2) * 2 + 1
    
    # Função recursiva para realizar a busca em profundidade
    def dfs(x, y):
        # Marca a célula atual como visitada
        visitados[y][x] = True
        labirinto[y][x] = 0
        # Embaralha as direções para tornar o labirinto mais aleatório
        direcoes = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(direcoes)
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 < nx < largura - 1 and 0 < ny < altura - 1 and not visitados[ny][nx]:
                labirinto[(y + ny) // 2][(x + nx) // 2] = 0
                dfs(nx, ny)
    dfs(x, y)
    return labirinto


labirinto = gerar_labirinto(21,21)

# Posição inicial e tamanho do quadrado
x, y = 1.0, 1.0
tamanho = 0.4

def desenha_labirinto():
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 1:
                glColor3f(0.7, 0.3, 0.1)
                glBegin(GL_QUADS)
                glVertex2f(j, i)
                glVertex2f(j + 1, i)
                glVertex2f(j + 1, i + 1)
                glVertex2f(j, i + 1)
                glEnd()
                
#player
def desenha_quadrado(x, y, tamanho):
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + tamanho, y)
    glVertex2f(x + tamanho, y + tamanho)
    glVertex2f(x, y + tamanho)
    glEnd()

def colisao(x, y, tamanho):
    for i in range(int(y), int(y + tamanho + 1)):
        for j in range(int(x), int(x + tamanho + 1)):
            if labirinto[i][j] == 1:
                return True
    return False

def desenha_texto(x, y, texto):
    glColor3f(1, 1, 1)  # Cor do texto
    glRasterPos2f(x, y)
    for char in texto:
        #glutBitmapCharacter("Arial", ord(char))
        pass
        

pygame.init()

display = (600, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluOrtho2D(0, len(labirinto), len(labirinto), 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Atualize o tempo
    tempo_atual = time.time() - tempo_inicial
    minutos = int(tempo_atual // 60)
    segundos = int(tempo_atual % 60)
    tempo_str = f"Tempo: {minutos}m {segundos}s"

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[K_LEFT]:
        dx = -0.01
    if keys[K_RIGHT]:
        dx = 0.01
    if keys[K_UP]:
        dy = -0.01
    if keys[K_DOWN]:
        dy = 0.01

    if not colisao(x + dx, y, tamanho):
        x += dx
    if not colisao(x, y + dy, tamanho):
        y += dy
    
    glClearColor(1, 0.7, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    desenha_labirinto()
    desenha_quadrado(x, y, tamanho)
    
    # Desenhe o tempo usando OpenGL
    desenha_texto(0.5, 0.5, tempo_str)
    
    pygame.display.flip()
    pygame.time.wait(2)