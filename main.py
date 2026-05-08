import pygame,sys
from grid import Grid
from blocks import *

pygame.init()
screen = pygame.display.set_mode((300, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

game_grid = Grid()

block = LBlock()


#головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_grid.draw(screen)
    block.draw(screen)
    pygame.display.update()
    clock.tick(60)