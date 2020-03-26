#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import time
from config import *
from solve import Solver
from create import Creater


# noinspection PyPep8Naming
class Commander(object):
    def __init__(self):
        self.creater = Creater()

    @staticmethod
    def printBoard(board):
        """ 打印数独列表 """
        for row in board:
            s = ''
            for n in row:
                if n == 0:
                    s += ' .'
                else:
                    s += ' %d' % n
            print(s)

    def createSudoku(self):
        """ 生成一个数独数组 """
        time_s = time.time()
        board = self.creater.createSudoku(LEVEL)
        # --------------------
        print('最后生成的数独是：')
        time_e = time.time()
        self.printBoard(board)
        print('生成程序执行时间：{:.04f}秒'.format(time_e - time_s))
        print()
        # --------------------
        return board

    def solveSudoku(self, board):
        """ 解决并打印数独 """
        time_s = time.time()
        solver = Solver()
        solved_board = solver.solveSudoku(board)
        time_e = time.time()
        # --------------------
        self.printBoard(solved_board)
        print('解决程序执行时间：{:.04f}秒， 共执行了{}次递归'.format(time_e - time_s, solver.count))
        # --------------------
