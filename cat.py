import math
from OpenGL.GL import *
from OpenGL.GLU import *

class Cat:
    def __init__(self, pos1, pos2, cat_model, cat_texture, rotate_angle, speed=0.01):
        self.pos1 = pos1
        self.pos2 = pos2
        self.speed = speed
        self.current = list(pos1)
        self.forward = True
        self.cat_model = cat_model
        self.cat_texture = cat_texture
        self.rotate_angle = rotate_angle  # grau atual de rotação

    def update(self):
        # alvo atual
        target = self.pos2 if self.forward else self.pos1
        dx = target[0] - self.current[0]
        dy = target[1] - self.current[1]
        dist = math.hypot(dx, dy)

        if dist < 0.05:
            self.forward = not self.forward
            return

        # passo em direção ao destino
        step_x = self.speed * dx / dist
        step_y = self.speed * dy / dist
        self.current[0] += step_x
        self.current[1] += step_y

        # calcular o ângulo desejado
        target_angle = math.degrees(math.atan2(dx, dy))  # (atenção à ordem dx/dy!)
        # suavizar a rotação
        diff = (target_angle - self.rotate_angle + 180) % 360 - 180
        self.rotate_angle += diff * (self.speed * 10)  # suavidade

    def draw(self):
        glPushMatrix()
        glTranslatef(self.current[0] + 0.5, 0, self.current[1] + 0.5)
        glRotatef(self.rotate_angle, 0, 1, 0)
        glRotatef(180, 0, 1, 0) 
        glBindTexture(GL_TEXTURE_2D, self.cat_texture)
        self.cat_model.draw()
        glPopMatrix()

    def check_collision(self, player_x, player_y):
        dist = math.hypot(player_x - (self.current[0] + 0.5), player_y - (self.current[1] + 0.5))
        return dist < 0.4
