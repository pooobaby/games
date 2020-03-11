#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import os
import random
import pygame
from pygame.locals import *


# noinspection PyPep8Naming,PyUnusedLocal
class BaseInit(object):
    def __init__(self):
        # 游戏主窗口运行的基本信息
        self.window_w, self.window_h = 800, 600         # 窗体尺寸大小
        self.window_title = 'Ping Ping Bird'            # 设定窗口标题
        self.bg_color = (255, 255, 255)                 # 设定背景颜色
        self.window_icon = pygame.image.load(r'images\logo.png')        # 设定图标文件
        self.fps = 60                       # 帧率，即每秒刷新多少次
        self.clock = pygame.time.Clock()    # 创建时钟对象 (可以控制游戏循环频率)

        self.screen = self.setWindow()      # 建立一个窗口对象

    pygame.init()                       # 初始化pygame，为使用硬件做准备

    # 设定背景音乐的音效基本信息
    pygame.mixer.init()                 # 初始化音乐播放器
    pygame.mixer.music.load(r'sounds\background.mp3')
    pygame.mixer.music.play(-1, 0.0)

    bd_level_01 = pygame.image.load(r'images\level_01.jpg')    # 第1关背景图片
    bd_level_02 = pygame.image.load(r'images\level_02.jpg')    # 第2关背景图片
    bd_level_03 = pygame.image.load(r'images\level_03.jpg')    # 第2关背景图片

    # 设定菜单页面中的基本信息
    menu_font_file = r'fonts\BOLDER.ttf'               # 菜单中的字体
    menu_font_size = 36                                # 菜单字体大小
    menu_text_color = ((255, 255, 255), (0, 0, 0))     # 菜单字体颜色
    menu_text_pos = ((100, 700), 480)                  # 菜单字体显示的位置
    menu_text = ['about', 'load', 'START', 'config', 'quit']                # 菜单中的文字内容
    menu_font = pygame.font.Font(menu_font_file, menu_font_size)            # 定义菜单字体对象

    menu_bd = pygame.image.load(r'images\menu_bd.jpg')              # 菜单背景图片
    menu_mouse_focus = pygame.image.load(r'images\mouse_focus.png')    # 菜单中鼠标正常图片
    menu_mouse_press = pygame.image.load(r'images\mouse_press.png')    # 菜单中鼠标按下时的图片

    # 设定载入页面的基本信息
    loading_bird_v = 150                             # 飞行小鸟的速度
    loading_bird_pos = ((150, 200), (600, 200))      # 飞行小鸟的位置

    loading_text = 'loading game...'            # 载入文字内容
    loading_text_color = (255, 255, 255)        # 载入文字颜色
    loading_text_pos = (400, 280)               # 载入文字显示位置

    loading_bd = pygame.image.load(r'images\loading_bd.jpg')       # 页面背景图片
    loading_bird_img = pygame.image.load(r'images\loading_bird.png')     # 载入时飞行小鸟的图片

    # 设定失败页面的基本信息
    losing_bd = pygame.image.load(r'images\losing_bd.jpg')       # 页面背景图片
    losing_text = 'Play again'  # 失败文字内容
    losing_text_color = [(255, 255, 255), (255, 240, 1)]  # 失败文字颜色序列
    losing_text_pos = (400, 450)  # 失败文字显示位置

    # 设定字体基本信息
    level_font_file = r'fonts\Juicebox.otf'   # 关卡中使用的字体
    # 关卡字体
    level_font_size = 18                # 关卡字体尺寸
    level_font_color = (255, 255, 255)  # 关卡文字的颜色
    level_font = pygame.font.Font(level_font_file, level_font_size)  # 关卡字体对象
    # 关卡提示信息
    info_font_size = 36                 # 关卡提示信息字体大小
    info_font_color = (255, 255, 255)   # 关卡提示信息字体颜色
    info_font = pygame.font.Font(level_font_file, info_font_size)         # 提示信息字体对象
    # 文字显示位置
    score_text_pos = (20, 580)      # 设定得分显示的位置
    level_text_pos = (780, 580)     # 设定关卡文字显示的位置
    life_text_pos = (150, 580)      # 设定生命值文字显示的位置
    # 文字内容
    score_text = 'score: '     # 设定得分的文字内容
    life_text = 'life: '       # 设定生命值的文字内容
    lost_one_text = 'You lost a bird...'                # 设定失去一个小鸟时的文字
    pause_text = 'Press SPACE key to continue...'   # 设定暂停信息的文字

    # 设定游戏元素基本信息
    bird_1 = pygame.image.load(r'images\bird_1.png')        # 小鸟1图片
    bird_2 = pygame.image.load(r'images\bird_2.png')        # 小鸟2图片
    plank_1 = pygame.image.load(r'images\plank_1.png')      # 木板1图片
    star_1 = pygame.image.load(r'images\star_1.png')        # 星星图片
    life_1 = pygame.image.load(r'images\life_1.png')        # 生命值图片
    cloud_1 = pygame.image.load(r'images\cloud_1.png')      # 乌云图片
    plank_2 = pygame.image.load(r'images\plank_2.png')      # 木板2图片-长
    plank_3 = pygame.image.load(r'images\plank_3.png')      # 木板3图片-短

    short = pygame.image.load(r'images\plank_short.png')    # 使木板变短的图片，TNT
    long = pygame.image.load(r'images\plank_long.png')      # 使木板变长的图片，西红柿
    blank_1 = pygame.image.load(r'images\blank_1.png')      # 空图片

    bird_1_size = 30            # 小鸟1的尺寸
    bird_2_size = 30            # 小鸟2的尺寸
    life_1_size = 20            # 生命值的尺寸
    cloud_1_size = 50           # 乌云的尺寸
    plank_1_size = [120, 10]    # 木板1尺寸
    plank_2_size = [240, 10]    # 木板2尺寸-长
    plank_3_size = [60, 10]     # 木板3尺寸-短
    short_size = 20             # 能使木板变短的TNT尺寸
    long_size = 50              # 能使木板变长的西红柿尺寸

    plank_1_y = 480             # 木板显示的y值
    bird_life = 5               # 小鸟的生命值
    bird_1_v = 200              # 小鸟的初始速度
    long_v = 400                # 能使木板变长的西红柿速度
    short_v = 400               # 能使木板变短的TNT速度
    life_1_space = 5            # 生命值的间隔
    bird_1_speed = {0: 1, 3: 1.2, 6: 1.4, 10: 1.6, 20: 2, 25: 2.2}    # 小鸟的速度档次

    # 设定游戏过关的阈值
    level_01 = 30                # 第1关得分
    level_02 = 35                # 第2关得分
    level_03 = 40                # 第3关得分
    long_short_times = 20        # 长短道具出现的次数
    long_short_score = random.sample(range(1, level_03), long_short_times)     # 生成长短道具出现的列表

    lost_one_size = 15          # -1 的尺寸
    lost_one = pygame.image.load(r'images\-1.png')          # -1 图片

    def setWindow(self):
        """
        -- 创建一个窗口对象
        :return:Surface object: Pygame中用于表示图像的对象
        """
        screen = pygame.display.set_mode((self.window_w, self.window_h), FULLSCREEN)    # 创建窗口对象
        # screen = pygame.display.set_mode((self.window_w, self.window_h))    # 创建窗口对象
        pygame.mouse.set_visible(False)                                     # 隐藏鼠标
        pygame.display.set_caption(self.window_title)                       # 窗口标题
        pygame.display.set_icon(self.window_icon)                           # 窗口图标
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (600, 200)           # 设置窗口出现的位置
        return screen

    @staticmethod
    def textObject(font, text, colors, position, angle):
        """
        -- 生成文字对象
        :param font: 定义的字体对象
        :param text: 文字信息
        :param colors: 字体颜色
        :param position: 字体位置
        :param angle: 显示字体时定位于哪里(center, bottomleft....)
        :return: textSurface: Surface(生成的文字对象); text_rect: Surface(文字转换成矩形图像的对象)
        """
        text_surface = font.render(text, True, colors)
        text_rect = text_surface.get_rect()
        exec('text_rect.{} = {}'.format(angle, position))
        return text_surface, text_rect
