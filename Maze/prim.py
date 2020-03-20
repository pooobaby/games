#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

from random import choice
import pygame


# 保存基本信息类，用于保存和获取迷宫算法使用的基础地图信息
class SetupInfo(object):
    WIDTH = 81
    HEIGHT = 51
    MAP_EMPTY = 0
    MAP_BLOCK = 1
    WALL_LEFT = 0
    WALL_UP = 1
    WALL_RIGHT = 2
    WALL_DOWN = 3
    START_X = 0
    START_Y = 0

    FPS = 60
    BLOCK = 10
    BORDER = 20
    SCREEN_WIDTH = WIDTH * BLOCK + BORDER * 2
    SCREEN_HEIGHT = HEIGHT * BLOCK + BORDER * 2
    WALL_COLOR = (128, 128, 128)
    CLEAR_COLOR = (76, 141, 174)
    ROUTE_COLOR = (12, 137, 24)
    START_POINT_COLOR = (255, 255, 255)
    END_POINT_COLOR = (87, 66, 102)


# noinspection PyPep8Naming,PyUnusedLocal
class MapBaseOperate(object):
    def __init__(self, width, height):
        """ 保存地图信息的二维数据，值为0表示该单元可以移动，值为1表示该单元是墙 """
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def resetMap(self, value):
        """ 将整个map单元设置为某个值的函数 """
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)

    def setMap(self, x, y, value):
        """设置某个单元为某个值的函数 x, y转置更符合常规坐标轴的思维 """
        if value == SetupInfo.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == SetupInfo.MAP_BLOCK:
            self.map[y][x] = 1
        else:
            self.map[y][x] = 'X'

    def isVisited(self, x, y):
        """ 某个单元是否被访问，x, y转置更符合常规坐标轴的思维 """
        return self.map[y][x] != 1

    def showMap(self):
        """ 显示地图 """
        for row in self.map:
            s = ''
            for entry in row:
                if entry == 0:
                    s += ' .'
                elif entry == 1:
                    s += ' #'
                else:
                    s += ' X'
            print(s)


# noinspection PyPep8Naming
class CreateMaze(object):
    def __init__(self, maze_map):
        self.maze_map = maze_map
        self.route_list = []

    def checkAdjacentPos(self, x, y, width, height, checklist):
        """ 检查当前迷宫单元的是否有未访问的相邻单元，
        如果有，则随即选取一个相邻单元，标记为已访问，并去掉当前迷宫单元与相邻迷宫单元之间的墙。
        如果没有，则不做操作
        """
        directions = []
        # 通过x, y的位置，判断哪个方向的墙是可以访问的并加入到方向列表中
        if x > 0:
            if not self.maze_map.isVisited(2 * (x - 1) + 1, 2 * y + 1):
                directions.append(SetupInfo.WALL_LEFT)
                # print('左边 的单元{}没被访问'.format((2 * (x - 1) + 1, 2 * y + 1)))
        if y > 0:
            if not self.maze_map.isVisited(2 * x + 1, 2 * (y - 1) + 1):
                directions.append(SetupInfo.WALL_UP)
                # print('上边 的单元{}没被访问'.format((2 * x + 1, 2 * (y - 1) + 1)))
        if x < width - 1:
            if not self.maze_map.isVisited(2 * (x + 1) + 1, 2 * y + 1):
                directions.append(SetupInfo.WALL_RIGHT)
                # print('右边 的单元{}没被访问'.format((2 * (x + 1) + 1, 2 * y + 1)))
        if y < height - 1:
            if not self.maze_map.isVisited(2 * x + 1, 2 * (y + 1) + 1):
                directions.append(SetupInfo.WALL_DOWN)
                # print('下边 的单元{}没被访问'.format((2 * x + 1, 2 * (y + 1) + 1)))

        if len(directions):  # 如果方向列表中非空
            direction = choice(directions)  # 随机选择一个方向
            if direction == SetupInfo.WALL_LEFT:
                self.maze_map.setMap(2 * (x - 1) + 1, 2 * y + 1, SetupInfo.MAP_EMPTY)  # 将相邻单元格标记为0
                self.maze_map.setMap(2 * x, 2 * y + 1, SetupInfo.MAP_EMPTY)  # 打通两个单元格的墙
                checklist.append((x - 1, y))  # 将相邻单元格加入栈
                # print('--随机选择 向左， 加入{}'.format((x - 1, y)))
            elif direction == SetupInfo.WALL_UP:
                self.maze_map.setMap(2 * x + 1, 2 * (y - 1) + 1, SetupInfo.MAP_EMPTY)
                self.maze_map.setMap(2 * x + 1, 2 * y, SetupInfo.MAP_EMPTY)
                checklist.append((x, y - 1))
                # print('--随机选择 向上,  加入{}'.format((x, y - 1)))
            elif direction == SetupInfo.WALL_RIGHT:
                self.maze_map.setMap(2 * (x + 1) + 1, 2 * y + 1, SetupInfo.MAP_EMPTY)
                self.maze_map.setMap(2 * x + 2, 2 * y + 1, SetupInfo.MAP_EMPTY)
                checklist.append((x + 1, y))
                # print('--随机选择 向右,  加入{}'.format((x + 1, y)))
            elif direction == SetupInfo.WALL_DOWN:
                self.maze_map.setMap(2 * x + 1, 2 * (y + 1) + 1, SetupInfo.MAP_EMPTY)
                self.maze_map.setMap(2 * x + 1, 2 * y + 2, SetupInfo.MAP_EMPTY)
                checklist.append((x, y + 1))
                # print('--随机选择 向下,  加入{}'.format((x, y + 1)))
            return True
        else:
            # print('当前迷宫单元没有未访问的相邻迷宫单元')
            return False  # 如果没有，返回False，出栈

    def recursiveBackTracker(self, width, height, start_x, start_y):
        """ 算法主循环
        算法主循环，重复下面步骤直到检查列表为空：
            - 随机选择一个迷宫单元作为起点，加入检查列表并标记为已访问
            - 当检查列表非空时，随机从列表中取出一个迷宫单元，进行循环
        如果当前迷宫单元有未被访问过的相邻迷宫单元
            - 随机选择一个未访问的相邻迷宫单元
            - 去掉当前迷宫单元与相邻迷宫单元之间的墙
            - 标记相邻迷宫单元为已访问，并将它加入检查列表
        否则，当前迷宫单元没有未访问的相邻迷宫单元
            - 则从检查列表删除当前迷宫单元
        """
        self.maze_map.setMap(2 * start_x + 1, 2 * start_y + 1, SetupInfo.MAP_EMPTY)  # 起点标记为已访问
        checklist, end_list = [], []  # 用列表做为一个栈, 设定存储栈顶元素、路径的列表
        checklist.append((start_x, start_y))  # 将起点加入栈
        count = 0
        while len(checklist):  # 当栈中非空时
            # print('第%d步 --------' % count)
            entry = choice(checklist)                       # Prim算法与回溯算法只有这条语句不同
            # print('随机选择：{}，迷宫单元列表：{}, '.format(entry, checklist))
            if not self.checkAdjacentPos(entry[0], entry[1], width, height, checklist):
                checklist.remove(entry)  # 当前迷宫单元没有未访问的相邻迷宫单元，出栈
            count += 1
        return end_list

    # noinspection PyUnusedLocal
    def getMazeRoute(self, maze_map, end_list, start_x, start_y):
        """ 输出起终点和迷宫路径 """
        for n in range(end_list.index(max(end_list)) + 1):  # 从起点到栈的长度最大时，将所有栈顶的迷宫单元提取出来就是路径
            route_x = 2 * end_list[n][1][0] + 1  # 获取经过迷宫单元的坐标
            route_y = 2 * end_list[n][1][1] + 1
            route_next_x = 2 * end_list[n + 1][1][0] + 1  # 获取下一步迷宫单元的坐标
            route_next_y = 2 * end_list[n + 1][1][1] + 1
            wall_x = int((route_x + route_next_x) / 2)  # 得到经过的墙的坐标
            wall_y = int((route_y + route_next_y) / 2)
            self.route_list.append((route_x, route_y))
            self.route_list.append((wall_x, wall_y))
        self.route_list.pop()  # 把最后的墙pop()掉
        end_x = self.route_list[-1][0]  # 路径列表中的最后一个元素就是终点
        end_y = self.route_list[-1][1]

        """ 下面是将路径列表中重复走过的坐标删除，没有想到更好的办法，不过这是自己想出来的，也挺高兴 """
        route_list_copy = self.route_list.copy()
        len_route = len(self.route_list)
        for n in range(len_route):
            for j in range(n + 1, len_route):
                if j >= len_route:
                    continue
                else:
                    if self.route_list[n] == self.route_list[j]:
                        for k in range(n, j):
                            route_list_copy.pop(n)
                            self.route_list = route_list_copy
                        len_route = len(self.route_list)
                        j = len
            continue
        self.route_list = route_list_copy

        maze_map.setMap(2 * start_x + 1, 2 * start_y + 1, 'X')  # 在迷宫地图上标记起终点
        maze_map.setMap(end_x, end_y, 'X')

    def doRecursiveBackTracker(self):
        # 主函数，先调用resetMap函数将地图都设置为墙
        self.maze_map.resetMap(SetupInfo.MAP_BLOCK)
        self.recursiveBackTracker((SetupInfo.WIDTH - 1) // 2, (SetupInfo.HEIGHT - 1) // 2,
                                  SetupInfo.START_X, SetupInfo.START_Y)


# noinspection PyPep8Naming
class DrawMaze(object):
    def __init__(self, maze_map):
        self.screen = pygame.display.set_mode((SetupInfo.SCREEN_WIDTH, SetupInfo.SCREEN_HEIGHT))  # 创建屏幕对象
        pygame.display.set_caption('{}*{} Maze'.format(SetupInfo.WIDTH, SetupInfo.HEIGHT))  # 窗口标题
        self.clock = pygame.time.Clock()
        self.color = SetupInfo.CLEAR_COLOR  # 首先设置路径块与迷宫单元块的颜色相同
        self.maze = maze_map
        # self.route_list = route_list
        self.no_route = True

    def display(self):
        """ 在窗口中显示迷宫，按任意键显示路径 """
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # 按鼠标显示路径，再按取消显示
                    if self.no_route:
                        self.color = SetupInfo.ROUTE_COLOR
                        self.no_route = False
                    else:
                        self.color = SetupInfo.CLEAR_COLOR
                        self.no_route = True

            self.drawMap()
            self.clock.tick(SetupInfo.FPS)
            pygame.display.update()

    def drawMap(self):
        """ 用遍历取出迷宫数据并在窗口中画颜色块 """
        for i, line in enumerate(self.maze):
            for j, value in enumerate(line):
                rect = (j * SetupInfo.BLOCK + SetupInfo.BORDER, i * SetupInfo.BLOCK + SetupInfo.BORDER,
                        SetupInfo.BLOCK, SetupInfo.BLOCK)
                if value == 1:
                    pygame.draw.rect(self.screen, SetupInfo.WALL_COLOR, rect, 0)
                elif value == 0:
                    pygame.draw.rect(self.screen, SetupInfo.CLEAR_COLOR, rect, 0)
                else:
                    pygame.draw.rect(self.screen, SetupInfo.END_POINT_COLOR, rect, 0)


def main():
    maze_map = MapBaseOperate(SetupInfo.WIDTH, SetupInfo.HEIGHT)
    create_maze = CreateMaze(maze_map)
    create_maze.doRecursiveBackTracker()
    # maze_map.showMap()
    DrawMaze(maze_map.map).display()


if __name__ == "__main__":
    main()
