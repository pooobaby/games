#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020


# noinspection PyPep8Naming
class Solver(object):
    def __init__(self):
        self.count = 0

    @staticmethod
    def startPos(board):
        """ 取出第一个位置为空的数 """
        for x in range(9):
            for y in range(9):
                if board[x][y] == 0:
                    return x, y
        return False, False

    @staticmethod
    def nextPos(board, x, y):
        """ 取出下一个位置为空的数"""
        for j in range(y+1, 9):
            if board[x][j] == 0:
                return x, j
        for i in range(x+1, 9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return -1, -1

    @staticmethod
    def mayNum(board, x, y):
        """ 得到当前位置上符合横，纵，九宫格条件的数字列表, 这个代码太简洁了 """
        i = x // 3
        j = y // 3
        # 得到当前位置所在九宫格内的所有数字列表
        area = [board[i*3+r][j*3+c] for r in range(3) for c in range(3)]
        # 用所有数字的列表减去横、纵、九宫格的数字，然后去重, list(zip(*board)是将列表进行转置
        num = set([x for x in range(1, 10)]) - set(area) - set(board[x]) - set(list(zip(*board))[y])
        return list(num)

    def fillNum(self, board, x, y):
        """ 主函数，用递归填写数字 """
        num_list = self.mayNum(board, x, y)
        for num in num_list:
            self.count += 1
            board[x][y] = num
            next_x, next_y = self.nextPos(board, x, y)
            if next_y == -1:
                return board
            else:
                # 如果下一个单元格没有可能填写的数字时，for循环不执行，函数直接结束，返回的结果是None
                end = self.fillNum(board, next_x, next_y)
                if end is None:
                    board[x][y] = 0
                else:
                    return board

    @staticmethod
    def isValid(data):
        """ 判断整个数独是否有效 """
        for y in range(9):
            for x in range(9):
                if data[y][x] > 9:
                    # print('数独中的数字大于9，无效')
                    return False

                if data[y][x] != 0 and data[y].count(data[y][x]) > 1:
                    # print('数独中的第{}行中有重复数字{}，无效'.format(y, data[y][x]))
                    return False

                for col in range(9):
                    if data[y][x] != 0 and col != y:
                        if data[col][x] == data[y][x]:
                            # print('数独中的第{}列中有重复数字{}，无效'.format(x, data[y][x]))
                            return False

                for i in range(3):
                    for j in range(3):
                        if data[y][x] != 0 and (i + 3 * (y // 3), j + 3 * (x // 3)) != (y, x):
                            if data[i + 3 * (y // 3)][j + 3 * (x // 3)] == data[y][x]:
                                # print('数独中的九宫格中有重复数字{}，无效'.format(data[y][x]))
                                return False
        return True

    def solveSudoku(self, board):
        if self.isValid(board):
            x, y = self.startPos(board)
            solved_board = self.fillNum(board, x, y)
            return solved_board
