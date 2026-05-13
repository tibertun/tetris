import pygame
import sys
from game import Game

pygame.init()

screen = pygame.display.set_mode((300, 600))
screen.fill((0, 0, 139))


title_font = pygame.font.Font(None, 40)

score_surface = title_font.render("Score", True, (255, 255, 255))
next_surface = title_font.render("Next", True, (255, 255, 255))

game_over_surface = title_font.render("Game Over", True, (255, 255, 255))

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
screen.fill((0, 0, 0))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

game = Game()

game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP:
                game.rotate()

        if event.type == game_update:
            game.move_down()
    score_value_surface = title_font.render(str(game.score), True, (255, 255, 255))

    screen.fill((44, 44, 127))
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50,50))
    if game.game_over == True:

      screen.blit (game_over_surface, (320, 450,50,50))


    pygame.draw.rect(screen, (59, 85, 162), score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, (59, 85, 162), next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)