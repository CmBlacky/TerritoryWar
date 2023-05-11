import pygame
import random

# Dimensions de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Dimensions de la carte
MAP_SIZE = 50
CELL_SIZE = WINDOW_WIDTH // MAP_SIZE

# Couleurs
GRAY = (150, 150, 150)


def draw_map(camps, screen):
    screen.fill(GRAY)  # Remplir l'écran avec la couleur grise

    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, cell_rect)
            pygame.draw.rect(screen, (100, 100, 100), cell_rect, 1)  # Contour plus foncé

    for camp in camps:
        for cell in camp.get_territory():
            x, y = cell
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, camp.color, cell_rect)

    pygame.display.flip()  # Rafraîchir l'écran