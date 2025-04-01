import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *

class Cat:
    def __init__(self, pos1, pos2, speed=0.005):
        self.pos1 = pos1
        self.pos2 = pos2
        self.speed = speed
        self.current = list(pos1)
        self.forward = True

    def update(self):
        # move entre pos1 <-> pos2
        target = self.pos2 if self.forward else self.pos1
        dx = target[0] - self.current[0]
        dy = target[1] - self.current[1]
        dist = math.hypot(dx, dy)

        if dist < 0.01:
            self.forward = not self.forward
            return

        step_x = self.speed * dx / dist
        step_y = self.speed * dy / dist
        self.current[0] += step_x
        self.current[1] += step_y

    def draw(self):
        glPushMatrix()
        glTranslatef(self.current[0] + 0.5, 0.1, self.current[1] + 0.5)
        glColor3f(0.8, 0.2, 0.2)
        quad = gluNewQuadric()
        gluSphere(quad, 0.15, 16, 16)
        glPopMatrix()

    def check_collision(self, player_x, player_y):
        dist = math.hypot(player_x - (self.current[0] + 0.5), player_y - (self.current[1] + 0.5))
        return dist < 0.4
