import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import numpy as np

# Inicializa o Pygame
pygame.init()

# Configuração da janela
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

# Configuração da câmera
glMatrixMode(GL_PROJECTION)
gluPerspective(60, (WIDTH / HEIGHT), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Configuração do jogador
player_x, player_y = 1.5, 1.5  # Posição inicial
player_angle = 0  # Ângulo da câmera
speed = 0.025  # Velocidade ajustada
mouse_sensitivity = 0.08  # Sensibilidade do mouse

# Labirinto (1 = parede, 0 = caminho)
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])


# Desenhar um cubo sólido sem linhas visíveis
def draw_cube(x, y):
    size = 1
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)  # Cinza opaco

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


# Desenhar labirinto
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                draw_cube(x, y)


# Captura o mouse no centro da tela
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEMOTION:
            dx, _ = event.rel
            player_angle += dx * mouse_sensitivity

    keys = pygame.key.get_pressed()
    move_x = math.cos(math.radians(player_angle)) * speed
    move_y = math.sin(math.radians(player_angle)) * speed

    if keys[K_w]:
        if maze[int(player_y)][int(player_x + move_x)] == 0:
            player_x += move_x
        if maze[int(player_y + move_y)][int(player_x)] == 0:
            player_y += move_y

    if keys[K_s]:
        if maze[int(player_y)][int(player_x - move_x)] == 0:
            player_x -= move_x
        if maze[int(player_y - move_y)][int(player_x)] == 0:
            player_y -= move_y

    if keys[K_a]:
        if maze[int(player_y)][int(player_x + move_y)] == 0:
            player_x += move_y
        if maze[int(player_y - move_x)][int(player_x)] == 0:
            player_y -= move_x

    if keys[K_d]:
        if maze[int(player_y)][int(player_x - move_y)] == 0:
            player_x -= move_y
        if maze[int(player_y + move_x)][int(player_x)] == 0:
            player_y += move_x

    glLoadIdentity()
    gluLookAt(
        player_x, 0.5, player_y,
        player_x + math.cos(math.radians(player_angle)), 0.5, player_y + math.sin(math.radians(player_angle)),
        0, 1, 0
    )

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_maze()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
