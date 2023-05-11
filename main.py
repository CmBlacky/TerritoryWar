import pygame

# Dimensions de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Dimensions de la carte
MAP_SIZE = 50
CELL_SIZE = WINDOW_WIDTH // MAP_SIZE

# Couleurs
GRAY = (150, 150, 150)
DARK_GRAY = (130, 130, 130)

class Camp:
    def __init__(self, color, symbol, initial_credits):
        self.color = color
        self.symbol = symbol
        self.credits = initial_credits
        self.territory = set()

def initialize_camps():
    camps = []
    camps.append(Camp("red", "R", 50))
    camps.append(Camp("blue", "B", 50))
    return camps

def draw_map(camps, screen):
    screen.fill(GRAY)  # Remplir l'écran avec la couleur grise

    for x in range(MAP_SIZE):
        for y in range(MAP_SIZE):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, cell_rect)
            pygame.draw.rect(screen, DARK_GRAY, cell_rect, 1)  # Contour plus foncé

    for camp in camps:
        for cell in camp.territory:
            x, y = cell
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, camp.color, cell_rect)

    pygame.display.flip()  # Rafraîchir l'écran

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Simulation de jeu de territoire")

    camps = initialize_camps()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_map(camps, screen)

    pygame.quit()

if __name__ == "__main__":
    main()
