import pygame
import sys
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 700
GRID_SIZE = 3
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
font = pygame.font.SysFont('comicsansms', 100)
grid = [['' for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
player = "X"
game_over = False


def draw_grid():
    """Draws the Tic-Tac-Toe grid on the screen."""
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_HEIGHT), 5)
        pygame.draw.line(screen, WHITE, (0, x * CELL_SIZE), (SCREEN_WIDTH, x * CELL_SIZE), 5)


def draw_marks():
    """Draws the X and O marks on the grid."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            mark = grid[row][col]
            if mark:
                color = BLUE if mark == 'X' else RED
                text = font.render(mark, True, color)
                screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 4, row * CELL_SIZE + CELL_SIZE // 8))


def check_winner():
    """Checks if there is a winner in the current grid state."""
    global game_over
    for i in range(GRID_SIZE):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != '':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != '':
            return grid[0][i]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '':
        return grid[0][2]
    if all(grid[row][col] != '' for row in range(GRID_SIZE) for col in range(GRID_SIZE)):
        return "Tie"

    return None


def reset_game():
    """Resets the game to the initial state."""
    global grid, player, game_over
    grid = [['' for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    player = "X"
    game_over = False

while True:
    screen.fill(BLACK)
    draw_grid()
    draw_marks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            if grid[row][col] == '':
                grid[row][col] = player
                winner = check_winner()
                if winner:
                    game_over = True
                    print(f"Winner: {winner}")
                else:
                    # Switch player
                    player = "O" if player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
    winner = check_winner()
    if game_over:
        winner_text = f"{winner} wins!" if winner != "Tie" else "It's a Tie!"
        text_surface = font.render(winner_text, True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 4 - 50, SCREEN_HEIGHT // 2 - 50))

    pygame.display.flip()
