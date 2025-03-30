from OpenGL.GL import *

def draw_cube(x, y):
    size = 1
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)

    # Frente
    glVertex3f(x, 0, y)
    glVertex3f(x + size, 0, y)
    glVertex3f(x + size, size, y)
    glVertex3f(x, size, y)

    # Trás
    glVertex3f(x, 0, y + size)
    glVertex3f(x + size, 0, y + size)
    glVertex3f(x + size, size, y + size)
    glVertex3f(x, size, y + size)

    # Esquerda
    glVertex3f(x, 0, y)
    glVertex3f(x, 0, y + size)
    glVertex3f(x, size, y + size)
    glVertex3f(x, size, y)

    # Direita
    glVertex3f(x + size, 0, y)
    glVertex3f(x + size, 0, y + size)
    glVertex3f(x + size, size, y + size)
    glVertex3f(x + size, size, y)

    # Topo
    glVertex3f(x, size, y)
    glVertex3f(x + size, size, y)
    glVertex3f(x + size, size, y + size)
    glVertex3f(x, size, y + size)

    # Base
    glVertex3f(x, 0, y)
    glVertex3f(x + size, 0, y)
    glVertex3f(x + size, 0, y + size)
    glVertex3f(x, 0, y + size)

    glEnd()
    glEnable(GL_DEPTH_TEST)

def draw_floor(x, y):
    size = 1
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)

    # Piso
    glVertex3f(x, 0, y)
    glVertex3f(x + size, 0, y)
    glVertex3f(x + size, 0, y + size)
    glVertex3f(x, 0, y + size)

    glEnd()
    glEnable(GL_DEPTH_TEST)

def set_lightning(mid):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    # Configuração da luz
    position = [mid, mid, 10.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    diffuse = [0.8, 1.0, 0.8, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse)
    ambient = [0.15, 0.15, 0.15, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient)
    specular = [0.4, 0.4, 0.4, 0.4]
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular)

def draw_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_cube(x, y)
            else:
                draw_floor(x, y)
    set_lightning(len(maze[0])/2)