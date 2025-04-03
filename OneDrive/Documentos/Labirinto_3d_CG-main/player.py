import pygame
import math
from config import PLAYER_START_X, PLAYER_START_Y, PLAYER_SPEED, MOUSE_SENSITIVITY, MAZE, COLLISION_MARGIN

class Player:
    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.angle = 0
        self.pitch = 0

    def update_angle(self, dx, dy):
        self.angle += dx * MOUSE_SENSITIVITY
        self.pitch -= dy * MOUSE_SENSITIVITY
        #self.pitch = max(-89, min(89, self.pitch)) - deixei o pitch sendo tratado no main.

    def handle_input(self):
        keys = pygame.key.get_pressed()

        move_x = math.cos(math.radians(self.angle)) * PLAYER_SPEED
        move_y = math.sin(math.radians(self.angle)) * PLAYER_SPEED

        dx = 0
        dy = 0

        if keys[pygame.K_w]:
            dx += move_x
            dy += move_y
        if keys[pygame.K_s]:
            dx -= move_x
            dy -= move_y
        if keys[pygame.K_a]:
            dx += move_y
            dy -= move_x
        if keys[pygame.K_d]:
            dx -= move_y
            dy += move_x

        # contornando o bug de ver dentro dos blocos
        if not self._is_near_wall(self.x + dx, self.y):
            self.x += dx
        if not self._is_near_wall(self.x, self.y + dy):
            self.y += dy

    def _is_near_wall(self, x, y):
        for dx in [-COLLISION_MARGIN, COLLISION_MARGIN]:
            for dy in [-COLLISION_MARGIN, COLLISION_MARGIN]:
                grid_x = int(x + dx)
                grid_y = int(y + dy)
                if 0 <= grid_y < len(MAZE) and 0 <= grid_x < len(MAZE[0]):
                    if MAZE[grid_y][grid_x] == 1:
                        return True
        return False
