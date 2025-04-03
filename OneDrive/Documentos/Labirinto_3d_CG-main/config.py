WIDTH, HEIGHT = 1920, 1080

FOV = 60  # Campo de visão
NEAR_PLANE = 0.1 
FAR_PLANE = 50.0
COLLISION_MARGIN = 0.1

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
            
# Atualiza o queijo coletado
def update_cheese_positions_and_map(cheese_pos):
    x, y = cheese_pos
    mx, my = int(x), int(y)
    # Remove o queijo da lista de posições
    if (x, y) in CHEESE_POSITIONS:
        CHEESE_POSITIONS.remove((x, y))
    
    # Atualiza o mapa para remover o queijo
    if MAZE[my][mx] == 2:
        MAZE[my][mx] = 0  # Marca o queijo como removido (caminho livre)

