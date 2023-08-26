import pygame
import sys
import os 
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Un livre dont vous êtes le héros')

# Load icon and background
programIcon = pygame.image.load(resource_path('Icon/dragon_icon.png'))
background = pygame.image.load(resource_path('assets/wp5381270-epic-winter-fantasy-wallpapers.jpg'))

# Define colors
WHITE = (255, 255, 255)
SINISTER_COLOR = (50, 50, 50)
BUTTON_COLOR = (120, 160, 180)
HOVER_COLOR = (150, 190, 210)  # Color when button is hovered over

# Set up font
Buttonfont = pygame.font.Font(None, 30)
Titlefont = pygame.font.Font(resource_path("Icon/You Are Scared.ttf"), 80)

#Music
m1 = pygame.mixer.Sound(resource_path("music/wind-outside-sound-ambient-141989.mp3"))
m2 = pygame.mixer.Sound(resource_path("a-piano-with-a-creepy-atmosphere-for-scary-stories-demo-version-158423.mp3"))

# Set volume for the music tracks
m1.set_volume(0.9)
m2.set_volume(0.8)

# Start playing the music tracks
m1.play(-1)
m2.play(-1)

# Create text
title_text = Titlefont.render('The Snowy Paths', True, WHITE)
title_rect = title_text.get_rect(center=(screen.get_width() // 2, 250))

# Snowflake class
class Snowflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 4)
        self.speed = random.randint(1, 3)
    
    def move(self):
        self.y += self.speed
        if self.y > screen.get_height():
            self.y = random.randint(-10, -1)
            self.x = random.randint(0, screen.get_width())
    
    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

def draw_buttons(button, color):
    pygame.draw.rect(screen, color, button, border_radius=12)

def main():
    # Create a button rect
    buttonPlay = pygame.Rect(0, 0, 200, 60)
    buttonExit = pygame.Rect(0, 0, 200, 60)
    
    # Center the buttons on the screen
    buttonPlay.center = (screen.get_width() // 2, screen.get_height() // 2 - 40)
    buttonExit.center = (screen.get_width() // 2, screen.get_height() // 2 + 80)

    button_text_Play = Buttonfont.render("Play", True, WHITE)
    button_text_Exit = Buttonfont.render("Exit", True, WHITE)

    hovered_play = False
    hovered_exit = False

    snowflakes = [Snowflake(random.randint(0, screen.get_width()), random.randint(0, screen.get_height())) for _ in range(100)]

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                hovered_play = buttonPlay.collidepoint(event.pos)
                hovered_exit = buttonExit.collidepoint(event.pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if buttonExit.collidepoint(event.pos):
                        running = False

        for flake in snowflakes:
            flake.move()

        screen.blit(background, (0, 0))

        for flake in snowflakes:
            flake.draw()

        draw_buttons(buttonExit, HOVER_COLOR if hovered_exit else BUTTON_COLOR)
        draw_buttons(buttonPlay, HOVER_COLOR if hovered_play else BUTTON_COLOR)

        text_rect = button_text_Exit.get_rect(center=buttonExit.center)
        screen.blit(button_text_Exit, text_rect)

        text_rect = button_text_Play.get_rect(center=buttonPlay.center)
        screen.blit(button_text_Play, text_rect)

        screen.blit(title_text, title_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
