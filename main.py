import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Piano")
clock = pygame.time.Clock()
running = True

#size for each white key
white_key_width = 100
white_key_height = 400

#size for each black
black_key_width = 60
black_key_height = 200


#initilize each white key
white_keys = {
    'C': pygame.Surface((white_key_width, white_key_height)),
    'D': pygame.Surface((white_key_width, white_key_height)),
    'E': pygame.Surface((white_key_width, white_key_height)),
    'F': pygame.Surface((white_key_width, white_key_height)),
    'G': pygame.Surface((white_key_width, white_key_height)),
    'A': pygame.Surface((white_key_width, white_key_height)),
    'B': pygame.Surface((white_key_width, white_key_height))
}

#initilizes each black key
black_keys = {
    'C#': pygame.Surface((black_key_width, black_key_height)),
    'D#': pygame.Surface((black_key_width, black_key_height)),
    'F#': pygame.Surface((black_key_width, black_key_height)),
    'G#': pygame.Surface((black_key_width, black_key_height)),
    'A#': pygame.Surface((black_key_width, black_key_height)),
}

#places each white key according to, key : x position
white_key_positions_x = {
    'C': 0,
    'D': 100,
    'E': 200,
    'F': 300,
    'G': 400,
    'A': 500,
    'B': 600
}

#places each black key according to, key : x position
black_key_positions_x = {
    'C#': 65,
    'D#': 170,
    'F#': 365,
    'G#': 465,
    'A#': 550
}


#for each white key, 
for key, surface in white_keys.items():
  outline_color = (100, 100, 100)  # Define the color for the outline
  surface.fill((200, 200, 200))
  
  # Create a white rectangle with an outline on the surface
  white_rect = pygame.Surface((white_key_width, white_key_height))
  white_rect.fill((200, 200, 200)) 
  
  # Fill the rectangle with gray color 
  #white_rect.get_rect gets position of rectangle and thickness of outline
  pygame.draw.rect(white_rect, (100, 100, 100), white_rect.get_rect(), 4) 

  
  # Blit the white rectangle onto the screen
  screen.blit(white_rect, (white_key_positions_x[key], 0))  
  


# For each black key, fill the surface with black color and move at the specified position
for key, surface in black_keys.items():
    surface.fill((0, 0, 0))  # Fill the surface with black color

   # Blit the black key surface onto the screen
    screen.blit(surface, (black_key_positions_x[key], 0))  

# Add a red block
red_block_rect = pygame.Rect(0, 0, 40, 40)
pygame.draw.rect(screen, (90, 0, 0), red_block_rect)


pygame.display.flip()


while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_x, mouse_y = event.pos
          # Check if the mouse click is within the red block
          if red_block_rect.collidepoint(mouse_x, mouse_y):
              pygame.quit()
              exit()

  pygame.display.flip()
  clock.tick(60)