#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from setup import *
from robot import AI


# noinspection PyPep8Naming,PyUnusedLocal
class State(object):
    def __init__(self):
        """ 各参数说明：
        map[x][y]: None(初始化), '1'(黑棋), '0'(白棋)
        turn: '1'(黑棋), '0'(白棋)
        result: 'B'(白棋), 'W'(黑棋), 'T'(平局)
        """
        self.maps = [[None for j in range(ROW)] for i in range(COL)]
        self.screen = self.defineScreen()
        self.clock = pygame.time.Clock()
        self.ai = AI(self.maps)
        self.step_count = 0
        self.step_list = []
        self.turn = 0
        self.starting = True

    @staticmethod
    def defineScreen():
        """ 定义游戏窗口 """
        screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
        logo = pygame.image.load(LOGO_IMG)
        pygame.display.set_icon(logo)
        pygame.display.set_caption('五子棋')
        return screen

    def reStart(self):
        """ 重新开始游戏 """
        self.maps = [[None for j in range(ROW)] for i in range(COL)]
        self.turn = 0
        self.starting = True
        self.step_count = 0
        self.step_list = []
        self.ai = AI(self.maps)

    def startGame(self):
        """ 判断游戏是否进行中 """
        return self.starting is True

    def humanPiece(self):
        """ 处理落子，返回落子坐标，棋子类型，结果文本 """
        x, y = pygame.mouse.get_pos()
        pos = self.ai.changePos(x, y)
        if pos:
            if self.changeData(pos[1][0], pos[1][1], self.turn):
                # 判断结果如何
                result_text = self.resultText(pos[1])
                if result_text:
                    self.starting = False
                # print('POS: {}, ARRAY: {}, RESULT: {}'.format(pos[0], pos[1], result_text))
                # self.printMap()
                self.step_count += 1
                self.step_list.append((self.step_count, self.turn, pos[1]))
                return pos[0], self.turn, result_text, self.starting, self.step_list

    def aiPiece(self):
        """ 调用AI下棋子 """
        pos_n = self.ai.layerOne()
        if self.changeData(pos_n[0], pos_n[1], self.turn):
            result_text = self.resultText(pos_n)
            if result_text:
                self.starting = False
            self.step_count += 1
            self.step_list.append((self.step_count, self.turn, pos_n))
            pos_c = (pos_n[1]*SPACE+L_BORDER, pos_n[0]*SPACE+T_BORDER)
            # self.printMap()
            return pos_c, self.turn, result_text, self.starting, self.step_list

    def changeData(self, x, y, turn):
        """ 如果在数组地图的坐标可以下棋子，返回True，同时改变表中的数据 """
        if self.maps[x][y] is None:
            if turn == 1:
                self.turn = 0
            else:
                self.turn = 1
            self.maps[x][y] = str(self.turn)
            return True

    def resultText(self, pos):
        """ 判断结果并返回结果文字，调用AI时需要重新传入一次数组 """
        result = AI(self.maps).judgeResult(pos[0], pos[1])
        # print(result)
        if result == 'B':
            result_text = 'Black wins'
        elif result == 'W':
            result_text = 'White wins'
        elif result == 'T':
            result_text = 'The game has drawn'
        else:
            result_text = None
        return result_text

    def printMap(self):
        """ 打印数组地图 """
        for row in self.maps:
            ss = ''
            for s in row:
                if s == '0':
                    ss += ' O'
                elif s == '1':
                    ss += ' X'
                else:
                    ss += ' .'
            print(ss)
