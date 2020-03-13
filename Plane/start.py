#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
import level_01
import os

def main():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300, 30)  # 设置窗口出现的位置
    plane = level_01.PlaneGame()
    plane.start()

if __name__ == '__main__':
    main()
