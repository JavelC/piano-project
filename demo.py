import pygame
import musicpy as mp
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Piano")
clock = pygame.time.Clock()
running = True

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")
test_rect = test_surface.get_rect(topleft=(80, 200))
c = mp.note("C", duration=3)
mp.write(c, name="C.mid")


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.blit(test_surface, test_rect)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if test_rect.collidepoint(mouse_pos):
                pygame.mixer.music.load("C.mid")
                pygame.mixer.music.play()
                test_surface.fill("Blue")
        if event.type == pygame.MOUSEBUTTONUP:
            if test_rect.collidepoint(mouse_pos):
                pygame.mixer.music.pause()
                test_surface.fill("Red")

    pygame.display.flip()
