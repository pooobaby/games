#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020


BOARD = [[0, 0, 0, 0, 0, 0, 7, 0, 0],
         [6, 0, 0, 1, 0, 0, 0, 0, 0],
         [2, 9, 3, 0, 0, 0, 0, 4, 0],
         [0, 4, 1, 0, 8, 0, 0, 9, 0],
         [0, 0, 0, 0, 2, 4, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 9, 0, 0, 0, 0, 0, 0],
         [0, 0, 8, 0, 0, 0, 0, 0, 0],
         [0, 3, 0, 4, 0, 0, 0, 8, 0]]

ROW, COL = 9, 9
LEVEL = 0.3
BLOCK = 50
L_BORDER, R_BORDER, T_BORDER, B_BORDER = 20, 20, 20, 20
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
WIN_W = L_BORDER + BLOCK * ROW + R_BORDER
WIN_H = T_BORDER + BLOCK * COL + B_BORDER

FPS = 60


LOGO_IMG = r'.\images\logo.ico'