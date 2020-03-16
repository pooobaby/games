#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

SCREEN_WIDTH = 800      # 窗口宽度
SCREEN_HEIGHT = 600     # 窗口高度
WINDOW_TITLE = '俄罗斯方块'
CELL_WIDTH = 25         # 方块在20*10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
LINE_NUM = 20           # 游戏区域共20行
COLUMN_NUM = 10         # 游戏区域共10列
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM     # 游戏区域宽度（单位：像素）
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM      # 游戏区域高度
GAME_AREA_LEFT = 393            # 游戏区左侧的空白区的宽度
GAME_AREA_TOP = 66              # 游戏区顶部的空白区的宽度
EDGE_COLOR = (0, 0, 0)          # 游戏区单元格边界线的颜色。今后，网格线会被去除。
CELL_COLOR = (100, 100, 100)    # 单元格填充色。
BG_COLOR = (230, 230, 230)      # 窗口背景色

# 各种方块的姿态序列
# 首先是未翻转的姿态，接着是向右翻转90度的姿态。再翻转90度，将回到未翻转前的姿态。
S_SHAPE_TEMPLATE = [['.OO.', 'OO..', '....'], ['.O..', '.OO.', '..O.']]
Z_SHAPE_TEMPLATE = [['OO..', '.OO.', '....'], ['..O.', '.OO.', '.O..']]
I_SHAPE_TEMPLATE = [['.O..', '.O..', '.O..', '.O..'], ['....', 'OOOO', '....', '....']]
O_SHAPE_TEMPLATE = [['OO', 'OO']]
J_SHAPE_TEMPLATE = [['.O.', '.O.', 'OO.'], ['O..', 'OOO', '...'], ['OO.', 'O..', 'O..'], ['OOO', '..O', '...']]
L_SHAPE_TEMPLATE = [['O..', 'O..', 'OO.'], ['...', 'OOO', 'O..'], ['OO.', '.O.', '.O.'], ['..O', 'OOO', '...']]
T_SHAPE_TEMPLATE = [['.O.', 'OOO', '...'], ['.O.', '.OO', '.O.'], ['...', 'OOO', '.O.'], ['..O', '.OO', '..O']]

PIECES = {'S': S_SHAPE_TEMPLATE, 'Z': Z_SHAPE_TEMPLATE, 'J': J_SHAPE_TEMPLATE, 'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE, 'O': O_SHAPE_TEMPLATE, 'T': T_SHAPE_TEMPLATE}

PIECE_TYPES = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']

PIECE_COLORS = {'S': (220, 20, 60), 'Z': (154, 205, 50), 'J': (0, 128, 0), 'L': (0, 128, 128),
                'I': (210, 105, 30), 'O': (128, 128, 128), 'T': (143, 188, 139)}

WALL_BLANK_LABEL = '-'      # 墙体矩阵中表示无砖块
TIMER_INTERVAL = 1000       # 方块自动落下的等待时间初始值

EDGE_WIDTH = 5              # 游戏区域外框线宽度
MARGIN_WIDTH = 40           # 游戏区域外框线与其他窗口元素之间的间距

DIFFICULTY_LEVEL_INTERVAL = 1000     # 每过1000分，难度升1级
TIMER_DECREASE_VALUE = 100           # 难度每升1级，定时器加快100ms

NEXT_PIECE_X = 667                  # 下一块显示区的x坐标
NEXT_PIECE_Y = 61                   # 下一块显示区的y坐标
CONTROL_TEXT_POS = (50, 450)        # 游戏控制按键显示区的坐标

GAME_INFO_FONT = r'.\fonts\arial.ttf'       # 关卡和分数显示设置
GAME_INFO_SIZE = 20
GAME_INFO_COLOR = (208, 208, 208)           # 关卡和分数显示颜色
GAME_INFO_Y = 490                           # 关卡和分数显示区的y值

RECORD_TEXT_FONT = r'.\fonts\arial.ttf'     # 游戏记录显示设置
RECORD_INFO_SIZE = 12
RECORD_TEXT_Y = 260
RECORD_TEXT_COLOR = (134, 124, 127)

HI_SCORE_FONT = r'.\fonts\arial.ttf'        # 最高分显示设置
HI_SCORE_SIZE = 36
HI_SCORE_TEXT_Y = 200
HI_SCORE_COLOR = (208, 208, 208)

SNAIL_DISTANCE = 350                        # 蜗牛爬行的距离
SNAIL_Y = 564                               # 蜗牛显示y值
SWITCH_POS = (385, 564)                     # 控制杆显示坐标

BG_00_IMG = r'.\images\background_00.jpg'
BG_01_IMG = r'.\images\background_01.jpg'
BG_02_IMG = r'.\images\background_02.jpg'
BG_03_IMG = r'.\images\background_03.jpg'
BG_04_IMG = r'.\images\background_04.jpg'
BG_05_IMG = r'.\images\background_05.jpg'
BACKGROUND_LIST = [BG_00_IMG, BG_01_IMG, BG_02_IMG, BG_03_IMG, BG_04_IMG, BG_05_IMG]        # 背景图片显示列表

GAME_OVER_FILE = r'.\images\gameover.png'
GAME_PAUSING_FILE = r'.\images\pausing.png'
GAME_CONTINUE_FILE = r'.\images\continue.png'
GAME_NEWGAME_FILE = r'.\images\newgame.png'
SNAIL_FILE = r'.\images\snail.png'
SWITCH_OPEN_FILE = r'.\images\switch_open.png'
SWITCH_CLOSE_FILE = r'.\images\switch_close.png'

LOGO_IMG = r'.\images\logo.ico'             # 图标文件
HI_SCORE_FILE = r'Hi-score.txt'             # 游戏记录文件
