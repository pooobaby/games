#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

""" 递归回溯法处理八皇后问题, 这个解法非常简洁并且易懂 """

import pygame

ROW = 8
FPS = 60
BLOCK = 50
BORDER = 10
W_WIDTH = ROW * BLOCK + BORDER * 2
W_HEIGHT = ROW * BLOCK + BORDER * 2
BACKGROUND_COLOR = (178, 93, 37)
BLACK_COLOR = (22, 24, 35)
WHITE_COLOR = (233, 231, 239)
QUEEN_IMG = r'.\images\queen.png'
LOGO_IMG = r'.\images\logo.ico'
TEXT_FONT = r'.\fonts\arial.ttf'
TEXT_COLOR = (0, 0, 0)
TEXT_SIZE = 14


class Queen(object):
    def __init__(self):
        self.count = 0              # 统计共有多少个解的计数器
        self.array_list = []        # 用来保存结果的列表

    def calculate(self, array, cur):
        """ 主算法函数 """
        if cur == len(array):
            self.count += 1
            self.array_list.append(array.copy())
            return
        for col in range(len(array)):
            array[cur] = col
            flag = True
            for row in range(cur):
                if array[row] == col or abs(col - array[row]) == cur - row:
                    flag = False
                    break
            if flag:
                self.calculate(array, cur+1)


# noinspection PyPep8Naming
class Painter(object):
    def __init__(self, solutions):
        pygame.init()
        self.solutions = solutions
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
        self.screen.fill(BACKGROUND_COLOR)
        self.logo = pygame.image.load(LOGO_IMG)
        pygame.display.set_icon(self.logo)
        self.queen_img = pygame.image.load(QUEEN_IMG)
        self.text_font = pygame.font.Font(TEXT_FONT, TEXT_SIZE)
        pygame.display.set_caption('八皇后问题的演示, 共%d种解法' % self.solutions)

    def drawing(self, array_list):
        """ 主显示函数，用左右方向键控制显示第N个解 """
        self.drawChessBoard()
        count = 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        count -= 1
                    if event.key == pygame.K_RIGHT:
                        count += 1
            self.drawChessBoard()
            if count < 1:
                count = self.solutions
            elif count > self.solutions:
                count = 1
            if count <= self.solutions:
                self.drawQueen(array_list, count - 1)
                pygame.display.set_caption('八皇后问题的演示，第%d种解法，共%d种' %
                                           (int(count), self.solutions))

            self.clock.tick(FPS)
            pygame.display.update()

    def drawQueen(self, array_list, n):
        """ 画皇后 """
        for i in array_list[n]:
            x = i
            y = array_list[n][i]
            pos = (x * BLOCK + BORDER, y * BLOCK + BORDER)
            self.screen.blit(self.queen_img, pos)

    def drawChessBoard(self):
        """ 画棋盘 """
        for i in range(ROW):
            for j in range(ROW):
                rect = (i * BLOCK + BORDER, j * BLOCK + BORDER,
                        BLOCK, BLOCK)
                if i % 2 == 0:
                    color = BLACK_COLOR if j % 2 == 0 else WHITE_COLOR
                else:
                    color = WHITE_COLOR if j % 2 == 0 else BLACK_COLOR
                pygame.draw.rect(self.screen, color, rect, 0)


def main():
    queen = Queen()
    queen.calculate([None]*ROW, 0)
    solutions = queen.count
    solutions_list = queen.array_list
    painter = Painter(solutions)
    painter.drawing(solutions_list)


if __name__ == '__main__':
    main()
