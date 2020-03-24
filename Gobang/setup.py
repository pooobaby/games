#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020


ROW = 15
COL = 15
DX = [1, 1, 0, -1, -1, -1, 0, 1]
DY = [0, 1, 1, 1, 0, -1, -1, -1]

SPACE = 30
L_BORDER = 50
R_BORDER = 30
T_BORDER = 50
B_BORDER = 30
RIGHT_W = 150

FPS = 60
WINDOW_W = L_BORDER + SPACE * (COL-1) + R_BORDER + RIGHT_W
WINDOW_H = T_BORDER + SPACE * (ROW-1) + B_BORDER
BG_COLOR = (128, 128, 128)
LINE_COLOR = (22, 24, 35)

RIGHT_SIDE_TEXT_FONT = r'.\fonts\msyh.ttc'
RIGHT_SIDE_STEP_TEXT_FONT = r'.\fonts\arial.ttf'
RIGHT_SIDE_TEXT_COLOR = (240, 252, 255)
RIGHT_SIDE_TEXT_SIZE = 12
RIGHT_SIDE_STEP_TEXT_SIZE = 12
RIGHT_SIDE_STEP_TEXT_COLOR = (66, 76, 80)
RIGHT_SIDE_BOTTOM_TEXT_SIZE = 20

RIGHT_SIDE_COLOR = (66, 76, 80)
RIGHT_SIDE_CENTER_LINE_Y = T_BORDER + 180
RIGHT_SIDE_BLOCK_H = 20
RIGHT_SIDE_BLOCK_W = 80

RIGHT_SIDE_BOTTOM_BLOCK_H = 40
RIGHT_SIDE_BOTTOM_BLOCK_W = RIGHT_W - R_BORDER


POINT_LIST = [(3, 3), (3, 7), (3, 11), (7, 3), (7, 7), (7, 11), (11, 3), (11, 7), (11, 11)]
POINT_R = 3

PIECE_R = 10
PIECE_NEAR = 10
PIECE_BLACK_COLOR = (0, 0, 0)
PIECE_WHITE_COLOR = (255, 255, 255)

X_AXIS_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
AXIS_TEXT_FONT = r'.\fonts\msyh.ttc'
AXIS_TEXT_COLOR = (0, 0, 0)
AXIS_TEXT_SIZE = 10

RESULT_TEXT_COLOR = (0, 0, 0)

LOGO_IMG = r'.\images\logo.ico'
BLACK_IMG = r'.\images\black.png'
WHITE_IMG = r'.\images\white.png'
BLACK_SMALL_IMG = r'.\images\black_small.png'
WHITE_SMALL_IMG = r'.\images\white_small.png'
RESTART_IMG = r'.\images\restart.png'
