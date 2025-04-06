import os
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame import image

from config import CHEESE_POSITIONS

wall_texture = None
floor_texture = None
cheese_texture = None

# Estrutura simples para armazenar modelo
class OBJModel:
    def __init__(self, filename, target_object):
        self.vertices = []
        self.faces = []
        self.normals = []
        self.texcoords = []
        self.load(filename, target_object)

    def load(self, filename, target_object=None):
        current_object = None
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('o '):  # Novo objeto
                    current_object = line.strip().split(' ')[1]
                elif line.startswith('g '):
                    current_object = line.strip().split(' ')[1]
                elif line.startswith('v '):
                    self.vertices.append(list(map(float, line.strip().split()[1:])))
                elif line.startswith('vn '):
                    self.normals.append(list(map(float, line.strip().split()[1:])))
                elif line.startswith('vt '):
                    self.texcoords.append(list(map(float, line.strip().split()[1:])))
                elif line.startswith('f '):
                    if target_object is None or current_object == target_object:
                        face = []
                        for v in line.strip().split()[1:]:
                            parts = v.split('/')
                            vi = int(parts[0]) - 1
                            ti = int(parts[1]) - 1 if len(parts) > 1 and parts[1] else None
                            ni = int(parts[2]) - 1 if len(parts) > 2 and parts[2] else None
                            face.append((vi, ti, ni))
                        self.faces.append(face)


    def draw(self):
        glBegin(GL_TRIANGLES)
        for face in self.faces:
            for (vi, ti, ni) in face:
                if ni is not None and ni < len(self.normals):
                    glNormal3fv(self.normals[ni])
                if ti is not None and ti < len(self.texcoords):
                    glTexCoord2f(*self.texcoords[ti][:2])  # <-- aqui
                glVertex3fv(self.vertices[vi])
        glEnd()


cheese_model = OBJModel('assets/models/cheese/cheese.obj', target_object='cheese')
cat_model = OBJModel('assets/models/cat/cat_mod2.obj', target_object='kitty_001')

def load_textures():
    global wall_texture, floor_texture, cheese_texture, cat_texture, end_texture

    #textura da parede final
    end_surface = image.load("./assets/end/End-JPG_Color.jpg")
    end_data = pygame.image.tostring(end_surface, "RGB", True)
    e_width, e_height = end_surface.get_size()
    end_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, end_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, e_width, e_height, 0, GL_RGB, GL_UNSIGNED_BYTE, end_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # textura da parede
    wall_surface = image.load("./assets/wall/Bricks077_1K-JPG_Color.jpg")
    wall_data = pygame.image.tostring(wall_surface, "RGB", True)
    w_width, w_height = wall_surface.get_size()
    wall_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w_width, w_height, 0, GL_RGB, GL_UNSIGNED_BYTE, wall_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # textura do piso
    floor_surface = image.load("./assets/floor/PavingStones134_1K-JPG_Color.jpg")
    floor_data = pygame.image.tostring(floor_surface, "RGB", True)
    f_width, f_height = floor_surface.get_size()
    floor_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, floor_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, f_width, f_height, 0, GL_RGB, GL_UNSIGNED_BYTE, floor_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # textura do queijo
    cheese_surface = image.load("./assets/models/cheese/cheese03DiffuseMap.png")
    cheese_data = pygame.image.tostring(cheese_surface, "RGB", True)
    f_width, f_height = cheese_surface.get_size()
    cheese_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, cheese_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, f_width, f_height, 0, GL_RGB, GL_UNSIGNED_BYTE, cheese_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # textura do gato
    cat_surface = image.load("./assets/models/cat/Texture_1.png")
    cat_data = pygame.image.tostring(cat_surface, "RGB", True)
    f_width, f_height = cat_surface.get_size()
    cat_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, cat_texture)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, f_width, f_height, 0, GL_RGB, GL_UNSIGNED_BYTE, cat_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return cat_texture

def draw_cube(x, y):
    size = 1
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, wall_texture)
    glBegin(GL_QUADS)

    glNormal3f(0, 0, -1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    glNormal3f(0, 0, 1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)

    glNormal3f(-1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    glNormal3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x + size, size, y)

    glNormal3f(0, 1, 0)
    glTexCoord2f(0, 0); glVertex3f(x, size, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, size, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)
    glEnd()

def draw_cube_end(x, y):
    size = 1
    glColor3f(1, 1, 1)
    glBindTexture(GL_TEXTURE_2D, end_texture)
    glBegin(GL_QUADS)

    glNormal3f(0, 0, -1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    glNormal3f(0, 0, 1)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)

    glNormal3f(-1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y)

    glNormal3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(x + size, 0, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, 0, y + size)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x + size, size, y)

    glNormal3f(0, 1, 0)
    glTexCoord2f(0, 0); glVertex3f(x, size, y)
    glTexCoord2f(1, 0); glVertex3f(x + size, size, y)
    glTexCoord2f(1, 1); glVertex3f(x + size, size, y + size)
    glTexCoord2f(0, 1); glVertex3f(x, size, y + size)
    glEnd()

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

def draw_cheese(x, y, angle):
    glDisable(GL_CULL_FACE)
    glBindTexture(GL_TEXTURE_2D, cheese_texture)
    glPushMatrix()
    glTranslatef(x + 0.5, 0.05, y + 0.5)
    glScalef(0.02, 0.02, 0.02)
    glRotatef(angle, 0, 1, 0)
    cheese_model.draw()
    glPopMatrix()

def draw_maze_with_cheese(maze, angle):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            draw_floor_tile(x, y)

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_cube(x, y)
            elif maze[y][x] == 3:
                draw_cube_end(x, y)

    for cx, cy in CHEESE_POSITIONS:
        draw_cheese(cx - 0.5, cy - 0.5, angle)
