#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from configs import *
import random
import time


class LinkLink(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_W, WIN_H))
        self.logo = pygame.image.load(LOGO_FILE)
        self.clock = pygame.time.Clock()
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption('连连看')
        self.win_text_font = pygame.font.Font(TEXT_FONT, WIN_TEXT_SIZE)
        self.info_text_font = pygame.font.Font(TEXT_FONT, INFO_TEXT_SIZE)

        self.icon_list = self.createIconList()
        self.stop = False
        self.choice = []
        self.route_list = []
        self.time_start = time.time()

    def start(self):
        """ 主程序，负责循环和显示 """
        maps = self.createMap()
        while True:
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if not self.stop:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            maps = self.judgeChoice(maps, x, y)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            self.restartGame()
                            maps = self.createMap()

            self.drawScreen(maps)
            self.drawTag()
            self.drawOver()
            self.drawCountTime()
            self.clock.tick(FPS)
            pygame.display.update()

    def judgeChoice(self, maps, x, y):
        """ 选择图案后如果是选择的第2个，判断是否连通，判断是否游戏结束 """
        if WIN_W - R_BORDER > x > L_BORDER and WIN_H - B_BORDER > y > T_BORDER:
            x_n = (x - L_BORDER) // ICON_SIZE
            y_n = (y - T_BORDER) // ICON_SIZE
            # 如果选择的图案为空或者已存在于self.choice列表中，直接返回
            if maps[y_n][x_n] == 0 or (y_n, x_n) in self.choice:
                return maps
            self.choice.append((y_n, x_n))
            self.drawTag()
            pygame.display.flip()
            # print((x, y), (x_n, y_n), self.choice)
            if len(self.choice) == 2:
                self.route_list = self.judgeLink(maps, self.choice)
                if self.route_list:
                    if maps[self.choice[0][0]][self.choice[0][1]] == maps[self.choice[1][0]][self.choice[1][1]]:
                        for n in self.choice:
                            maps[n[0]][n[1]] = 0
                    else:
                        self.route_list = []
                    self.drawLine()
                    pygame.display.flip()
                    time.sleep(2)
                    self.judgeOver(maps)
                self.choice = []
                self.route_list = []
        return maps

    @staticmethod
    def judgeLink(maps, choice):
        """ 判断是否相连 """
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        start_first_list, end_list, route_list, start_turn_list = [], [], [], []
        pos_start = choice[0]
        pos_end = choice[1]
        start_first_list.append(pos_start)
        end_list.append(pos_end)

        # 如果两个图案相邻，可以消除
        if pos_end[0] - pos_start[0] == 0:
            if abs(pos_end[1] - pos_start[1]) == 1:
                route_list.append(pos_start)
                route_list.append(pos_end)
                return route_list
        if pos_end[1] - pos_start[1] == 0:
            if abs(pos_end[0] - pos_start[0]) == 1:
                route_list.append(pos_start)
                route_list.append(pos_end)
                return route_list

        # 开始单元格四个方向为空的坐标加入列表
        for n in range(len(direction)):
            x_s = pos_start[0] + direction[n][0]
            y_s = pos_start[1] + direction[n][1]
            while maps[x_s][y_s] == 0 and len(maps)-1 >= x_s >= 0 and len(maps[0])-1 >= y_s >= 0:
                # print('x_s: %d, y_s: %d' % (x_s, y_s))
                start_first_list.append((x_s, y_s))
                x_s = x_s + direction[n][0]
                y_s = y_s + direction[n][1]
                if x_s > len(maps) - 1 or x_s < 0 or y_s > len(maps[0]) - 1 or y_s < 0:
                    break
        # print('start_first_list: %s' % start_first_list)

        # 在start_list列表中遍历所有单元格，将为空的坐标为入列表
        for pos in start_first_list:
            for n in range(len(direction)):
                x_s = pos[0] + direction[n][0]
                y_s = pos[1] + direction[n][1]
                if x_s > len(maps) - 1 or x_s < 0 or y_s > len(maps[0]) - 1 or y_s < 0:
                    continue
                while maps[x_s][y_s] == 0 and len(maps) - 1 >= x_s >= 0 and len(maps[0]) - 1 >= y_s >= 0:
                    if (x_s, y_s) in start_first_list:
                        break
                    start_turn_list.append((x_s, y_s))
                    x_s = x_s + direction[n][0]
                    y_s = y_s + direction[n][1]
                    if x_s > len(maps) - 1 or x_s < 0 or y_s > len(maps[0]) - 1 or y_s < 0:
                        break
        # print('start_turn_list: %s' % start_turn_list)

        # 结束单元格四个方向为空的坐标加入列表
        for n in range(len(direction)):
            x_e = pos_end[0] + direction[n][0]
            y_e = pos_end[1] + direction[n][1]
            while maps[x_e][y_e] == 0 and len(maps)-1 >= x_e >= 0 and len(maps[0])-1 >= y_e >= 0:
                # print('x_s: %d, y_s: %d' % (x_e, y_e))
                end_list.append((x_e, y_e))
                x_e = x_e + direction[n][0]
                y_e = y_e + direction[n][1]
                if x_e > len(maps) - 1 or x_e < 0 or y_e > len(maps[0]) - 1 or y_e < 0:
                    break
        # print('end_list: %s' % end_list)

        route_list.append(start_first_list[0])
        # 如果在开始的初始列表中有相同的单元格，连接线为两条
        for i in start_first_list:
            for j in end_list:
                if j == i:
                    route_list.append(i)
                    route_list.append(end_list[0])
                    # print('route_list: %s' % route_list)
                    # print()
                    return route_list

        # 如果在开始的转向列表中有相同的单元格，连接线为三条
        for i in start_turn_list:
            for j in end_list:
                if j == i:
                    for n in start_first_list[1:]:
                        if n[0] == i[0] or n[1] == i[1]:
                            route_list.append(n)
                    route_list.append(i)
                    route_list.append(end_list[0])
                    # print('route_list: %s' % route_list)
                    # print()
                    return route_list

    def restartGame(self):
        """ 重新游戏，参数初始化 """
        self.stop = False
        self.choice = []
        self.time_start = time.time()

    def drawScreen(self, maps):
        """ 显示屏幕和各种图案 """
        self.screen.fill(BG_COLOR)
        for x in range(len(maps)):
            for y in range(len(maps[0])):
                index = maps[x][y]
                if index == 0:
                    continue
                icon = self.icon_list[index-1]
                pos = (L_BORDER + y * ICON_SIZE, T_BORDER + x * ICON_SIZE)
                rect = (L_BORDER + y * ICON_SIZE, T_BORDER + x * ICON_SIZE, ICON_SIZE, ICON_SIZE)
                self.screen.blit(icon, pos)
                pygame.draw.rect(self.screen, CELL_COLOR, rect, 1)

    def drawLine(self):
        # 在选择的图案上画连接线
        if self.route_list and len(self.route_list) >= 2:
            for n in range(len(self.route_list) - 1):
                start = self.route_list[n]
                end = self.route_list[n + 1]
                start_pos = (L_BORDER + start[1] * ICON_SIZE + ICON_SIZE / 2,
                             T_BORDER + start[0] * ICON_SIZE + ICON_SIZE / 2)
                end_pos = (L_BORDER + end[1] * ICON_SIZE + ICON_SIZE / 2,
                           T_BORDER + end[0] * ICON_SIZE + ICON_SIZE / 2)
                pygame.draw.line(self.screen, LINE_COLOR, start_pos, end_pos, 2)

    def drawTag(self):
        # 在选择的图案上画和标记
        if len(self.choice):
            for n in self.choice:
                rect = (L_BORDER + n[1] * ICON_SIZE, T_BORDER + n[0] * ICON_SIZE, ICON_SIZE, ICON_SIZE)
                pygame.draw.rect(self.screen, TAG_COLOR, rect, 2)

    def drawCountTime(self):
        time_end = time.time()
        time_count = time_end - self.time_start
        if not self.stop:
            text_surf = self.info_text_font.render('{} sec'.format(int(time_count)), True, TEXT_COLOR)
            text_rect = text_surf.get_rect()
            text_rect.bottomright = (WIN_W - ICON_SIZE, (T_BORDER + ICON_SIZE) / 2)
            self.screen.blit(text_surf, text_rect)

    def drawOver(self):
        """ 显示游戏结束并按F1重新开始 """
        if self.stop:
            text_surf = self.win_text_font.render('You Win, Press F1 ReStart', True, TEXT_COLOR)
            text_rect = text_surf.get_rect()
            text_rect.center = (WIN_W / 2, WIN_H / 2)
            self.screen.blit(text_surf, text_rect)

    # noinspection PyUnusedLocal
    @staticmethod
    def createMap():
        """ 随机生成地图，初始的二维数组是外围多一圈空白的数组 """
        maps = [[0 for i in range(COL+2)] for j in range(ROW+2)]
        temp_list = []
        for i in range(1, COL+1):
            for j in range(1, ROW+1):
                temp_list.append(i)
        random.shuffle(temp_list)
        # print(temp_list)
        for x in range(1, ROW+1):
            for y in range(1, COL+1):
                maps[x][y] = temp_list[(x-1)*COL+(y-1)]

        # for i in maps:
        #     print(i)
        return maps

    @staticmethod
    def createIconList():
        """ 随机提取小图标 """
        icon_list = []
        index_list = random.sample(range(1, 17), ICON_KIND)
        for index in index_list:
            icon_file = ICONS_IMG + str(index) + '.png'
            icon_list.append(pygame.image.load(icon_file))
        return icon_list

    def judgeOver(self, maps):
        """ 判断游戏是否结束 """
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] != 0:
                    return False
        self.stop = True
        return True


def main():
    link_link = LinkLink()
    link_link.start()


if __name__ == '__main__':
    main()
