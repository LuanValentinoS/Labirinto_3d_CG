import math
from OpenGL.GL import *
from OpenGL.GLU import *
from config import WIDTH, HEIGHT, FOV, NEAR_PLANE, FAR_PLANE
from maze import draw_maze

def setup_opengl():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(FOV, WIDTH / HEIGHT, NEAR_PLANE, FAR_PLANE)
    glMatrixMode(GL_MODELVIEW)

def render_scene(player, maze):
    glLoadIdentity()
    gluLookAt(
        player.x, 0.5, player.y,
        player.x + math.cos(math.radians(player.angle)), 0.5, player.y + math.sin(math.radians(player.angle)),
        0, 1, 0
    )

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_maze(maze)
