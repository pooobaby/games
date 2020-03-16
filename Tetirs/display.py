#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

from setting import *
import pygame


class GameDisplay(object):
    @staticmethod
    def draw_cell(screen, row, column, color):
        """ 第row行column列的格子里填充color颜色。一种方块对应一种颜色 """
        cell_position = (column * CELL_WIDTH + GAME_AREA_LEFT, row * CELL_WIDTH + GAME_AREA_TOP)
        GameDisplay.draw_cell_rect(screen, cell_position, color)

    @staticmethod
    def draw_cell_rect(screen, left_top_anchor, color):
        left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(left_top_anchor, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_window(screen, game_state, game_resource):
        """ 绘制游戏窗口 """
        GameDisplay.draw_wall(game_state.wall)
        GameDisplay.draw_score(screen, game_state.game_score)
        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_game_over(screen, game_resource)
            GameDisplay.draw_start_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen, game_resource)
            GameDisplay.draw_continue_prompt(screen, game_resource)
        GameDisplay.draw_next_piece(screen, game_state.next_piece)
        GameDisplay.draw_difficulty_level(screen, game_state.difficulty)
        for n, record in enumerate(game_state.record_list[-10:]):
            y = RECORD_TEXT_Y + n * RECORD_INFO_SIZE * 1.5
            GameDisplay.draw_game_record(screen, record, y)
        GameDisplay.draw_lines(screen, game_state.lines)
        GameDisplay.draw_hi_score(screen, game_state.hi_score)
        GameDisplay.draw_switch(screen, game_resource, game_state.switch_state)
        GameDisplay.draw_snail(screen, game_resource, game_state.snail_x)

    @staticmethod
    def draw_snail(screen, game_resource, x):
        """ 绘制小蜗牛 """
        surf = game_resource.load_snail_img()
        rect = surf.get_rect()
        rect.bottomright = (x, SNAIL_Y)
        screen.blit(surf, rect)

    @staticmethod
    def draw_switch(screen, game_resource, switch_state):
        """ 绘制控制开关 """
        surf = game_resource.load_switch_img(switch_state)
        rect = surf.get_rect()
        rect.bottomright = SWITCH_POS
        screen.blit(surf, rect)

    @staticmethod
    def draw_wall(game_wall):
        """ 绘制墙体 """
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, r, c, PIECE_COLORS[game_wall.area[r][c]])

    @staticmethod
    def draw_difficulty_level(screen, level):
        """ 绘制游戏难度级别 """
        level_label_font = pygame.font.Font(GAME_INFO_FONT, GAME_INFO_SIZE)
        level_label_surface = level_label_font.render(u'level: ' + str(level), True, GAME_INFO_COLOR)
        level_label_position = (NEXT_PIECE_X, GAME_INFO_Y)
        screen.blit(level_label_surface, level_label_position)

    @staticmethod
    def draw_lines(screen, lines):
        """ 绘制游戏消除行数 """
        score_label_font = pygame.font.Font(GAME_INFO_FONT, GAME_INFO_SIZE)
        score_label_surface = score_label_font.render(u'lines: ' + str(lines), True, GAME_INFO_COLOR)
        score_label_position = (NEXT_PIECE_X, GAME_INFO_Y+25)
        screen.blit(score_label_surface, score_label_position)

    @staticmethod
    def draw_score(screen, score):
        """ 绘制游戏得分 """
        score_label_font = pygame.font.Font(GAME_INFO_FONT, GAME_INFO_SIZE)
        score_label_surface = score_label_font.render(u'score: ' + str(score), True, GAME_INFO_COLOR)
        score_label_position = (NEXT_PIECE_X, GAME_INFO_Y+50)
        screen.blit(score_label_surface, score_label_position)

    @staticmethod
    def draw_hi_score(screen, hi_score):
        """ 绘制游戏最高分 """
        score_label_font = pygame.font.Font(HI_SCORE_FONT, HI_SCORE_SIZE)
        score_label_surface = score_label_font.render(str(hi_score), True, HI_SCORE_COLOR)
        score_label_rect = score_label_surface.get_rect()
        score_label_rect.center = (NEXT_PIECE_X+55, HI_SCORE_TEXT_Y)
        screen.blit(score_label_surface, score_label_rect)

    @staticmethod
    def draw_game_record(screen, game_record, y):
        """ 绘制游戏记录 """
        score_label_font = pygame.font.Font(RECORD_TEXT_FONT, RECORD_INFO_SIZE)
        score_label_surface = score_label_font.render(game_record, True, RECORD_TEXT_COLOR)
        score_label_position = (NEXT_PIECE_X, y)
        screen.blit(score_label_surface, score_label_position)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        """ 显示按F1游戏开始 """
        surf = game_resource.load_newgame_img()
        rect = game_resource.load_newgame_img().get_rect()
        rect.bottomleft = CONTROL_TEXT_POS
        screen.blit(surf, rect)

    @staticmethod
    def draw_continue_prompt(screen, game_resource):
        """ 显示按F2游戏继续 """
        surf = game_resource.load_continue_img()
        rect = game_resource.load_continue_img().get_rect()
        rect.bottomleft = CONTROL_TEXT_POS
        screen.blit(surf, rect)

    @staticmethod
    def draw_game_over(screen, game_resource):
        """ 显示gameover """
        surf = game_resource.load_gameover_img()
        rect = game_resource.load_gameover_img().get_rect()
        rect.center = ((SCREEN_WIDTH+GAME_AREA_WIDTH)/2, SCREEN_HEIGHT/2)
        screen.blit(surf, rect)

    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        """ 显示pausing """
        surf = game_resource.load_pausing_img()
        rect = game_resource.load_pausing_img().get_rect()
        rect.center = ((SCREEN_WIDTH+GAME_AREA_WIDTH)/2, SCREEN_HEIGHT/2)
        screen.blit(surf, rect)

    @staticmethod
    def draw_next_piece(screen, next_piece):
        """ 绘制下一方块 """
        start_x = NEXT_PIECE_X
        start_y = NEXT_PIECE_Y
        if next_piece:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []    # 主要绘制的单元格
            shape_template = PIECES[next_piece.shape]
            shape_turn = shape_template[next_piece.turn_times]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == 'O':
                        cells.append((c,  r, PIECE_COLORS[next_piece.shape]))

            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            for cell in cells:
                color = cell[2]
                left_top = (start_x + (cell[0] - min_c) * CELL_WIDTH, start_y + (cell[1] - min_r) * CELL_WIDTH)
                GameDisplay.draw_cell_rect(screen, left_top, color)
