from game import *
import pygame
import time
import pygame
from pygame.locals import *

tempo_inicial = time.time()


pygame.init()

lab = Labirinto(altura=31,largura=31)
x, y = 1.0, 1.0
tamanho = 0.4

player = Player(x, y , tamanho)
inimigos = [Inimigo(5, 5, 0.4), Inimigo(5, 5, 0.4), Inimigo(5, 5, 0.4)]

labirinto = lab.gera_labirinto()

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
    
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    lab.desenha_labirinto(labirinto)
    player.desenha_player()
    player.move(keys, labirinto) 
    player.dx, player.dy = 0, 0

    for inimigo in inimigos:
        inimigo.desenha_player()
        inimigo.move(labirinto)  
        player.colide_inimigo(inimigo.x, inimigo.y, inimigo.dx, inimigo.dy) 
    # Desenhe o tempo usando OpenGL
    #desenha_texto(0.5, 0.5, tempo_str)
    
    pygame.display.flip()
    pygame.time.wait(2)