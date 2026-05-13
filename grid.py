import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_cols)] for j in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end= " ")
            print()

    def is_in_grid(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        else:
            return False

    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        else:
            return False

    def is_row_full(self, row):
        for col in range(self.num_cols):
            if self.grid[row][col] == 0:
                return False
        return True

    def clear_row(self, row):
        for col in range(self.num_cols):
            self.grid[row][col] = 0

    def move_row_down(self, row, num_rows):
        for col in range(self.num_cols):
            self.grid[row+num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0


    # def get_cell_color(self):
    #     dark_grey = (26, 31, 40) #порожня клітинка
    #     green = (47, 230, 23) #S фігура
    #     red = (232, 18, 18) #Z фігура
    #     orange = (226, 116, 17) #L фігура
    #     yellow = (237, 234, 4) #O фігура
    #     purple = (166, 0, 247) #T фігура
    #     cyan = (21, 204, 209) #I фігура
    #     blue = (13, 64, 216) #J фігура
    #
    #     return [dark_grey, green, red, orange, yellow, purple, cyan, blue]

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 11, row * self.cell_size + 11, self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
