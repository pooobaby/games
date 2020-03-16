#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import datetime
from setting import *

def save_record(game_score):
    """ 将最高分和游戏记录保存到文件中 """
    now_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M')
    score = game_score
    record = '{},{}'.format(now_time, score)
    with open(HI_SCORE_FILE, 'a+', encoding='utf-8') as f:
        f.write(record)
