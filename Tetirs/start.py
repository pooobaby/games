#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import os
import sys
import pygame
from setting import *
from display import GameDisplay
from state import GameState
from resource import GameResource


# noinspection PyArgumentList
def main():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (200, 60)            # 设置窗口出现的位置
    logo = pygame.image.load(LOGO_IMG)  # 设置游戏窗口图标
    pygame.display.set_icon(logo)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     # 创建屏幕对象
    pygame.display.set_caption(WINDOW_TITLE)                            # 窗口标题
    pygame.key.set_repeat(100, 100)     # 一直按下某个键时，每过100毫秒就引发一个KEYDOWN事件????

    game_state = GameState(screen)      # 初始化游戏状态
    game_resource = GameResource()      #

    while True:
        if game_state.piece and game_state.piece.is_on_bottom:  # 方块触底的话
            game_state.touch_bottom()
        check_events(game_state)                 # 监视键盘和鼠标事件
        screen.blit(game_resource.load_bg_img(game_state.difficulty), (0, 0))        # 设定屏幕背景
        if game_state.piece:                                    # 绘制方块
            game_state.piece.paint()
        if game_state.stopped:                                  # 如果游戏结束
            if game_state.session_count > 0:                    # 玩的场次大于0
                score = game_state.game_score
                game_state.save_record(score, game_state.save_flag)                   # 保存游戏记录到文件中
        GameDisplay.draw_game_window(screen, game_state, game_resource)     # 绘制游戏区域网格线和墙体
        pygame.display.flip()       # 让最近绘制的屏幕可见


def check_events(game_state):
    """ 捕捉和处理键盘按键事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_down()


def on_key_down(event, game_state):
    if not game_state.paused and event.key == pygame.K_DOWN:
        # print("向下方向键被按下")
        if game_state.piece:
            game_state.piece.move_down()
    elif not game_state.paused and event.key == pygame.K_UP:
        # print("向上方向键被按下")
        if game_state.piece:
            game_state.piece.turn()
    elif not game_state.paused and event.key == pygame.K_RIGHT:
        # print("向右方向键被按下")
        if game_state.piece:
            game_state.piece.move_right()
    elif not game_state.paused and event.key == pygame.K_LEFT:
        # print("向左方向键被按下")
        if game_state.piece:
            game_state.piece.move_left()
    elif not game_state.paused and event.key == pygame.K_SPACE:
        if game_state.piece:
            game_state.piece.fall_down()
    elif event.key == pygame.K_F1 and game_state.stopped:
        game_state.start_game()
    elif event.key == pygame.K_F2 and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()
    elif event.key == pygame.K_F5:     # 按F5键强制重新开始游戏
        game_state.start_game()
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


if __name__ == '__main__':
    main()
