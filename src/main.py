
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Un livre dont vous êtes le héros')

# Load icon and background
programIcon = pygame.image.load('Icon/dragon_icon.png')
background = pygame.image.load('assets/wp5381270-epic-winter-fantasy-wallpapers.jpg')

# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (120, 160, 180)

# Create a button rect
buttonPlay = pygame.Rect(0, 0, 200, 60)
buttonExit = pygame.Rect(0, 0, 200, 60)

# Center the buttons on the screen
buttonPlay.center = (screen.get_width() // 2, screen.get_height() // 2 - 40)
buttonExit.center = (screen.get_width() // 2, screen.get_height() // 2 + 80)

# Set up font
Buttonfont = pygame.font.Font(None, 30)
Titlefont = pygame.font.Font("Icon/You Are Scared.ttf", 80)

button_text_Play = Buttonfont.render("Play", True, WHITE)
button_text_Exit = Buttonfont.render("Exit", True, WHITE)

# Create text
title_text = Titlefont.render('The Snowy Paths', True, WHITE)
title_rect = title_text.get_rect(center=(screen.get_width() // 2, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if buttonExit.collidepoint(event.pos):
                    running = False

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, BUTTON_COLOR, buttonExit, border_radius = 12)
    pygame.draw.rect(screen, BUTTON_COLOR, buttonPlay, border_radius = 12)

    # Center the text on the buttons
    text_rect = button_text_Exit.get_rect(center=buttonExit.center)
    screen.blit(button_text_Exit, text_rect)

    text_rect = button_text_Play.get_rect(center=buttonPlay.center)
    screen.blit(button_text_Play, text_rect)

    screen.blit(title_text, title_rect)  # Display the title

    pygame.display.flip()

pygame.quit()
sys.exit()
