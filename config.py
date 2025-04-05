WIDTH, HEIGHT = 1920, 1080

FOV = 60  # Campo de visão
NEAR_PLANE = 0.1 
FAR_PLANE = 50.0
COLLISION_MARGIN = 0.1
CAMERA_HEIGHT = 0.15 #altura da camera


PLAYER_START_X = 1.5
PLAYER_START_Y = 1.5
PLAYER_SPEED = 0.025
MOUSE_SENSITIVITY = 0.08

# Labirinto (1 = parede, 2 = queijo, 0 = caminho)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 1, 0, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 2, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 2, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


CHEESE_POSITIONS = []

for y in range(len(MAZE)):
    for x in range(len(MAZE[y])):
        if MAZE[y][x] == 2:
            CHEESE_POSITIONS.append((x + 0.5, y + 0.5))  # centro do quadrado
