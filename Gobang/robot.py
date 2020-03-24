#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

from setup import *


# noinspection PyPep8Naming
class AI(object):
    # noinspection PyUnusedLocal
    def __init__(self, maps):
        self.maps = maps
        self.is_end = False

    @staticmethod
    def inBoard(x, y):
        """ 判断当前位置是否在棋盘内部 """
        return True if ROW > x >= 0 and COL > y >= 0 else False

    def downOk(self, x, y):
        """ 判断当前位置是否可以落子 """
        return True if self.inBoard(x, y) and self.maps[x][y] is None else False

    def sameColor(self, x, y, i):
        """ 判断当前位置是否与给定的棋子(i值)相同 """
        return True if self.inBoard(x, y) and self.maps[x][y] == i else False

    def numInLine(self, x, y, d):
        """ 在给定的方向direct(direct区分正负)上，和该点相同棋子的个数 """
        i = x + DX[d]
        j = y + DY[d]
        same_num = 0
        piece = self.maps[x][y]
        if piece is None:
            return 0
        while self.sameColor(i, j, piece):
            same_num = same_num + 1
            i = i + DX[d]
            j = j + DY[d]
        return same_num

    def numOfSameKey(self, x, y, d, i, key, same_key):
        """ 统计在d方向上，和key值相同的点的个数，即和key同色的连子个数 """
        if i == 1:
            while self.sameColor(x + DX[d] * i, y + DY[d] * i, key):
                same_key += 1
                i += 1
        elif i == -1:
            while self.sameColor(x + DX[d] * i, y + DY[d] * i, key):
                same_key += 1
                i -= 1
        return same_key, i

    def judgeResult(self, x, y):
        """ 从八个方向判断是否有五子相连的情况, 先判断是否有五子相连，再判断平局 """
        piece = self.maps[x][y]
        for d in range(8):
            same_key, i = self.numOfSameKey(x, y, d, 1, piece, 1)
            if same_key == 5:
                if piece == '1':
                    return 'B'
                elif piece == '0':
                    return 'W'

        none_count = 0
        for row in self.maps:
            for i in row:
                if i is None:
                    none_count += 1
        if none_count == 0:
            return 'T'
        return 'C'

    def liveFour(self, x, y):
        """ 该点四个方向里(即v不区分正负)，活四局势的个数 """
        key = self.maps[x][y]
        s = 0
        for d in range(4):
            same_key = 1
            same_key, i = self.numOfSameKey(x, y, d, 1, key, same_key)
            if not self.downOk(x + DX[d] * i, y + DY[d] * i):
                continue
            same_key, i = self.numOfSameKey(x, y, d, -1, key, same_key)
            if not self.downOk(x + DX[d] * i, y + DX[d] * i):
                continue
            if same_key == 4:
                s = s + 1
        return s

    def chongFour(self, x, y):
        """ 该点八个方向里(即v区分正负)，冲四局势的个数 """
        key = self.maps[x][y]
        s = 0
        for d in range(8):
            same_key = 0
            flag = True
            i = 1
            while self.sameColor(x+DX[d]*i, y+DY[d]*i, key) or flag:
                if not self.sameColor(x+DX[d]*i, y+DY[d]*i, key):
                    if flag and self.inBoard(x+DX[d]*i, y+DY[d]*i) and self.maps[x+DX[d]*i][y+DY[d]*i] is not None:
                        same_key -= 10
                    flag = False
                same_key += 1
                i += 1
            i -= 1
            if not self.inBoard(x+DX[d]*i, y+DY[d]*i):
                continue
            same_key, i = self.numOfSameKey(x, y, d, -1, key, same_key)
            if same_key == 4:
                s += 1
        return s - self.liveFour(x, y) * 2

    def liveThree(self, x, y):
        """ 该点四个方向里活三，以及八个方向里断三的个数 """
        key = self.maps[x][y]
        s = 0
        for d in range(4):
            same_key = 1
            same_key, i = self.numOfSameKey(x, y, d, 1, key, same_key)
            if not self.downOk(x+DX[d]*i, y+DY[d]*i):
                continue
            if not self.downOk(x+DX[d]*(i+1), y+DY[d]*(i+1)):
                continue
            same_key, i = self.numOfSameKey(x, y, d, -1, key, same_key)
            if not self.downOk(x+DX[d]*i, y+DY[d]*i):
                continue
            if not self.downOk(x+DX[d]*(i-1), y+DX[d]*(i-1)):
                continue
            if same_key == 3:
                s += 1
        for d in range(8):
            same_key = 0
            flag = True
            i = 1
            while self.sameColor(x+DX[d]*i, y+DY[d]*i, key) or flag:
                if not self.sameColor(x+DX[d]*i, y+DY[d]*i, key):
                    if flag and self.inBoard(x+DX[d]*i, y+DY[d]*i) and self.maps[x+DX[d]*i][y+DY[d]*i] is not None:
                        same_key -= 10
                    flag = False
                same_key += 1
                i += 1
            if not self.downOk(x+DX[d]*i, y+DY[d]*i):
                continue
            if self.inBoard(x+DX[d]*(i-1), y+DX[d]*(i-1)) and self.maps[x+DX[d]*(i-1)][y+DX[d]*(i-1)] is None:
                continue
            same_key, i = self.numOfSameKey(x, y, d, -1, key, same_key)
            if not self.downOk(x+DX[d]*i, y+DY[d]*i):
                continue
            if same_key == 3:
                s += 1
        return s

    def gameOver(self, x, y):
        """  如果有五子连线，估分最大10000 """
        for d in range(4):
            if (self.numInLine(x, y, d) + self.numInLine(x, y, d + 4)) >= 4:
                return True
        return False

    def getScore(self, x, y):
        """ 主评估函数，返回评估得分 """
        if self.gameOver(x, y):
            return 10000
        score = self.liveFour(x, y) * 1000 + (self.chongFour(x, y) + self.liveThree(x, y)) * 100
        for d in range(8):
            if self.inBoard(x+DX[d], y+DY[d]) and self.maps[x+DX[d]][y+DY[d]] is not None:
                score = score + 1
        return score

    def layerOne(self):
        """ 博弈树第一层，极大值，自己层 """
        l1_max = -100000
        if self.maps[int((COL-1)/2)][int((ROW-1)/2)] is None:
            return int((COL-1)/2), int((ROW-1)/2)
        pos_x = -1
        pos_y = -1
        for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.maps[x][y] = '0'
                score = self.getScore(x, y)
                if score == 0:
                    self.maps[x][y] = None
                    continue
                if score == 10000:
                    return x, y
                score = self.layerTwo(l1_max)
                self.maps[x][y] = None
                if score > l1_max:
                    l1_max = score
                    pos_x = x
                    pos_y = y
        print('{}, score:{}'.format((pos_x, pos_y), l1_max))
        return pos_x, pos_y

    def layerTwo(self, l1_max):
        """ 博弈树第二层，极小值，对手层 """
        l2_min = 100000
        for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.maps[x][y] = '1'
                score = self.getScore(x, y)
                if score == 0:
                    self.maps[x][y] = None
                    continue
                if score == 10000:
                    self.maps[x][y] = None
                    return -10000
                score = self.layerThree(score, l2_min)
                if score < l1_max:
                    self.maps[x][y] = None
                    return -10000
                self.maps[x][y] = None
                if score < l2_min:
                    l2_min = score
        return l2_min

    def layerThree(self, l2_score, l2_min):
        """ 博弈树第三层 """
        three_max = -100000
        for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.maps[x][y] = '0'
                score = self.getScore(x, y)
                if score == 0:
                    self.maps[x][y] = None
                    continue
                if score == 10000:
                    self.maps[x][y] = None
                    return -10000
                if score - l2_score * 2 > l2_min:
                    self.maps[x][y] = None
                    return 10000
                self.maps[x][y] = None
                if score - l2_score * 2 > three_max:
                    three_max = score - l2_score * 2
        return three_max

    @staticmethod
    def changePos(x, y):
        """ 首先判断坐标是否在棋盘内，然后将鼠标坐标转换为棋盘上的点坐标，否则返回False
        :return: [(符合棋盘点的坐标), 轮换值, 胜负结果]
        """
        # 判断坐标是否在棋盘内
        if x < L_BORDER - PIECE_NEAR or x > L_BORDER + (ROW-1) * SPACE + PIECE_NEAR:
            return False
        if y < T_BORDER - PIECE_NEAR or y > T_BORDER + (COL-1) * SPACE + PIECE_NEAR:
            return False
        # 将坐标转换为符合棋盘上点的坐标
        x_int = (x - L_BORDER) // SPACE
        y_int = (y - T_BORDER) // SPACE
        if x - L_BORDER - PIECE_NEAR <= x_int * SPACE:
            x_c = L_BORDER + x_int * SPACE
        elif x - L_BORDER + PIECE_NEAR >= (x_int + 1) * SPACE:
            x_c = L_BORDER + (x_int + 1) * SPACE
        else:
            return False
        if y - T_BORDER - PIECE_NEAR <= y_int * SPACE:
            y_c = T_BORDER + y_int * SPACE
        elif y - T_BORDER + PIECE_NEAR >= (y_int + 1) * SPACE:
            y_c = T_BORDER + (y_int + 1) * SPACE
        else:
            return False
        # 将坐标转换为数组坐标，需要将x, y转置
        x_n = (y_c - T_BORDER) // SPACE
        y_n = (x_c - L_BORDER) // SPACE
        return [(x_c, y_c), (x_n, y_n)]
