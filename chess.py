import pygame

# Initialize pygame
pygame.init()

# Set the width and height of the screen
width = 850
height = 850  

# Create the screen
screen = pygame.display.set_mode((width, height))

board = """rnbqkbnr
pppppppp
........
........
........
........
PPPPPPPP
RNBQKBNR
"""
pieces_folder = "./pieces/"

piece_images = {}

types = ["pawn", "rook", "knight", "bishop", "queen", "king"]

for color in ["white", "black"]:
    for type in types:
        image_path = f"{pieces_folder}{color}-{type}.png"
        newType = type[0].upper() if color == "black" else type[0]
        if type == "knight":
            newType = "N" if color == "black" else "n"
        piece_images[newType] = pygame.image.load(image_path)

# Set square size
square_size = height // 8

# Draw the chessboard squares
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = (255, 206, 158)  # Light square color
        else:
            color = (209, 139, 71)  # Dark square color
        pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

# Draw the chess pieces
for row, line in enumerate(board.split("\n")):
    for col, char in enumerate(line):
        if char != ".":
            piece_image = piece_images.get(char)
            if piece_image:
                # Center the piece on the square
                x_pos = col * square_size + (square_size - piece_image.get_width()) // 2
                y_pos = row * square_size + (square_size - piece_image.get_height()) // 2
                screen.blit(piece_image, (x_pos, y_pos))

# Update the screen
pygame.display.flip()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
