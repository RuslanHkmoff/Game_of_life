import pygame as p
import random as r
from pygame.locals import *
import copy
#цвет клеток
cells_colour = (0, 200, 64)
#цвет экрана
background = (0, 0, 0)
# экран
p.display.set_caption('game_life')
# зададим экран и его размеры
screen_size = p.display.set_mode((600, 600))
n = screen_size.get_height() // 20
k = screen_size.get_width() // 20


class Cell:
    # создаем множество клеток и функции состояний
    cells = set()

    def __init__(self, coord_x, coord_y, lively):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.lively = lively
        Cell.cells.add(self)
        return

    def death(self): # функция смерти клетки
        self.lively = False
        return

    def revival(self): # функция оживления клетки
        self.lively = True
        return

    def neibours(self): # функция определения соседей клетки
        cnt = 0
        for coord_z in Cell.cells:
            if coord_z.lively:
                if coord_z.coord_x == (self.coord_x + 1) and coord_z.coord_y == self.coord_y:
                    cnt += 1
                elif coord_z.coord_x == self.coord_x - 1 and coord_z.coord_y == self.coord_y - 1:
                    cnt += 1
                elif coord_z.coord_x == (self.coord_x - 1) and coord_z.coord_y == self.coord_y:
                    cnt += 1
                elif coord_z.coord_x == self.coord_x and coord_z.coord_y == self.coord_y + 1:
                    cnt += 1
                elif coord_z.coord_x == self.coord_x - 1 and coord_z.coord_y == self.coord_y + 1:
                    cnt += 1
                elif coord_z.coord_x == self.coord_x + 1 and coord_z.coord_y == self.coord_y - 1:
                    cnt += 1
                elif coord_z.coord_x == self.coord_x and coord_z.coord_y == self.coord_y - 1:
                    cnt += 1
                elif coord_z.coord_x == (self.coord_x + 1) and coord_z.coord_y == self.coord_y + 1:
                    cnt += 1
        return cnt


class Game_life:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        return

    def generation0(self): # задаем начальное положение клеток (нулевое поколение)
        for i in range(n):
            for j in range(k):
                Cell(i, j, r.choice([True, False]))
        return

    def phase(self):
        for i in p.event.get():
            if i.type == QUIT:
                quit()
        for q in Cell.cells:
            p.draw.rect(screen_size, (cells_colour if q.lively else background), [q.coord_y * 20, q.coord_x * 20, 20, 20])


        new_cells = set()
        for cell in Cell.cells:
            new_cell = copy.deepcopy(cell)
            if cell.neibours() not in (2, 3):
                new_cell.death()
            if cell.neibours() == 3:
                new_cell.revival()
            new_cells.add(new_cell)
        Cell.cells = copy.deepcopy(new_cells)
        p.display.update()
        return

    def play(self):
        self.generation0()
        while 1:
            self.phase()
        return


game = Game_life(n, k)
game.play()
