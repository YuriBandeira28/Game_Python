
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import pygame
from pygame.locals import *
import time


class Labirinto():
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


    def gera_labirinto(self):
        # Inicializa o labirinto com paredes
        labirinto = [[1] * self.largura for _ in range(self.altura)]
        # Inicializa a matriz de visitados
        visitados = [[False] * self.largura for _ in range(self.altura)]
        # Escolhe uma célula inicial aleatória com coordenadas ímpares
        x, y = random.randint(0, (self.largura - 3) // 2) * 2 + 1, random.randint(0, (self.altura - 3) // 2) * 2 + 1
        
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
                if 0 < nx < self.largura - 1 and 0 < ny < self.altura - 1 and not visitados[ny][nx]:
                    labirinto[(y + ny) // 2][(x + nx) // 2] = 0
                    dfs(nx, ny)
        dfs(x, y)
        return labirinto
    
    def desenha_labirinto(self, labirinto):
        degrade = 1
        for i in range(len(labirinto)):
            for j in range(len(labirinto[i])):
                if labirinto[i][j] == 1:
                    cor_labirinto = [0.5, 0.5, 0.8]
                    #indice_escolhido = random.randint(0,2)
                    #cor_labirinto[indice_escolhido] = degrade
                    cor_labirinto = tuple(cor_labirinto)
                    glColor3f(cor_labirinto[0], cor_labirinto[1], degrade)
                    glBegin(GL_QUADS)
                    glVertex2f(j, i)
                    glVertex2f(j + 1, i)
                    glVertex2f(j + 1, i + 1)
                    glVertex2f(j, i + 1)
                    glEnd()
                    degrade -= 0.0005
                    
class Player():

    vidas = 3
    dx, dy = 0, 0
    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho

    def desenha_player(self):
        glColor3f(0, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.tamanho, self.y)
        glVertex2f(self.x + self.tamanho, self.y + self.tamanho)
        glVertex2f(self.x, self.y + self.tamanho)
        glEnd()

    def colisao(self, x, y, tamanho,labirinto):     
        for i in range(int(y), int(y + tamanho + 1)):
            for j in range(int(x), int(x + tamanho + 1)):
                if labirinto[i][j] == 1:
                    return True
        return False

    def colide_inimigo(self, x_inimigo, y_inimigo, inimigo_dx, inimigo_dy):
        if self.x + self.dx == x_inimigo + inimigo_dx and self.y + self.dy == y_inimigo + inimigo_dy:
            self.vidas -=1

        if self.vidas == 0:
            time.sleep(2)
            print("FIM DE JOGO")
            exit()

    def move(self , keys, labirinto):
        
        if keys[K_LEFT]:
            self.dx = -0.03

        if keys[K_RIGHT]:
            self.dx = 0.03
            
        if keys[K_UP]:
            self.dy = -0.03
            
        if keys[K_DOWN]:
            self.dy = 0.03

        if not self.colisao(self.x + self.dx, self.y, self.tamanho, labirinto):
            self.x += self.dx
        if not self.colisao(self.x, self.y + self.dy, self.tamanho, labirinto):
            self.y += self.dy
    
class Inimigo():

    dx = 0
    dy = 0

    def __init__(self, x, y, tamanho):
        self.x = x
        self.y = y
        self.tamanho = tamanho

    def desenha_player(self):
        glColor3f(1, 0, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.tamanho, self.y)
        glVertex2f(self.x + self.tamanho, self.y + self.tamanho)
        glVertex2f(self.x, self.y + self.tamanho)
        glEnd()

    def colisao(self, x, y, tamanho,labirinto):     
        for i in range(int(y), int(y + tamanho + 1)):
            for j in range(int(x), int(x + tamanho + 1)):
                if labirinto[i][j] == 1:
                    return True
        return False


    def move(self , labirinto):

        #pesquisar sistema de movimentação automática

        #provisório
        self.dx += random.uniform(-0.01, 0.01)
        self.dy += random.uniform(-0.01, 0.01)
        
        if not self.colisao(self.x + self.dx, self.y, self.tamanho, labirinto):
            self.x += self.dx
        if not self.colisao(self.x, self.y + self.dy, self.tamanho, labirinto):
            self.y += self.dy
    


    

    
