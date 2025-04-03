import pygame
from pygame.locals import *
from player import Player
# from maze import draw_maze
from renderer import setup_opengl, render_scene
from config import WIDTH, HEIGHT, MAZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)

    setup_opengl()

    player = Player()
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEMOTION:
                dx, _ = event.rel
                player.update_angle(dx)

        player.handle_input()
        render_scene(player, MAZE)
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
