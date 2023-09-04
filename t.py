import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
pygame.init()
display = (800, 400)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


#min x = 0 (ponto central)

# X vai de 0 a 10 pra cada lado

# Y vai de 0 a 5 pra cada lado tambem
def lines():

    glBegin(GL_LINES)
    glColor(0,0,0)
    #X
    # 1
    glVertex3f(-5, -5 , 0)
    glVertex3f(-5, 5, 0)

    # 2
    glVertex3f(0.0, -5, 0)
    glVertex3f(0.0, 5, 0)
    # 3
    glVertex3f(5, -5, 0)
    glVertex3f(5, 5, 0)

    #Y
    glVertex3f(-10, 0, 0)
    glVertex3f(10, 0, 0)

    glEnd()


## dimensões de cada quadrado da tela

# cada quadrado tem 5 unidades no X
# centro de cada quadrado vai ser 5 (posição) / 2 = 2.5


# cada quadrado tem 10 unidades no Y
# centro de cadao quadrado no Y vai ser 10 (posição)/ 2 = 5


def quadrado():
    glBegin(GL_QUADS)
    #glColor3f(1.0, 0.4, 0.0)
    glColor3f(0.7, 0.3, 0.1)

    glVertex3f(-9.5, 0.5, 0) # ponto 1
    glVertex3f(-5.5, 0.5, 0) # ponto 2

    glVertex3f(-5.5, 4.5, 0) # ponto 3
    glVertex3f(-9.5, 4.5, 0) # ponto 4
    glEnd()

def triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1)

    glVertex3f(-4.5, 0.5, 0) # ponto 1
    glVertex3f(-0.5, 0.5, 0) # ponto 2
    glVertex3f(-2.5, 4.5, 0) # ponto 3
    glEnd()

def pentagono():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0)

    glVertex3f(4.5, 0.5, 0) # ponto 1
    glVertex3f(0.5, 0.5, 0) # ponto 2

    glVertex3f(0.5, 3.5, 0) # ponto 3
    glVertex3f(2.5, 4.5, 0) # ponto 4

    glVertex3f(4.5, 3.5, 0) # ponto 5
    glEnd()

def trapezio_n_preenchido():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 0.0, 0)

    # 1
    glVertex3f(9.5, 0.5, 0)
    glVertex3f(8.5, 3.5, 0)
    glVertex3f(7.5, 0.5, 0)

    glVertex3f(8.5, 3.5, 0)

    # 2
    glVertex3f(7.5, 0.5, 0)
    glVertex3f(6.5, 3.5, 0)
    glVertex3f(5.5, 0.5, 0)

    glEnd()

def bandeirinha_sao_joao():
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)

    glVertex3f(-9.5, -0.5, 0) # ponto 1
    glVertex3f(-5.5, -0.5, 0) # ponto 2

    glVertex3f(-5.5, -4.5, 0) # ponto 3
    glVertex3f(-7.5, -2.5, 0) # ponto 4
    glVertex3f(-9.5, -4.5, 0) # ponto 4

    glEnd()


def linhas_x():

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 1.0)

    glVertex3f(-5, -5, 0)
    glVertex3f(0, 0,0)

    glVertex3f(-5, -0, 0)
    glVertex3f(0, -5,0)

    glEnd()

def grade():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 1.0)

    for i in range(1, 5):
        #x
        glVertex3f(0+i, 0, 0)
        glVertex3f(0+i, -5, 0)

        #y
        glVertex3f(0, 0-i, 0)
        glVertex3f(5, 0-i, 0)
    glEnd()


def circulo():
    points = 100
    PI = 3.1415926535
    glBegin(GL_LINE_LOOP)
    glColor3f(1.0, 1.0, 0.0)

    for i in range(points):
        angulo = 2 * PI * i/ points
        # print("angulo - ", angulo)
        # print(math.cos(angulo),math.sin(angulo))
        glVertex3f(7.5 + math.cos(angulo),-2.5 - math.sin(angulo), 0)
    glEnd()

def preenche_cirulo():
    glColor3f(0.2, 0.2,0.2)

    glBegin(GL_QUADS)
    glVertex3f(5, 0, 0)
    glVertex3f(5, -5, 0)

    #y
    glVertex3f(10, -5, 0)
    glVertex3f(10, 0, 0)
    glEnd()



def main():
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslate(0.0, 0.0, -12)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClearColor(1.0, 1.0, 1.0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glPointSize(3.0)
        # glBegin(GL_POINTS)
        # glColor(0, 0, 0)

        # glVertex2f(0, 4)
        # glEnd()

        lines()
        quadrado()
        triangulo()
        pentagono()
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        trapezio_n_preenchido()
        glLineWidth(3.0)
        bandeirinha_sao_joao()
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glLineWidth(5.0)
        linhas_x()
        grade()
        glLineWidth(1.0)
        preenche_cirulo()
        glLineWidth(3.0)
        circulo()
        glLineWidth(1.0)


        pygame.display.flip()
        pygame.time.wait(20)


main()