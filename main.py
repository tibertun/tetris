import pygame,sys
from game import Game

pygame.init()
screen = pygame.display.set_mode((300, 600))
screen.fill((0, 0, 0))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

game = Game()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 100)

#головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == game_update and not game.game_over:
            game.move_down()

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)