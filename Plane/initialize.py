#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame


class Init(object):
    def __init__(self):
        pass

    SCREEN_RECT = pygame.Rect(0, 0, 512, 600)   # 用一个常量来存储屏幕的位置和大小,常量用全大写表示
    SCREEN_CENTER = [SCREEN_RECT.width/2, SCREEN_RECT.height/2]

    CREATE_ENEMY_EVENT = pygame.USEREVENT       # 敌机事件定时器常量值
    OWN_FIRE_EVENT = pygame.USEREVENT + 1       # 发射子弹定时器常量值
    BONUS_ENEMY_EVENT = pygame.USEREVENT + 2    # 加分敌机的定时器常量值
    STAR_ENEMY_EVENT = pygame.USEREVENT + 3     # 星星敌机的定时器常量值

    ENEMY_TIMER = 600                           # 敌机出现的时间频率
    BULLET_TIMER = 400                          # 子弹出现的时间频率
    BONUS_TIMER = 5000                          # 加分敌机出现的时间频率
    START_TIMER = 20000                         # 星星敌机出现的时间频率
    LIFE_NUMS = 5                               # 生命值
    MOVE_SPEED = 4                              # 已方飞机移动速度
    STAR_ENEMY_LIFE = 6                         # 打掉星星敌机需要的子弹

    BACKGROUND = r'.\images\background.png'
    GAME_OVER = r'.\images\gameover.png'
    OWN_IMAGE = r'.\images\own.png'
    OWN_DOWN_IMAGE = r'.\images\own_died.png'
    ENEMY_RED_IMAGE = r'.\images\enemy_red.png'
    ENEMY_BLUE_IMAGE = r'.\images\enemy_blue.png'
    ENEMY_DOWN_IMAGE = r'.\images\enemy_down.png'
    BULLET_IMAGE = r'.\images\bullet.png'
    LIFE_IMAGE = r'.\images\life.png'
    GOLD_COIN_IMAGE = r'.\images\bonus.png'
    STAR_IMAGE = r'.\images\star.png'
    READY_IMAGE = r'.\images\ready.png'

    SYS_FONT = r'.\fonts\BOLDER.ttf'

    FPS = 60            # 屏幕刷新频率
