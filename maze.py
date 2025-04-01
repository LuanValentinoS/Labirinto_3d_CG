from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame import image

from config import CHEESE_POSITIONS

# IDs das texturas globais
wall_texture = None
floor_texture = None

def load_textures():
    global wall_texture, floor_texture

    # parede
    wall_surface = image.load("./assets/wall/Bricks077_1K-JPG_Color.jpg")
    wall_data = pygame.image.tostring(wall_surface, "RGB", True)
    w_width, w_height = wall_surface.get_size()

    wall_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) 
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w_width, w_height, 0, GL_RGB, GL_UNSIGNED_BYTE, wall_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # chao
    floor_surface = image.load("./assets/floor/PavingStones134_1K-JPG_Color.jpg")
    floor_data = pygame.image.tostring(floor_surface, "RGB", True)
    f_width, f_height = floor_surface.get_size()

    floor_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, floor_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE) 
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, f_width, f_height, 0, GL_RGB, GL_UNSIGNED_BYTE, floor_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

def draw_cube(x, y):
    size = 1
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glBegin(GL_QUADS)

    # Frente
    glNormal3f(0, 0, -1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    # Trás
    glNormal3f(0, 0, 1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)

    # Esquerda
    glNormal3f(-1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    # Direita
    glNormal3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x + size, size, y)

    # Topo
    glNormal3f(0, 1, 0)
    glTexCoord2f(0, 0); glVertex3f(x, size, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, size, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)
    glEnd()

    # Base - tratada em draw_floor_tile()

# desenha o chao com a textura
def draw_floor_tile(x, y):
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, floor_texture)
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + 1, 0, y)
    glTexCoord2f(1, 1); glVertex3f(x + 1, 0, y + 1)
    glTexCoord2f(0, 1); glVertex3f(x, 0, y + 1)
    glEnd()

# desenha o queijo
def draw_cheese(x, y):
    glPushMatrix()
    glTranslatef(x + 0.5, 0.1, y + 0.5)
    glColor3f(1.0, 0.9, 0.3)
    quad = gluNewQuadric()
    gluSphere(quad, 0.075, 10, 10)
    glPopMatrix()

# desenha o labirinto com os queijos
def draw_maze_with_cheese(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            draw_floor_tile(x, y)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_cube(x, y)

    for cx, cy in CHEESE_POSITIONS:
        draw_cheese(cx - 0.5, cy - 0.5)
