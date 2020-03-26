#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import numpy as np
from config import *
from solve import Solver


# noinspection PyPep8Naming
class Creater(object):
    def __init__(self):
        self.row = ROW
        self.col = COL
        self.solver = Solver()
        self.dig_list = [(8, 8)]
        self.bb = []

    def createSudoku(self, level):
        """ 生成数独 """
        while True:
            array = np.zeros((self.row, self.col), np.int)  # 生成一个全是0的数组
            rg = np.arange(1, self.row + 1)  # 生成一个1-9的数列
            # m[0, :]表示第一行，从rg中，随机选取大小为n的数据，replace表示是否重用元素，即抽取出来的数据是否放回原数组中
            array[0, :] = np.random.choice(rg, self.row, replace=False)
            # 在下面的循环中，如果出错，证明上面生成的随机数不合理，重新再来一遍
            try:
                for r in range(1, self.row):  # 从第2行开始
                    for c in range(self.col):
                        # np.setdiff1d找到rg, array[:r, c]中集合元素的差异。返回在rg中但不在m[:r, c]中的已排序的唯一值。
                        col_rest = np.setdiff1d(rg, array[:r, c])
                        row_rest = np.setdiff1d(rg, array[r, :c])
                        # np.intersect1d返回两个数组共有的唯一值数组(按值排序)
                        avb1 = np.intersect1d(col_rest, row_rest)
                        # 获取九宫格的左顶点
                        sub_r, sub_c = r // 3, c // 3
                        # np.ravel()得到扁平化数字列表,得到九宫格中数字的列表，np.setdiff1d返回在[1-9]中但不在扁平化数字列表中的列表
                        avb2 = np.setdiff1d(np.arange(0, self.row + 1),
                                            array[sub_r * 3:(sub_r + 1) * 3, sub_c * 3:(sub_c + 1) * 3].ravel())
                        # 返回[行列可能的数]与[九宫格可能的数]共有的唯一值数组(按值排序)
                        avb = np.intersect1d(avb1, avb2)
                        # 如果返回的列表不为空，随机取一个数填入这个单元格中
                        array[r, c] = np.random.choice(avb, size=1)
                break
            except ValueError:
                pass
        board = array.copy()
        print('生成的初始数组：')
        self.printBoard(board)
        print()
        # 随机生成9*9的bool值数组，并按次序将值为True的单元格赋值为0
        board[np.random.choice([True, False], size=array.shape, p=[level, 1 - level])] = 0
        return board.tolist()

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
