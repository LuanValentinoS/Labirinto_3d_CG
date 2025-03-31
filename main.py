import pygame
import datetime
from pygame.locals import *
from player import Player
from OpenGL.GL import *
import pygame.freetype
from maze import load_textures
from renderer import setup_opengl, render_scene
from config import WIDTH, HEIGHT, MAZE, CHEESE_POSITIONS

def main():
    pygame.init()
    pygame.freetype.init()
    font = pygame.freetype.SysFont(None, 32)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

    setup_opengl()
    load_textures()
    player = Player()
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    collected = 0
    running = True
    start_ticks = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEMOTION:
                dx, dy = event.rel
                player.update_angle(dx, dy)
        player.handle_input()

        # Detectar coleta de queijo
        player_pos = (player.x, player.y)
        for cheese in CHEESE_POSITIONS[:]:  # cópia da lista
            dist = ((player_pos[0] - cheese[0])**2 + (player_pos[1] - cheese[1])**2) ** 0.5
            if dist < .6:
                CHEESE_POSITIONS.remove(cheese)
                collected += 1
                mx, my = int(cheese[0]), int(cheese[1])
                MAZE[my][mx] = 0  # libera o caminho

        if not CHEESE_POSITIONS:
            end_ticks = pygame.time.get_ticks()
            total_time = (end_ticks - start_ticks) / 1000  # segundos
            show_ranking(total_time)
            running = False

        render_scene(player, MAZE)

        # Desenha o contador por cima da cena
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        draw_text(font, f"Queijos coletados: {collected}", 10, 30)
        glEnable(GL_LIGHTING)
        glEnable(GL_DEPTH_TEST)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

def draw_text(font, text, x, y):
    surf, _ = font.render(text, (255, 255, 255))
    data = pygame.image.tostring(surf, "RGBA", True)
    glWindowPos2d(x, HEIGHT - y)  # y invertido
    glDrawPixels(surf.get_width(), surf.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

def show_ranking(player_time):
    filename = "ranking.txt"

    # Salvar nova entrada
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"{now} - {player_time:.2f} segundos\n")

    # Ler ranking
    with open(filename, "r") as f:
        entries = f.readlines()

    # Ordenar por tempo
    parsed = []
    for line in entries:
        try:
            date_str, time_str = line.strip().split(" - ")
            time_val = float(time_str.replace(" segundos", ""))
            parsed.append((date_str, time_val))
        except:
            continue

    parsed.sort(key=lambda x: x[1])

    # Mostrar ranking final
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    font = pygame.freetype.SysFont(None, 36)

    font.render_to(screen, (50, 40), "Ranking", (255, 255, 0))

    for i, (date, tempo) in enumerate(parsed[:5]):  # Top 5
        font.render_to(screen, (50, 100 + i * 40), f"{i+1}. {date} - {tempo:.2f} s", (255, 255, 255))

    font.render_to(screen, (50, 350), f"Seu tempo: {player_time:.2f} segundos", (0, 255, 0))
    font.render_to(screen, (50, 400), "Pressione ESC para sair", (200, 200, 200))
    pygame.display.flip()

    # Espera até o jogador apertar ESC
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False

if __name__ == "__main__":
    main()
