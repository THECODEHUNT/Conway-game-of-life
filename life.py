import argparse
import pygame
import time
import random
from utils import next_gen, random_fill, save_pattern, load_pattern

CELL_SIZE = 20
MARGIN = 1
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (220, 220, 220)

def draw_grid(screen, live_cells, width, height, font, generation):
    screen.fill(WHITE)
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - MARGIN, CELL_SIZE - MARGIN)
            if (x, y) in live_cells:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, GREY, rect, 1)
    text = font.render(f"Gen: {generation} | Live: {len(live_cells)}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

def main():
    print("$ python life.py --width 40 --height 20 --fps 6")
    print("┌ Game of Life ──────────────────────────────┐")
    print("│ Space:▶/⏸  N:Step  R:Random  S:Save  L:Load│")
    print("│ Generation 42      Live cells: 117         │")
    print("└─────────────────────────────────────────────┘")

    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int, default=30)
    parser.add_argument('--height', type=int, default=20)
    parser.add_argument('--fps', type=int, default=10)
    args = parser.parse_args()

    width, height, fps = args.width, args.height, args.fps
    pygame.init()
    screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE + 30))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    live_cells = set()
    running = False
    generation = 0

    while True:
        draw_grid(screen, live_cells, width, height, font, generation)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                elif event.key == pygame.K_n:
                    live_cells = next_gen(live_cells)
                    generation += 1
                elif event.key == pygame.K_c:
                    live_cells = set()
                    generation = 0
                elif event.key == pygame.K_r:
                    live_cells = random_fill(width, height)
                    generation = 0
                elif event.key == pygame.K_s:
                    save_pattern(live_cells, "patterns.txt")
                elif event.key == pygame.K_l:
                    live_cells = load_pattern("patterns.txt")
                    generation = 0

        if running:
            live_cells = next_gen(live_cells)
            generation += 1
            time.sleep(1.0 / fps)

        clock.tick(60)

if __name__ == '__main__':
    main()
