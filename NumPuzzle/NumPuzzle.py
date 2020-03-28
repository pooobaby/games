#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
import random

ROW = 4
FPS = 10
BLOCK = 100
BORDER = 10
W_WIDTH = ROW * BLOCK + BORDER * 2
W_HEIGHT = ROW * BLOCK + BORDER * 2
BACKGROUND_COLOR = (66, 80, 102)
LINE_COLOR = (255, 251, 240)
BLOCK_COLOR = (46, 78, 126)
ZERO_BLOCK_COLOR = (128, 128, 128)
TEXT_COLOR = (255, 251, 240)
WIN_TEXT_COLOR = (255, 166, 49)
TEXT_SIZE = 48
WIN_TEXT_SIZE = 36
TEXT_FONT = r'.\fonts\impact.ttf'
LOGO_IMG = r'.\images\logo.ico'


# noinspection PyPep8Naming,PyUnusedLocal,PyTypeChecker
class NumPuzzle(object):
    def __init__(self):
        pygame.init()
        self.board = [[None for i in range(4)] for j in range(4)]
        self.starting = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
        self.screen.fill(BACKGROUND_COLOR)
        self.text_font = pygame.font.Font(TEXT_FONT, TEXT_SIZE)
        self.win_text_font = pygame.font.Font(TEXT_FONT, WIN_TEXT_SIZE)
        self.logo = pygame.image.load(LOGO_IMG)
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('数字华容道')

    def restart(self):
        """ 重新开始游戏 """
        self.starting = True
        for i in range(4):
            for j in range(4):
                self.board[i][j] = i * 4 + j + 1
        """ 打乱初始化数组的顺序 """
        for n in range(10):
            move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            x, y = self.getPos(16)
            if x == 0:
                move.remove((-1, 0))
            if x == 3:
                move.remove((1, 0))
            if y == 0:
                move.remove((0, -1))
            if y == 3:
                move.remove((0, 1))
            move_n = random.choice(move)
            x_n = x + move_n[0]
            y_n = y + move_n[1]
            self.board[x][y], self.board[x_n][y_n] = self.board[x_n][y_n], self.board[x][y]

    def playing(self):
        """ 主函数，负责主循环 """
        self.restart()
        self.drawBoard()
        self.drawNum(self.board)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    x, y = self.getPos(16)
                    self.control(event, x, y)
                    self.drawBoard()
                    self.drawNum(self.board)
                    if self.judgeWin():
                        self.winGame()
            self.clock.tick(FPS)
            pygame.display.update()

    def drawBoard(self):
        """ 画棋盘 """
        self.screen.fill(BACKGROUND_COLOR)
        for j in range(4):
            for i in range(4):
                rect = (i * BLOCK + BORDER, j * BLOCK + BORDER, BLOCK, BLOCK)
                pygame.draw.rect(self.screen, BLOCK_COLOR, rect, 0)
                rect = (i * BLOCK + BORDER, j * BLOCK + BORDER, BLOCK, BLOCK)
                pygame.draw.rect(self.screen, LINE_COLOR, rect, 4)

    def drawNum(self, board):
        """ 画数字和空的格子 """
        for j in range(4):
            for i in range(4):
                num = board[j][i]
                if num == 16:
                    rect = (i * BLOCK + BORDER + 3, j * BLOCK + BORDER + 3, BLOCK - 5, BLOCK - 5)
                    pygame.draw.rect(self.screen, ZERO_BLOCK_COLOR, rect, 0)
                    num = ''
                text_surf = self.text_font.render(str(num), True, TEXT_COLOR)
                text_rect = text_surf.get_rect()
                text_rect.center = (i * BLOCK + BORDER + BLOCK / 2, j * BLOCK + BORDER + BLOCK / 2)
                self.screen.blit(text_surf, text_rect)

    def getPos(self, value):
        """ 获得二维列表某个值的索引值 """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == value:
                    x = i
                    y = j
                    return x, y

    def control(self, event, x, y):
        """ 根据获取的键盘事件进行判断与变换操作 """
        if event.key == pygame.K_F1:
            self.restart()
            self.drawBoard()
            self.drawNum(self.board)
        if self.starting:
            if event.key == pygame.K_UP and x > 0:
                move = (-1, 0)
            elif event.key == pygame.K_DOWN and x < 3:
                move = (1, 0)
            elif event.key == pygame.K_LEFT and y > 0:
                move = (0, -1)
            elif event.key == pygame.K_RIGHT and y < 3:
                move = (0, 1)
            else:
                move = (0, 0)
            x_n = x + move[0]
            y_n = y + move[1]
            self.board[x][y], self.board[x_n][y_n] = self.board[x_n][y_n], self.board[x][y]

    @staticmethod
    def printBoard(board):
        """ 打印数组，测试用 """
        for x in range(len(board)):
            line = ''
            for y in range(len(board[x])):
                line += '{:3d}'.format(board[x][y])
            print(line)

    def judgeWin(self):
        """ 判断当前状态是否胜利 """
        judge_list = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == i * 4 + j + 1:
                    judge_list.append('OK')
        if len(judge_list) == 16:
            self.starting = False
            return True
        return False

    def winGame(self):
        """ 显示获胜信息 """
        text_surf = self.win_text_font.render('You Win, Press F1 ReStart', True, WIN_TEXT_COLOR)
        text_rect = text_surf.get_rect()
        text_rect.center = (W_WIDTH / 2, W_HEIGHT / 2)
        self.screen.blit(text_surf, text_rect)


def main():
    num_puzzle = NumPuzzle()
    num_puzzle.playing()


if __name__ == '__main__':
    main()
