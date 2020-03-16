#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import random
from setting import *
from piece import Piece
from wall import GameWall
import pygame
import time
import datetime


class GameState(object):
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)            # 建立一个空的墙
        self.piece = None                       # 当前块和下一块都为None
        self.next_piece = None
        self.timer_interval = TIMER_INTERVAL    # 方块自动落下的等待时间初始值
        self.game_score = 0                     # 得分
        self.stopped = True                     # 游戏结束标志
        self.paused = False                     # 游戏暂停标志
        self.session_count = 0                  # 玩的场次
        self.difficulty = 1                     # 游戏初始难度
        self.save_flag = True                   # 保存游戏的标志
        self.record_list, self.hi_score = self.load_record()    # 载入游戏记录
        self.score_interval = DIFFICULTY_LEVEL_INTERVAL         # 过关需要达到的分数值，初始化
        self.lines = 0                          # 消除的行数
        self.snail_x = 0                        # 蜗牛的x值
        self.switch_state = SWITCH_OPEN_FILE    # 控制杆状态

    @staticmethod
    def set_timer(timer_interval):
        """ 设置游戏定时器 """
        pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    @staticmethod
    def stop_timer():
        """ 游戏停止时，清除定时器 """
        pygame.time.set_timer(pygame.USEREVENT, 0)      # 传入0表示清除定时器

    def add_score(self, score, line):
        """ 将eliminate_lines()生成的分数累加，按幂次增加或减少过关分值和掉块频率 """
        level_interval = int(DIFFICULTY_LEVEL_INTERVAL * 1.1 ** (self.difficulty-1))    # 过关需要增加的分数
        timer_interval = int(TIMER_DECREASE_VALUE * 0.9 ** (self.difficulty-1))         # 过关后改变的掉块频率
        self.lines += line                              # 行数增加
        self.snail_x += int(SNAIL_DISTANCE*score/level_interval)  # 改变小蜗牛爬行的坐标
        self.game_score += score                        # 总分增加
        if self.game_score >= self.score_interval:      # 如果超过过关需要达到的分数值，过关
            self.difficulty += 1                        # 难度(关卡)+1
            self.timer_interval -= timer_interval       # 掉块频率减少
            self.score_interval += level_interval       # 重新改变下次过关需要的分值
            pygame.time.set_timer(pygame.USEREVENT, self.timer_interval)
            self.snail_x = 0                            # 蜗牛坐标回0
            self.switch_state = SWITCH_OPEN_FILE        # 控制杆状态改变

    def start_game(self):
        """ 每次开始游戏时，对基本参数初始化 """
        self.stopped = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.piece = self.new_piece()       # 生成第一个方块。此时self.piece=None, self.next_piece引用方块对象。
        self.piece = self.new_piece()       # 生成第二个方块，此时self.piece引用方块对象。
        self.difficulty = 1
        self.session_count += 1
        self.wall.clear()
        self.game_score = 0
        self.paused = False
        self.save_flag = True
        self.record_list, self.hi_score = self.load_record()
        self.score_interval = DIFFICULTY_LEVEL_INTERVAL  # 过关需要达到的分数值，初始化
        self.lines = 0                                      # 消除的行数
        self.switch_state = SWITCH_CLOSE_FILE
        self.snail_x = 0
        random.seed(int(time.time()))       # 每次游戏，使用不同的随机数序列

    def pause_game(self):
        self.stop_timer()
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    def touch_bottom(self):
        self.wall.add_to_wall(self.piece)
        score, eliminated_num = self.wall.eliminate_lines()
        self.add_score(score, eliminated_num)
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                self.stopped = True
                break
        if not self.stopped:
            self.piece = self.new_piece()
            if self.piece.hit_wall():
                self.stopped = True
        if self.stopped:
            self.stop_timer()

    def new_piece(self):
        self.piece = self.next_piece
        self.next_piece = Piece(random.choice(PIECE_TYPES), self.screen, self.wall)
        return self.piece

    @staticmethod
    def load_record():
        """ 从文件中load最高分和游戏记录 """
        record_list, score_list = [], []
        with open(HI_SCORE_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for l, line in enumerate(lines):
            line = line.replace('\n', '')
            game_date = line.split(',')[0]
            game_score = int(line.split(',')[1])
            score_list.append(game_score)
            record_list.append('{}: {}'.format(game_date, game_score))
        hi_score = max(score_list)
        return record_list, hi_score

    def save_record(self, score, save_flag):
        """ 将最高分和游戏记录保存到文件中 """
        if save_flag:           # 如果save_flag为True，保存记录到文件中
            now_time = datetime.datetime.now().strftime('%m/%d %H:%M')
            record = '{},{}\n'.format(now_time, score)
            with open(HI_SCORE_FILE, 'a+', encoding='utf-8') as f:
                f.write(record)
            self.save_flag = False      # save_flag变为False，直到下一次游戏开始再变为True
