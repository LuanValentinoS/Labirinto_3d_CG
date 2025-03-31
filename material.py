from OpenGL.GL import *

def set_material_rugosity(shininess):
    """Define brilho especular com base na rugosidade"""
    spec = max(0.05, min(1.0, shininess / 20))  # converte shininess para 0.05–1.0
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [spec] * 3 + [1.0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)
