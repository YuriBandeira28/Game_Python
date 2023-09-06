import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image

# Carrega o GIF
def load_gif(filename):
    im = Image.open(filename)
    frames = []
    try:
        while True:
            frames.append(im.copy())
            im.seek(len(frames))
    except EOFError:
        pass
    return frames

# Inicializa o Pygame e cria a janela OpenGL
def init_display(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    glOrtho(0, width, height, 0, -1, 1)
    glDisable(GL_DEPTH_TEST)

# Exibe o GIF na janela OpenGL
def display_gif(frames, frame_duration):
    frame_index = 0
    last_frame_time = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        current_time = pygame.time.get_ticks()
        if current_time - last_frame_time > frame_duration:
            last_frame_time = current_time
            frame = frames[frame_index]

            # Converta o quadro do GIF para o formato RGBA
            frame_rgba = frame.convert("RGBA")
            texture_data = frame_rgba.tobytes("raw", "RGBA")

            glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
            glTexImage2D(
                GL_TEXTURE_2D, 0, GL_RGBA, frame.width, frame.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data
            )

            glEnable(GL_TEXTURE_2D)
            glBegin(GL_QUADS)
            glTexCoord2f(0, 1)
            glVertex2f(0, 0)
            glTexCoord2f(1, 1)
            glVertex2f(frame.width, 0)
            glTexCoord2f(1, 0)
            glVertex2f(frame.width, frame.height)
            glTexCoord2f(0, 0)
            glVertex2f(0, frame.height)
            glEnd()
            glDisable(GL_TEXTURE_2D)

            pygame.display.flip()

            frame_index = (frame_index + 1) % len(frames)

if __name__ == "__main__":
    gif_filename = "end.gif"  # Substitua pelo caminho do seu arquivo GIF
    gif_frames = load_gif(gif_filename)
    frame_duration = 100  # Duração de cada quadro em milissegundos

    width, height = gif_frames[0].size
    init_display(width, height)
    display_gif(gif_frames, frame_duration)
