
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
import maze
from config import WIDTH, HEIGHT, FOV, NEAR_PLANE, FAR_PLANE


def setup_opengl():
    glEnable(GL_TEXTURE_2D)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(FOV, WIDTH / HEIGHT, NEAR_PLANE, FAR_PLANE)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    ambient_light = [0.2, 0.2, 0.2, 1.0]
    diffuse_light = [0.8, 0.8, 0.8, 1.0]
    light_position = [2.0, 4.0, 2.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 5.0)
    
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def render_scene(player, maze_data, cheese_angle):
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pitch_rad = math.radians(player.pitch)
    yaw_rad = math.radians(player.angle)

    dir_x = math.cos(pitch_rad) * math.cos(yaw_rad)
    dir_y = math.sin(pitch_rad)
    dir_z = math.cos(pitch_rad) * math.sin(yaw_rad)

    gluLookAt(
        player.x, 0.4, player.y,
        player.x + dir_x, 0.4 + dir_y, player.y + dir_z,
        0, 1, 0
    )

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    maze.draw_maze_with_cheese(maze_data, cheese_angle)