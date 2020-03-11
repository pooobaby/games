#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import random
import pygame
from initialize import BaseInit


# noinspection PyPep8Naming
class Level1(BaseInit):
    def __init__(self):
        super().__init__()
        self.level_text = 'level 01'
        self.bird = self.bird_1
        self.bird_size = self.bird_1_size
        self.bird_v = self.bird_1_v
        self.bird_speed = self.bird_1_speed
        self.life_space = self.life_1_space
        self.life_size = self.life_1_size
        self.life = self.life_1
        self.plank = self.plank_1
        self.cloud = self.cloud_1
        self.plank_y = self.plank_1_y
        self.plank_size = self.plank_1_size

        self.tools = PublicTools()

    def start(self, bird_life):
        """
        -- 第1关中的主函数，返回生命值
        :return: bird_life：过完此关还剩余的生命值
        """
        score = 0
        bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v = self.resetData()    # 游戏参数复位

        self.screen.blit(self.bd_level_01, (0, 0))  # 画上背景，以便显示level 1
        self.tools.levelDisplay(self.level_text)     # 调用levelDisplay()显示level 1
        while bird_life:
            self.screen.blit(self.bd_level_01, (0, 0))  # 画上背景
            life_x, life_y = self.tools.lifeText(bird_life, self.life, self.life_space, self.life_size)     # 显示生命值

            bird_x = bird_x + bird_vx * v_up / self.fps
            bird_y = bird_y + bird_vy * v_up / self.fps
            plank_x = pygame.mouse.get_pos()[0]             # 获得鼠标的x位置

            self.tools.levelText(self.level_text)            # 显示关卡信息
            self.tools.scoreText(score)       # 显示得分的文字
            self.screen.blit(self.plank, (plank_x, self.plank_y))     # 画木板
            self.screen.blit(bird, (int(bird_x), int(bird_y)))          # 画小鸟
            pygame.display.update()     # 刷新画面

            if bird_x >= self.window_w - self.bird_size or bird_x <= 0:     # 小鸟到达窗口左右两侧后折返
                bird_vx = -bird_vx
            if bird_y < 0:              # 小鸟到达窗口上端后折返
                bird_vy = -bird_vy

            if bird_y > self.plank_y - self.bird_size - 2:       # 小鸟到达木板线时
                if plank_x < bird_x < plank_x + self.plank_size[0]:        # 小鸟位于木板的宽度内时
                    score, score_v, bird_vy, bird = self.touchPlank(score, score_v, bird_x, bird_y, bird_vy)
                    # 小鸟碰到木板时调用函数touchPlank()
                    bird_y = bird_y - 5     # 小鸟的y值减少5，不然会产生连击

            if bird_y >= self.window_h - 40:        # 如果小鸟落到屏幕外面调用lostBird()
                self.tools.lostOneBird(bird_x, bird_y, life_x, life_y)         # 显示失败的相关信息，画一个乌云和-1
                bird_life = bird_life - 1       # 生命值减1
                bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v = self.resetData()    # 游戏参数复位

            if score >= self.level_01:      # 如果得分到达设定的阈值
                self.tools.passLevel(self.level_text)
                return bird_life

            for n in self.bird_speed:       # 根据得分改变小鸟的速度
                if score_v == n:
                    v_up = self.bird_speed[n]

            for event in pygame.event.get():                # 监听用户事件
                if event.type == pygame.QUIT:               # 关闭窗口时退出
                    exit()
                if event.type == pygame.KEYDOWN:            # 键盘事件发生
                    if event.key == pygame.K_SPACE:         # 按下空格键调用pause()
                        pause = True
                        self.tools.pause(pause)
                    if event.key == pygame.K_ESCAPE:        # 按下esc键返回上级菜单
                        bird_life = 'esc'
                        return bird_life

            self.clock.tick(self.fps)             # 设置FPS
        return bird_life

    def resetData(self):
        """
        -- 游戏设定值复位，输出复位后的参数数值
        :return: bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v
        """
        score_v = 0
        bird = pygame.transform.rotate(self.bird, 0)  # 设置小鸟的初始旋转角度为0
        bird_x = random.randint(0, self.window_w - self.bird_size)  # 小鸟的初始x值随机生成
        bird_y = self.bird_size / 2  # 小鸟的初始y值
        bird_vx, bird_vy = self.bird_v, self.bird_v  # 小鸟在x, y方向上的初始速度
        v_up = self.bird_speed[score_v]  # 小鸟的初始速度为1
        return bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v

    def touchPlank(self, score, score_v, bird_x, bird_y, bird_vy):
        """
        -- 小鸟与木板相碰时，速度反转，得分+1，画小星星，小鸟旋转
        :param score: 得分
        :param score_v: 本次得分
        :param bird_x: 小鸟的x值
        :param bird_y: 小鸟的y值
        :param bird_vy: 小鸟的速度
        :return: score: int; bird_vy: float; bird: Surface
        """
        bird_vy = -bird_vy
        score += 1
        score_v += 1
        self.screen.blit(self.star_1, (bird_x + self.bird_size, bird_y + self.bird_size))      # 画小星星
        bird = pygame.transform.rotate(self.bird, random.randint(0, 180))      # 随机设置小鸟旋转角度
        pygame.display.update()
        return score, score_v, bird_vy, bird


# noinspection PyPep8Naming
class Level2(BaseInit):
    def __init__(self):
        super().__init__()
        self.level_text = 'level 02'
        self.b1 = self.bird_1
        self.b2 = self.bird_2
        self.bird_size = self.bird_1_size
        self.bird_v = self.bird_1_v
        self.bird_speed = self.bird_1_speed
        self.life_space = self.life_1_space
        self.life_size = self.life_1_size
        self.life = self.life_1
        self.plank = self.plank_1
        self.cloud = self.cloud_1
        self.plank_y = self.plank_1_y
        self.plank_size = self.plank_1_size

        self.tools = PublicTools()

    def start(self, bird_life):
        """
        -- 第2关中的主函数，返回生命值
        :return: bird_life：过完此关还剩余的生命值
        """
        score = 0
        b1, b1_x, b1_y, b1_vx, b1_vy, v1_up, score1_v = self.resetData(self.b1)  # 游戏参数复位
        b2, b2_x, b2_y, b2_vx, b2_vy, v2_up, score2_v = self.resetData(self.b2)  # 游戏参数复位

        self.screen.blit(self.bd_level_02, (0, 0))  # 画上背景，以便显示level 2
        self.tools.levelDisplay(self.level_text)  # 调用levelDisplay()显示level 2
        while bird_life:
            self.screen.blit(self.bd_level_02, (0, 0))  # 画上背景
            life_x, life_y = self.tools.lifeText(bird_life, self.life, self.life_space, self.life_size)  # 显示生命值
            plank_x = pygame.mouse.get_pos()[0]  # 获得鼠标的x位置

            b1_x = b1_x + b1_vx * v1_up / self.fps
            b1_y = b1_y + b1_vy * v1_up / self.fps

            self.tools.levelText(self.level_text)  # 显示关卡信息
            self.tools.scoreText(score)  # 显示得分的文字
            self.screen.blit(self.plank, (plank_x, self.plank_y))  # 画木板
            self.screen.blit(b1, (int(b1_x), int(b1_y)))  # 画小鸟1

            if b1_x >= self.window_w - self.bird_size or b1_x <= 0:  # 小鸟1到达窗口左右两侧后折返
                b1_vx = -b1_vx
            if b1_y < 0:  # 小鸟1到达窗口上端后折返
                b1_vy = -b1_vy
            if b1_y > self.plank_y - self.bird_size - 2:  # 小鸟1到达木板线时
                if plank_x < b1_x < plank_x + self.plank_size[0]:  # 小鸟1位于木板的宽度内时
                    score, score1_v, b1_vy, b1 = self.touchPlank(self.b1, score, score1_v, b1_x, b1_y, b1_vy)
                    # 小鸟1碰到木板时调用函数touchPlank()
                    b1_y = b1_y - 5
            if b1_y >= self.window_h - 40:  # 如果小鸟1落到屏幕外面调用lostBird()
                self.tools.lostOneBird(b1_x, b1_y, life_x, life_y)  # 显示失败的相关信息，画一个乌云和-1
                bird_life = bird_life - 1  # 生命值减1
                b1, b1_x, b1_y, b1_vx, b1_vy, v1_up, score1_v = self.resetData(self.b1)  # 游戏参数复位

            if score >= 1:
                b2_x = b2_x + b2_vx * v2_up / self.fps
                b2_y = b2_y + b2_vy * v2_up / self.fps
                if b2_x >= self.window_w - self.bird_size or b2_x <= 0:  # 小鸟2到达窗口左右两侧后折返
                    b2_vx = -b2_vx
                if b2_y < 0:  # 小鸟2到达窗口上端后折返
                    b2_vy = -b2_vy
                if self.plank_y > b2_y > self.plank_y - self.bird_size - 2:       # 小鸟2到达木板线时
                    if plank_x < b2_x < plank_x + self.plank_size[0]:         # 小鸟2位于木板的宽度内时
                        score, score2_v, b2_vy, b2 = self.touchPlank(self.b2, score, score2_v, b2_x, b2_y, b2_vy)
                        # 小鸟2碰到木板时调用函数touchPlank()
                        b2_y = b2_y - 5
                if b2_y >= self.window_h - 40:  # 如果小鸟2落到屏幕外面调用lostBird()
                    self.tools.lostOneBird(b2_x, b2_y, life_x, life_y)  # 显示失败的相关信息，画一个乌云和-1
                    bird_life = bird_life - 1  # 生命值减1
                    b2, b2_x, b2_y, b2_vx, b2_vy, v2_up, score2_v = self.resetData(self.b2)  # 游戏参数复位

                self.screen.blit(b2, (int(b2_x), int(b2_y)))  # 画小鸟2

            pygame.display.update()  # 刷新画面

            if score >= self.level_02:      # 如果得分到达设定的阈值
                self.tools.passLevel(self.level_text)
                return bird_life

            for n in self.bird_speed:  # 根据得分改变小鸟的速度
                if score1_v == n:
                    v1_up = self.bird_speed[n]
                if score2_v == n:
                    v2_up = self.bird_speed[n]

            for event in pygame.event.get():  # 监听用户事件
                if event.type == pygame.QUIT:  # 关闭窗口时退出
                    exit()
                if event.type == pygame.KEYDOWN:  # 键盘事件发生
                    if event.key == pygame.K_SPACE:  # 按下空格键调用pause()
                        pause = True
                        self.tools.pause(pause)
                    if event.key == pygame.K_ESCAPE:  # 按下esc键返回上级菜单
                        bird_life = 'esc'
                        return bird_life

            self.clock.tick(self.fps)  #
        return bird_life

    def resetData(self, bird):
        """
        -- 游戏设定值复位，输出复位后的参数数值
        :return: bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v
        """
        score_v = 0
        bird = pygame.transform.rotate(bird, 0)  # 设置小鸟的初始旋转角度为0
        bird_x = random.randint(0, self.window_w - self.bird_size)  # 小鸟的初始x值随机生成
        bird_y = self.bird_size / 2  # 小鸟的初始y值
        bird_vx, bird_vy = self.bird_v, self.bird_v  # 小鸟在x, y方向上的初始速度
        v_up = self.bird_speed[score_v]  # 小鸟的初始速度为1
        return bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v

    def touchPlank(self, bird, score, score_v, bird_x, bird_y, bird_vy):
        """
        -- 小鸟与木板相碰时，速度反转，得分+1，画小星星，小鸟旋转
        :param bird：小鸟
        :param score: 得分
        :param score_v: 本次得分
        :param bird_x: 小鸟的x值
        :param bird_y: 小鸟的y值
        :param bird_vy: 小鸟的速度
        :return: score: int; bird_vy: float; bird: Surface
        """
        bird_vy = -bird_vy
        score += 1
        score_v += 1
        self.screen.blit(self.star_1, (bird_x + self.bird_size, bird_y + self.bird_size))      # 画小星星
        bird = pygame.transform.rotate(bird, random.randint(0, 180))      # 随机设置小鸟旋转角度
        pygame.display.update()
        return score, score_v, bird_vy, bird


# noinspection PyPep8Naming
class Level3(BaseInit):
    def __init__(self):
        super().__init__()
        self.level_text = 'level 03'
        self.b1 = self.bird_1
        self.b2 = self.bird_2
        self.bird_size = self.bird_1_size
        self.bird_v = self.bird_1_v
        self.bird_speed = self.bird_1_speed
        self.life_space = self.life_1_space
        self.life_size = self.life_1_size
        self.life = self.life_1
        self.plank = self.plank_1
        self.cloud = self.cloud_1
        self.plank_y = self.plank_1_y
        self.plank_size = self.plank_1_size
        self.ll = self.long
        self.ss = self.short
        self.ll_v = self.long_v
        self.ss_v = self.short_v

        self.tools = PublicTools()

    def start(self, bird_life):
        """
        -- 第3关中的主函数，返回生命值
        :return: bird_life：过完此关还剩余的生命值
        """
        score = 0
        l_s_score = self.long_short_score
        random.shuffle(l_s_score)       # 获取长短道具阈值列表并打乱顺序
        l_score = l_s_score[:int(self.long_short_times/2)]      # 将长短道具的阈值列表分开
        s_score = l_s_score[int(self.long_short_times/2):]

        b1, b1_x, b1_y, b1_vx, b1_vy, v1_up, score1_v = self.resetData(self.b1)  # 游戏参数复位
        b2, b2_x, b2_y, b2_vx, b2_vy, v2_up, score2_v = self.resetData(self.b2)  # 游戏参数复位

        long_x = random.randint(0, self.window_w - self.long_size)      # 长道具的初始x值
        long_y = self.long_size / 2         # 长道具的初始y值

        short_x = random.randint(0, self.window_w - self.short_size)      # 短道具的初始x值
        short_y = self.short_size / 2       # 短道具的初始y值

        self.screen.blit(self.bd_level_03, (0, 0))  # 画上背景，以便显示level 3
        self.tools.levelDisplay(self.level_text)  # 调用levelDisplay()显示level 3

        while bird_life:
            self.screen.blit(self.bd_level_03, (0, 0))  # 画上背景
            life_x, life_y = self.tools.lifeText(bird_life, self.life, self.life_space, self.life_size)  # 显示生命值
            plank_x = pygame.mouse.get_pos()[0]  # 获得鼠标的x位置

            b1_x = b1_x + b1_vx * v1_up / self.fps
            b1_y = b1_y + b1_vy * v1_up / self.fps

            self.tools.levelText(self.level_text)  # 显示关卡信息
            self.tools.scoreText(score)  # 显示得分的文字
            self.screen.blit(self.plank, (plank_x, self.plank_y))  # 画木板
            self.screen.blit(b1, (int(b1_x), int(b1_y)))  # 画小鸟1

            if b1_x >= self.window_w - self.bird_size or b1_x <= 0:  # 小鸟1到达窗口左右两侧后折返
                b1_vx = -b1_vx
            if b1_y < 0:  # 小鸟1到达窗口上端后折返
                b1_vy = -b1_vy
            if self.plank_y > b1_y > self.plank_y - self.bird_size - 2:  # 小鸟1到达木板线时
                if plank_x < b1_x < plank_x + self.plank_size[0]:  # 小鸟1位于木板的宽度内时
                    score, score1_v, b1_vy, b1 = self.touchPlank(self.b1, score, score1_v, b1_x, b1_y, b1_vy)
                    # 小鸟1碰到木板时调用函数touchPlank()
                    b1_y = b1_y - 5
            if b1_y >= self.window_h - 40:  # 如果小鸟1落到屏幕外面调用lostBird()
                self.tools.lostOneBird(b1_x, b1_y, life_x, life_y)  # 显示失败的相关信息，画一个乌云和-1
                bird_life = bird_life - 1  # 生命值减1
                b1, b1_x, b1_y, b1_vx, b1_vy, v1_up, score1_v = self.resetData(self.b1)  # 游戏参数复位

            if score >= 1:
                b2_x = b2_x + b2_vx * v2_up / self.fps
                b2_y = b2_y + b2_vy * v2_up / self.fps
                if b2_x >= self.window_w - self.bird_size or b2_x <= 0:  # 小鸟2到达窗口左右两侧后折返
                    b2_vx = -b2_vx
                if b2_y < 0:  # 小鸟2到达窗口上端后折返
                    b2_vy = -b2_vy
                if self.plank_y > b2_y > self.plank_y - self.bird_size - 2:       # 小鸟2到达木板线时
                    if plank_x < b2_x < plank_x + self.plank_size[0]:         # 小鸟2位于木板的宽度内时
                        score, score2_v, b2_vy, b2 = self.touchPlank(self.b2, score, score2_v, b2_x, b2_y, b2_vy)
                        # 小鸟2碰到木板时调用函数touchPlank()
                        b2_y = b2_y - 5
                if b2_y >= self.window_h - 40:  # 如果小鸟2落到屏幕外面调用lostBird()
                    self.tools.lostOneBird(b2_x, b2_y, life_x, life_y)  # 显示失败的相关信息，画一个乌云和-1
                    bird_life = bird_life - 1  # 生命值减1
                    b2, b2_x, b2_y, b2_vx, b2_vy, v2_up, score2_v = self.resetData(self.b2)  # 游戏参数复位
                self.screen.blit(b2, (int(b2_x), int(b2_y)))  # 画小鸟2

            if score in l_score:        # 当得分在长道具的阈值列表里时
                long_x, long_y, self.plank, self.plank_size, score, l_score \
                    = self.longPlank(self.plank, self.plank_size, long_x, long_y, plank_x, score, l_score)
                self.screen.blit(self.ll, (int(long_x), int(long_y)))  # 画西红柿
            if score in s_score:        # 当得分在短道具的阈值列表里时
                short_x, short_y, self.plank, self.plank_size, score, s_score \
                    = self.shortPlank(self.plank, self.plank_size, short_x, short_y, plank_x, score, s_score)
                self.screen.blit(self.ss, (int(short_x), int(short_y)))  # 画TNT

            pygame.display.update()  # 刷新画面

            for n in self.bird_speed:  # 根据得分改变小鸟的速度
                if score1_v == n:
                    v1_up = self.bird_speed[n]
                if score2_v == n:
                    v2_up = self.bird_speed[n]

            for event in pygame.event.get():  # 监听用户事件
                if event.type == pygame.QUIT:  # 关闭窗口时退出
                    exit()
                if event.type == pygame.KEYDOWN:  # 键盘事件发生
                    if event.key == pygame.K_SPACE:  # 按下空格键调用pause()
                        pause = True
                        self.tools.pause(pause)
                    if event.key == pygame.K_ESCAPE:  # 按下esc键返回上级菜单
                        bird_life = 'esc'                   # --------------------- 记得要改回'esc'
                        return bird_life
            self.clock.tick(self.fps)  #
        return bird_life

    def longPlank(self, plank, plank_size, long_x, long_y, plank_x, score, l_score):
        """
        -- 长道具使木板变长。返回改变后的木板和道具的y值
        :param plank: 当前的木板
        :param plank_size: 当前木板尺寸
        :param long_x: 长道具x值
        :param long_y: 长道具y值
        :param plank_x: 当前木板的x值
        :param score: 得分
        :param l_score: 木板阈值的列表
        :return: long_y, plank, plank_size：长道具y值，改变后的木板，改变后木板的尺寸
        """
        if long_y < self.plank_y - 2:
            long_y = long_y + self.ll_v * self.bird_speed[0] / self.fps
        if long_y >= self.plank_y - 2:  # 西红柿到达木板线时
            if plank_x < long_x < plank_x + self.plank_size[0]:  # 西红柿位于木板的宽度内时
                if self.plank_size == self.plank_1_size:  # 判断当前木板的长度
                    plank = self.plank_2
                    plank_size = self.plank_2_size
                elif self.plank_size == self.plank_3_size:  # 判断当前木板的长度
                    plank = self.plank_1
                    plank_size = self.plank_1_size
            long_x = random.randint(0, self.window_w - self.long_size)  # 长道具的初始x值
            long_y = self.long_size / 2
            l_score.remove(score)
        return long_x, long_y, plank, plank_size, score, l_score

    def shortPlank(self, plank, plank_size, short_x, short_y, plank_x, score, s_score):
        """
        -- 短道具使木板变短。返回改变后的木板和道具的y值
        :param plank: 当前的木板
        :param plank_size: 当前木板尺寸
        :param short_x: 短道具x值
        :param short_y: 短道具y值
        :param plank_x: 当前木板的x值
        :param score: 得分
        :param s_score: 木板阈值的列表
        :return: short_y, plank, plank_size：短道具y值，改变后的木板，改变后木板的尺寸
        """
        if short_y < self.plank_y - 2:
            short_y = short_y + self.ss_v * self.bird_speed[0] / self.fps
        if short_y >= self.plank_y - 2:  # TNT到达木板线时
            if plank_x < short_x < plank_x + self.plank_size[0]:  # TNT位于木板的宽度内时
                if self.plank_size == self.plank_1_size:  # 判断当前木板的长度
                    plank = self.plank_3
                    plank_size = self.plank_3_size
                elif self.plank_size == self.plank_2_size:  # 判断当前木板的长度
                    plank = self.plank_1
                    plank_size = self.plank_1_size
            short_x = random.randint(0, self.window_w - self.short_size)  # 短道具的初始x值
            short_y = self.short_size / 2
            s_score.remove(score)
        return short_x, short_y, plank, plank_size, score, s_score

    def resetData(self, bird):
        """
        -- 游戏设定值复位，输出复位后的参数数值
        :return: bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v
        """
        score_v = 0
        bird = pygame.transform.rotate(bird, 0)  # 设置小鸟的初始旋转角度为0
        bird_x = random.randint(0, self.window_w - self.bird_size)  # 小鸟的初始x值随机生成
        bird_y = self.bird_size / 2  # 小鸟的初始y值
        bird_vx, bird_vy = self.bird_v, self.bird_v  # 小鸟在x, y方向上的初始速度
        v_up = self.bird_speed[score_v]  # 小鸟的初始速度为1
        return bird, bird_x, bird_y, bird_vx, bird_vy, v_up, score_v

    def touchPlank(self, bird, score, score_v, bird_x, bird_y, bird_vy):
        """
        -- 小鸟与木板相碰时，速度反转，得分+1，画小星星，小鸟旋转
        :param bird：小鸟
        :param score: 得分
        :param score_v: 本次得分
        :param bird_x: 小鸟的x值
        :param bird_y: 小鸟的y值
        :param bird_vy: 小鸟的速度
        :return: score: int; bird_vy: float; bird: Surface
        """
        bird_vy = -bird_vy
        score += 1
        score_v += 1
        self.screen.blit(self.star_1, (bird_x + self.bird_size, bird_y + self.bird_size))      # 画小星星
        bird = pygame.transform.rotate(bird, random.randint(0, 180))      # 随机设置小鸟旋转角度
        pygame.display.update()
        return score, score_v, bird_vy, bird


# noinspection PyPep8Naming
class PublicTools(BaseInit):
    def __init__(self):
        super().__init__()

    def lostOneBird(self, bird_x, bird_y, life_x, life_y):
        # 显示失败信息，画乌云和-1
        lost_surf, lost_rect = self.textObject(self.info_font, self.lost_one_text, self.info_font_color,
                                               ((self.window_w / 2), (self.window_h / 2 - self.info_font_size * 2)),
                                               'center')
        self.screen.blit(lost_surf, lost_rect)       # 显示失败信息，位置在屏幕中央向上2倍字体尺寸
        self.screen.blit(self.cloud_1, (bird_x, bird_y))    # 画乌云
        self.screen.blit(self.lost_one, (life_x, life_y))      # 画-1
        pygame.display.update()
        pygame.time.wait(600)       # 暂停程序一段时间

    def passLevel(self, level_text):
        # 显示过关的字样
        level_surf, level_rect = self.textObject(self.info_font, 'Finish the ' + level_text + ', continue...',
                                                 self.info_font_color, (self.window_w / 2, self.window_h / 2),
                                                 'center')
        self.screen.blit(level_surf, level_rect)  # 显示Level 1
        pygame.display.update()
        pygame.time.wait(2000)  # 暂停程序一段时间

    def levelDisplay(self, level_text):
        # 显示第n关的字样
        level_surf, level_rect = self.textObject(self.info_font, level_text, self.info_font_color,
                                                 (self.window_w / 2, self.window_h / 2), 'center')
        self.screen.blit(level_surf, level_rect)  # 显示Level 1
        pygame.display.update()
        pygame.time.wait(2000)  # 暂停程序一段时间

    def scoreText(self, score):
        """
        -- 显示得分信息
        :param score: 得分数值
        :return:
        """
        score_text = self.score_text + str(score)
        score_surf, score_rect = self.textObject(self.level_font, score_text, self.level_font_color,
                                                 (self.score_text_pos[0], self.score_text_pos[1]), 'bottomleft')
        self.screen.blit(score_surf, score_rect)

    def lifeText(self, bird_life, life, life_space, life_size):
        """
        -- 显示生命值文字，画心形图片，返回坐标值
        :param bird_life: 生命值
        :param life: 生命值的surface对象
        :param life_space：生命值图片间隔
        :param life_size：生命值图片的尺寸
        :return: life_x, life_y: 返回生命值图片最后的坐标，lostBird()使用
        """
        life_surf, life_rect = self.textObject(self.level_font, self.life_text, self.level_font_color,
                                               (self.life_text_pos[0], self.life_text_pos[1]), 'bottomright')
        self.screen.blit(life_surf, life_rect)       # 显示生命值文字
        life_x = self.life_text_pos[0] + life_space   # 获取生命值图片x值
        life_y = self.life_text_pos[1] - life_size    # 获取生命值图片y值
        for l in range(bird_life-1):      # 用遍历画生命值图片
            self.screen.blit(life, (life_x, life_y))
            life_x = life_x + life_size + life_space
        return life_x, life_y

    def levelText(self, level_text):
        """
        -- 显示关卡信息
        :param level_text: 关卡信息
        :return: None
        """
        level_surf, level_rect = self.textObject(self.level_font, level_text, self.level_font_color,
                                                 (self.level_text_pos[0], self.level_text_pos[1]), 'bottomright')
        self.screen.blit(level_surf, level_rect)

    def pause(self, pause):
        """
        -- 显示暂停信息，关闭窗口时退出，按下空格键返回游戏
        :param pause: bool,True or False
        :return: None
        """
        pause_surf, pause_rect = self.textObject(self.info_font, self.pause_text, self.info_font_color,
                                                 ((self.window_w / 2), (self.window_h / 2)), 'center')
        self.screen.blit(pause_surf, pause_rect)

        pygame.display.update()  # 刷新画面
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
            self.clock.tick(self.fps)
        return
