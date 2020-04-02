#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020


ICON_KIND = 12
ROW = 8
COL = 12
ICON_SIZE = 50
L_BORDER, B_BORDER, R_BORDER = 0, 0, 0
T_BORDER = 10
WIN_W = L_BORDER + R_BORDER + (COL+2) * ICON_SIZE
WIN_H = T_BORDER + B_BORDER + (ROW+2) * ICON_SIZE

FPS = 10
EMPTY = -1
BG_COLOR = (240, 240, 244)
TAG_COLOR = (255, 33, 33)
LINE_COLOR = (255, 0 ,0)
CELL_COLOR = (187, 205, 197)

ICONS_IMG = r'.\images\icon_'
TEXT_FONT = r'.\fonts\arial.ttf'
LOGO_FILE = r'.\images\logo.ico'

WIN_TEXT_SIZE = 24
INFO_TEXT_SIZE = 16
TEXT_COLOR = (0, 0, 0)