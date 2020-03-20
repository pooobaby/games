#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

"""
用递归的方法解决迷宫问题，加入了可以自动生成迷宫，但有些问题还不是很明白
生成迷宫用了很笨的方法，在生成20行、列以上的迷宫时会很慢
"""

import random
import pygame

FPS = 60
ROW = 10
COL = 10
BLOCK = 20
BORDER = 20
SCREEN_WIDTH = COL * BLOCK + BORDER * 2
SCREEN_HEIGHT = ROW * BLOCK + BORDER * 2
IMPOSSIBLE_COLOR = (128, 128, 128)
POSSIBLE_COLOR = (76, 141, 174)
ROUTE_COLOR = (12, 137, 24)


# noinspection PyPep8Naming
class DrawMaze(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # 创建屏幕对象
        pygame.display.set_caption('{}*{} Maze'.format(ROW, COL))               # 窗口标题
        self.clock = pygame.time.Clock()
        self.color = POSSIBLE_COLOR                 # 首先设置路径块与可能块的颜色相同
        self.maze = MakeMaze().create(ROW, COL)
        self.no_route = True

    def display(self):
        """ 在窗口中显示迷宫，按任意键显示路径 """
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:    # 按鼠标显示路径，再按取消显示
                    if self.no_route:
                        self.color = ROUTE_COLOR
                        self.no_route = False
                    else:
                        self.color = POSSIBLE_COLOR
                        self.no_route = True
                if event.type == pygame.KEYDOWN:            # 按任意键重新生成迷宫
                    self.maze = MakeMaze().create(ROW, COL)

            self.drawBlock(self.color)
            self.clock.tick(FPS)
            pygame.display.update()

    def drawBlock(self, color):
        """ 用遍历取出迷宫数据并在窗口中画颜色块 """
        for i, line in enumerate(self.maze):
            for j, value in enumerate(line):
                rect = (j * BLOCK + BORDER, i * BLOCK + BORDER, BLOCK, BLOCK)
                if value == 0:
                    pygame.draw.rect(self.screen, IMPOSSIBLE_COLOR, rect, 0)
                elif value == 1:
                    pygame.draw.rect(self.screen, POSSIBLE_COLOR, rect, 0)
                else:
                    pygame.draw.rect(self.screen, color, rect, 0)


# noinspection PyPep8Naming
class MakeMaze(object):
    def __init__(self):
        self.route_list = []        # 初始化路线列表

    # noinspection PyUnusedLocal
    def create(self, x, y):
        """ 生成迷宫 """
        route_list = []  # 初始化路线列表
        while True:
            maze = [[random.choice([0, 1]) for j in range(y)] for i in range(x)]
            maze[0][0] = 1
            if self.walk(maze, 0, 0):
                return maze

    def walk(self, maze, x, y):
        """
        如果位置是迷宫的出口，说明成功走出迷宫
        依次向下、右、左、上进行探测，走的通就返回True，然后继续探测，走不通就返回False
        """
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            maze[x][y] = 2                      # 将出口位置做标记
            return True

        if self.validPos(maze, x, y):           # 递归主体实现
            self.route_list.append((x, y))      # 将位置加入路线列表中
            maze[x][y] = 2                      # 做标记，防止折回
            if self.walk(maze, x + 1, y) or self.walk(maze, x, y + 1) \
                    or self.walk(maze, x, y - 1) or self.walk(maze, x - 1, y):
                return True
            else:
                maze[x][y] = 1                  # 没走通把上一步位置标记取消，以便能够退回
                self.route_list.pop()           # 在位置列表中删除位置，即最后一个元素
                return False
        return False

    @staticmethod
    def pprint(maze):
        """ 打印迷宫 """
        [print(n) for n in maze]

    @staticmethod
    def validPos(maze, x, y):
        """ 判断坐标的有效性，如果超出数组边界或是不满足值为1的条件，说明该点无效返回False，否则返回True """
        if len(maze) > x >= 0 and len(maze[0]) > y >= 0 and maze[x][y] == 1:
            return True
        else:
            return False


def main():
    drawer = DrawMaze()                 # 用迷宫生成画图对象
    drawer.display()                    # 显示迷宫


if __name__ == '__main__':
    main()
