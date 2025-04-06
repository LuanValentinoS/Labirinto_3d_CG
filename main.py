from OpenGL.GL import *
import copy
import pygame
import datetime
from pygame.locals import *
import pygame.freetype

from player import Player
from maze import load_textures, cat_model
from cat import Cat
from renderer import setup_opengl, render_scene
from config import WIDTH, HEIGHT, MAZE, CHEESE_POSITIONS, update_cheese_positions_and_map


# Função para desenhar o ícone
def draw_icon(img, x, y):
    data = pygame.image.tostring(img, "RGBA", True)
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_DEPTH_TEST)
    glWindowPos2d(x, HEIGHT - y)
    glDrawPixels(img.get_width(), img.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)
    glPopAttrib()


# Função para desenhar texto na tela
def draw_text(font, text, x, y, color=(255, 255, 255)):
    surf, _ = font.render(text, fgcolor=color, bgcolor=None)
    data = pygame.image.tostring(surf, "RGBA", True)
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)
    glDisable(GL_TEXTURE_2D)
    glDisable(GL_DEPTH_TEST)
    glWindowPos2d(x, HEIGHT - y)
    glDrawPixels(surf.get_width(), surf.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)
    glPopAttrib()


def main():
    maze = copy.deepcopy(MAZE)
    cheese_positions = list(CHEESE_POSITIONS)
    pygame.init()
    pygame.mixer.init()
    pygame.freetype.init()
    font = pygame.freetype.SysFont(None, 32)
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    lives = 3

    # Sons
    sound_step = pygame.mixer.Sound("assets/sounds/step.wav")
    sound_cheese = pygame.mixer.Sound("assets/sounds/cheese.wav")
    sound_meow = pygame.mixer.Sound("assets/sounds/meow.wav")
    sound_gameover = pygame.mixer.Sound("assets/sounds/gameover.wav")

    cheese_icon = pygame.image.load("assets/models/cheese/cheese.png").convert_alpha()
    cheese_icon = pygame.transform.scale(cheese_icon, (64, 64))
    heart_icon = pygame.image.load("assets/models/heart/heart.png").convert_alpha()  # Coração para representar as vidas
    heart_icon = pygame.transform.scale(heart_icon, (64, 64))  # Ajuste o tamanho do coração conforme necessário

    setup_opengl()
    cat_texture = load_textures()
    player = Player()

    cats = [
        Cat((1, 5), (2, 5), cat_model, cat_texture=cat_texture, rotate_angle=0),
        Cat((6, 2), (6, 4), cat_model, cat_texture=cat_texture, rotate_angle=90)
    ]
    """
    # Versão 16x16
    
    cats = [
    Cat((1, 5), (3, 5), cat_model, cat_texture=cat_texture, rotate_angle=0),
    Cat((2, 7), (2, 8), cat_model, cat_texture=cat_texture, rotate_angle=90),
    Cat((5, 5), (5, 7), cat_model, cat_texture=cat_texture, rotate_angle=90),
    Cat((5, 11), (5, 13), cat_model, cat_texture=cat_texture, rotate_angle=90),
    Cat((7, 6), (8, 6), cat_model, cat_texture=cat_texture, rotate_angle=0),
    Cat((9, 1), (9, 2), cat_model, cat_texture=cat_texture, rotate_angle=90),
    Cat((8, 3), (9, 3), cat_model, cat_texture=cat_texture, rotate_angle=0),
    Cat((9, 4), (10, 4), cat_model, cat_texture=cat_texture, rotate_angle=0),
    Cat((9, 10), (11, 10), cat_model, cat_texture=cat_texture, rotate_angle=0),
    Cat((9, 12), (9, 14), cat_model, cat_texture=cat_texture, rotate_angle=90),
    Cat((12, 2), (12, 5), cat_model, cat_texture=cat_texture, rotate_angle=90)
    ]
    """

    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    collected = 0  # contador de queijos
    running = True
    start_ticks = pygame.time.get_ticks()  # marca o tempo para o ranking
    cheese_angle = 0  # angulo inicial do queijo
    warning = 0
    while running:
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cheese_angle = (cheese_angle + 1) % 360
        current_ticks = pygame.time.get_ticks()
        elapsed_time = (current_ticks - start_ticks) / 1000

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.mixer.pause()
                choice = pause_menu(font)
                pygame.mixer.unpause()
                if choice == "exit":
                    running = False
                    break
            elif event.type == MOUSEMOTION:
                dx, dy = event.rel
                player.update_angle(dx, dy)
                player.pitch = max(-45, min(45, player.pitch))

        player.handle_input()

        keys = pygame.key.get_pressed()
        if any([keys[K_w], keys[K_a], keys[K_s], keys[K_d]]):
            if not pygame.mixer.get_busy():
                sound_step.play()

        player_pos = (player.x, player.y)
        # Para cada queijo, verifica se o jogador está perto e coleta o queijo
        for cheese in cheese_positions[:]:
            dist = ((player_pos[0] - cheese[0]) ** 2 + (player_pos[1] - cheese[1]) ** 2) ** 0.5
            if dist < .6:  # Quando o jogador está perto do queijo
                cheese_positions.remove(cheese)  # Remove a posição do queijo
                update_cheese_positions_and_map(cheese)
                sound_cheese.play()
                collected += 1
                mx, my = int(cheese[0]), int(cheese[1])
                MAZE[my][mx] = 0  # Marca o queijo como coletado no mapa

        if not cheese_positions:
            if player.near_end:
                end_ticks = pygame.time.get_ticks()
                total_time = (end_ticks - start_ticks) / 1000
                sound_gameover.play()
                show_ranking(total_time)
                running = False
                

        for cat in cats:
            cat.update()
            if cat.check_collision(player.x, player.y):
                lives -= 1
                sound_meow.play()
                if lives <= 0:
                    sound_gameover.play()
                    show_message("Game Over",48)
                    running = False
                    break
                else:
                    show_message(f"O gato te comeu! Vidas restantes: {lives}", 48)
                    player = Player()

        render_scene(player, maze, cheese_angle)

        for cat in cats:
            cat.draw()

        # Exibe o coração para as vidas em vez do texto de vidas
        for i in range(lives):
            x = 10 + i * 36  # Posição dos corações na tela
            y = HEIGHT - 50
            draw_icon(heart_icon, x, y)

        # Exibe o ícone de queijo
        for i in range(collected):
            x = WIDTH - 74 - i * 68  # Ajuste a posição dos ícones de queijo
            y = 64 + 10
            draw_icon(cheese_icon, x, y)

        draw_text(font, f"Queijos: {collected}/4", WIDTH // 2 - 100, HEIGHT - 60)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


def show_message(text, font_size):
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)

    font = pygame.freetype.SysFont(None, font_size)
    surf, _ = font.render(text, (255, 0, 0))
    data = pygame.image.tostring(surf, "RGBA", True)
    glWindowPos2d(WIDTH // 2 - surf.get_width() // 2, HEIGHT // 2)
    glDrawPixels(surf.get_width(), surf.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, data)

    pygame.display.flip()
    pygame.time.wait(2000)
    glPopAttrib()


def show_ranking(player_time):
    filename = "ranking.txt"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"{now} - {player_time:.2f} segundos\n")

    with open(filename, "r") as f:
        entries = f.readlines()

    parsed = []
    for line in entries:
        try:
            date_str, time_str = line.strip().split(" - ")
            time_val = float(time_str.replace(" segundos", ""))
            parsed.append((date_str, time_val))
        except:
            continue

    parsed.sort(key=lambda x: x[1])

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    font = pygame.freetype.SysFont(None, 36)
    draw_text(font, "Ranking", 50, 40, (255, 255, 0))

    for i, (date, tempo) in enumerate(parsed[:5]):  # Top 5 dos tempos
        draw_text(font, f"{i + 1}. {date} - {tempo:.2f} s", 50, 100 + i * 40, (255, 255, 255))

    draw_text(font, f"Seu tempo: {player_time:.2f} segundos", 50, 350, (0, 255, 0))
    draw_text(font, "Pressione ESC para sair", 50, 400, (200, 200, 200))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False


def pause_menu(font):
    selected = 0
    options = ["Voltar ao jogo", "Sair"]
    waiting = True

    while waiting:
        glClearColor(0.1, 0.1, 0.1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected else (255, 255, 255)
            draw_text(font, option, WIDTH // 2 - 100, HEIGHT // 2 + i * 40, color)

        draw_text(font, "PAUSADO", WIDTH // 2 - 100, HEIGHT // 2 - 100, (200, 200, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return "exit"
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == K_RETURN:
                    if options[selected] == "Voltar ao jogo":
                        return "resume"
                    elif options[selected] == "Sair":
                        return "exit"
        pygame.time.wait(100)



if __name__ == "__main__":
    main()
