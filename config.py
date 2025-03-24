WIDTH, HEIGHT = 1920, 1080

FOV = 60  # Campo de visão
NEAR_PLANE = 0.1
FAR_PLANE = 50.0

PLAYER_START_X = 1.5
PLAYER_START_Y = 1.5
PLAYER_SPEED = 0.025
MOUSE_SENSITIVITY = 0.08

# Labirinto (1 = parede, 0 = caminho)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
