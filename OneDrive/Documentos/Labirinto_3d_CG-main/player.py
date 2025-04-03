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

    def handle_input(self):
        keys = pygame.key.get_pressed()

        # Define o multiplicador de corrida: se shift esquerdo estiver pressionado, aumenta a velocidade.
        sprint_multiplier = 2.0 if keys[pygame.K_LSHIFT] else 1.0

        move_x = math.cos(math.radians(self.angle)) * PLAYER_SPEED * sprint_multiplier
        move_y = math.sin(math.radians(self.angle)) * PLAYER_SPEED * sprint_multiplier

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

        # Verifica se o jogador pode se mover na nova posição sem colidir com paredes
        if not self._is_near_wall(self.x + dx, self.y):
            self.x += dx
        if not self._is_near_wall(self.x, self.y + dy):
            self.y += dy

    def _is_near_wall(self, x, y):
        """
        Verifica se há uma parede próxima ao jogador, cercando-o com um raio de pontos de colisão.
        """
        check_offsets = [
            (-COLLISION_MARGIN * 1.5, -COLLISION_MARGIN * 1.5),  # Diagonal superior esquerda
            (COLLISION_MARGIN * 1.5, -COLLISION_MARGIN * 1.5),  # Diagonal superior direita
            (-COLLISION_MARGIN * 1.5, COLLISION_MARGIN * 1.5),  # Diagonal inferior esquerda
            (COLLISION_MARGIN * 1.5, COLLISION_MARGIN * 1.5),  # Diagonal inferior direita
        ]

        for offset_x, offset_y in check_offsets:
            grid_x = int(x + offset_x)
            grid_y = int(y + offset_y)
            if 0 <= grid_y < len(MAZE) and 0 <= grid_x < len(MAZE[0]):
                if MAZE[grid_y][grid_x] == 1:
                    return True  # Há uma parede próxima, impede o movimento

        return False  # Nenhuma parede detectada





