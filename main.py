# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_rectangle(screen, rect, color, thickness):
    pygame.draw.rect(screen, color, rect, thickness)

my_rect1 = [100, 100, 200, 150]
thickness1 = 8   

def draw_circle(screen, center, radius, color, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)

circle_center = (500, 200)  
circle_radius = 50          
circle_color = config.SUNSETORANGE  
circle_thickness = 0 

def draw_line(surface, color, start_pos, end_pos, thickness):
    pygame.draw.line(surface, color, start_pos, end_pos, thickness)


def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        draw_rectangle(screen, my_rect1, config.AQUAMARINE, thickness1)
        draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)
        draw_line(screen, config.FIREBRICK, [200,300], [777,666], 4)

        pygame.display.flip()

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()