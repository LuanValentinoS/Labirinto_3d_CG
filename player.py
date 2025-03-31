import pygame
import math
from config import PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED, MOUSE_SENSITIVITY, MAZE

class Player:
    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.angle = 0
        self.pitch = 0

    def update_angle(self, dx, dy):
        self.angle += dx * MOUSE_SENSITIVITY
        self.pitch -= dy * MOUSE_SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch)) 

    def handle_input(self):
        keys = pygame.key.get_pressed()
        move_x = math.cos(math.radians(self.angle)) * PLAYER_SPEED
        move_y = math.sin(math.radians(self.angle)) * PLAYER_SPEED

        if keys[pygame.K_w]:
            if MAZE[int(self.y)][int(self.x + move_x)] == 0:
                self.x += move_x
            if MAZE[int(self.y + move_y)][int(self.x)] == 0:
                self.y += move_y

        if keys[pygame.K_s]:
            if MAZE[int(self.y)][int(self.x - move_x)] == 0:
                self.x -= move_x
            if MAZE[int(self.y - move_y)][int(self.x)] == 0:
                self.y -= move_y

        if keys[pygame.K_a]:
            if MAZE[int(self.y)][int(self.x + move_y)] == 0:
                self.x += move_y
            if MAZE[int(self.y - move_x)][int(self.x)] == 0:
                self.y -= move_x

        if keys[pygame.K_d]:
            if MAZE[int(self.y)][int(self.x - move_y)] == 0:
                self.x -= move_y
            if MAZE[int(self.y + move_x)][int(self.x)] == 0:
                self.y += move_x
