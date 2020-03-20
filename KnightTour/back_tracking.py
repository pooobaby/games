#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame


class SetupInfo(object):
    ROW = 8        # 这里定义的是x的值，即纵向的数目
    COL = 8        # 这里定义的是y的值，即横向的数目
    START_X = 0
    START_Y = 0
    DIRECTION_DICT = {1: (-2, -1), 2: (-1, -2), 3: (1, -2), 4: (2, -1), 5: (2, 1), 6: (1, 2), 7: (-1, 2), 8: (-2, 1)}

    FPS = 60
    BLOCK = 50
    BORDER = 20
    UP_BORDER = 30
    SCREEN_WIDTH = ROW * BLOCK + BORDER * 2
    SCREEN_HEIGHT = COL * BLOCK + UP_BORDER + BORDER
    BACKGROUND_COLOR = (128, 128, 128)
    BLACK_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    KNIGHT_IMG = r'.\images\knight.png'
    FLAG_IMG = r'.\images\flag.png'
    TEXT_FONT = r'.\fonts\arial.ttf'
    TEXT_COLOR = (0, 0, 0)
    TEXT_SIZE = 14


# noinspection PyPep8Naming
class Knight(object):
    # noinspection PyUnusedLocal
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(self.height)] for i in range(self.width)]
        self.direction_dict = SetupInfo.DIRECTION_DICT

    def isVisited(self, x, y):
        """ 判断棋盘上的点是否被访问过 """
        return self.board[x][y] != 1

    def validPos(self, x, y):
        """ 判断坐标点是否在棋盘内 """
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    def print(self):
        """ 打印棋盘 """
        for row in self.board:
            char = ''
            for s in row:
                if s == 0:
                    char += ' .'
                elif s == 1:
                    char += ' X'
            print(char)

    def checkPoint(self, x, y, point_list):
        """ 从8个方向中按序取值
        判断下一步是否在棋盘内，如果在棋盘内并且没有被访问过
            - 将下一步的点标记为已访问
            - 同时加入列表
            - 返回True
        否则：
            - 继续试探下一个方向，如果8个方向都走不通就返回False
        """
        for k in self.direction_dict:
            direction = self.direction_dict[k]
            next_x = x + direction[0]
            next_y = y + direction[1]
            if self.validPos(next_x, next_y):
                if self.isVisited(next_x, next_y):
                    self.board[next_x][next_y] = 1
                    point_list.append((next_x, next_y))
                    return True
            else:
                continue
        return False

    def go(self):
        """ 主运行函数
        定义一个坐标点的列表为栈，加入起点
        当列表不为空时
            - 取出栈顶的点
            - 从这个点开始走一步，如果可以走就继续取下一个点循环
            - 不能走就删除栈顶的元素，退回一步继续尝试
        总的运算次数 = 2 * ROW * COL - 2，ROW, COL为行和列的数值
        """
        count = 0
        route_list = []
        point_list = [(SetupInfo.START_X, SetupInfo.START_Y)]
        self.board[SetupInfo.START_X][SetupInfo.START_Y] = 1
        while len(point_list):
            count += 1
            point = point_list[-1]
            route_list.append(point)
            if not self.checkPoint(point[0], point[1], point_list):
                point_list.pop()
        # print('总计走了%d步' % (count-1))
        # print('所有的步数：\n{}'.format(route_list))
        return route_list


# noinspection PyPep8Naming
class Drawing(object):
    def __init__(self, route_list):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SetupInfo.SCREEN_WIDTH, SetupInfo.SCREEN_HEIGHT))
        self.screen.fill(SetupInfo.BACKGROUND_COLOR)
        self.route_list = route_list
        self.knight = pygame.image.load(SetupInfo.KNIGHT_IMG)
        self.flag = pygame.image.load(SetupInfo.FLAG_IMG)
        self.step = 1
        self.text_font = pygame.font.Font(SetupInfo.TEXT_FONT, SetupInfo.TEXT_SIZE)
        pygame.display.set_caption('骑士游历问题的演示')

    def display(self):
        """ 界面显示，把棋盘画在主循环外面，在循环体中只画各种元素 """
        self.drawChessBoard()
        self.drawKnight(self.knight, self.route_list[0])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.step < len(self.route_list):
                            self.drawBlock(self.route_list[self.step-1])
                            self.drawKnight(self.flag, self.route_list[self.step-1])
                            self.drawKnight(self.knight, self.route_list[self.step])
                            self.step += 1
            self.drawText()
            self.clock.tick(SetupInfo.FPS)
            pygame.display.update()

    def drawText(self):
        """ 显示文字信息 """
        text = 'The {} step  current location {}'.format(self.step-1, self.route_list[self.step-1])
        text_surf = self.text_font.render(text, False, SetupInfo.TEXT_COLOR)
        self.screen.blit(text_surf, (SetupInfo.BORDER, (SetupInfo.UP_BORDER - SetupInfo.TEXT_SIZE)/2))

    def drawChessBoard(self):
        """ 画棋盘 """
        for i in range(SetupInfo.ROW):
            for j in range(SetupInfo.COL):
                rect = (i * SetupInfo.BLOCK + SetupInfo.BORDER, j * SetupInfo.BLOCK + SetupInfo.UP_BORDER,
                        SetupInfo.BLOCK, SetupInfo.BLOCK)
                if i % 2 == 0:
                    color = SetupInfo.BLACK_COLOR if j % 2 == 0 else SetupInfo.WHITE_COLOR
                else:
                    color = SetupInfo.WHITE_COLOR if j % 2 == 0 else SetupInfo.BLACK_COLOR
                pygame.draw.rect(self.screen, color, rect, 0)

    def drawBlock(self, step):
        """ 画一个块 用来盖住上一步的骑士和文字信息 """
        text_rect = (SetupInfo.BORDER, 0, SetupInfo.SCREEN_HEIGHT-SetupInfo.BORDER, SetupInfo.UP_BORDER)
        block_rect = (step[0] * SetupInfo.BLOCK + SetupInfo.BORDER, step[1] * SetupInfo.BLOCK + SetupInfo.UP_BORDER,
                      SetupInfo.BLOCK, SetupInfo.BLOCK)
        if step[0] % 2 == 0:
            color = SetupInfo.BLACK_COLOR if step[1] % 2 == 0 else SetupInfo.WHITE_COLOR
        else:
            color = SetupInfo.WHITE_COLOR if step[1] % 2 == 0 else SetupInfo.BLACK_COLOR
        pygame.draw.rect(self.screen, SetupInfo.BACKGROUND_COLOR, text_rect, 0)
        pygame.draw.rect(self.screen, color, block_rect, 0)

    def drawKnight(self, image, step):
        """ 画骑士 """
        step = (step[0]*SetupInfo.BLOCK+SetupInfo.BORDER, step[1]*SetupInfo.BLOCK+SetupInfo.UP_BORDER)
        self.screen.blit(image, step)


def main():
    knight = Knight(SetupInfo.ROW, SetupInfo.COL)
    end_list = knight.go()
    # knight.print()
    Drawing(end_list).display()


if __name__ == '__main__':
    main()
