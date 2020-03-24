#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from setup import *


# noinspection PyPep8Naming
class Display(object):
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.black = pygame.image.load(BLACK_IMG)
        self.white = pygame.image.load(WHITE_IMG)
        self.black_small = pygame.image.load(BLACK_SMALL_IMG)
        self.white_small = pygame.image.load(WHITE_SMALL_IMG)
        self.restart_surf = pygame.image.load(RESTART_IMG)

    def drawMain(self, cur_pos, turn, result_text, starting, step_list):
        """ 主显示函数 """
        piece_surf = self.white if turn == 0 else self.black
        self.drawPiece(cur_pos, piece_surf)
        self.drawStep(step_list)
        self.drawResult(result_text)
        if not starting:
            self.drawRestart(self.restart_surf)
        else:
            if turn == 0:
                next_text = 'Next Black'
            else:
                next_text = 'Next White'
            self.drawNext(next_text)

    def drawStep(self, step_list):
        """ 显示落子记录 """
        pygame.draw.rect(self.screen, BG_COLOR,
                         (WINDOW_W-RIGHT_W+15, RIGHT_SIDE_CENTER_LINE_Y+10,
                          RIGHT_W-15, WINDOW_H-B_BORDER-RIGHT_SIDE_CENTER_LINE_Y-RIGHT_SIDE_BOTTOM_BLOCK_H), 0)
        for n, value in enumerate(step_list[-10:]):
            text = '{:03d}: {}   X={:02d}  Y={:02d}'.format(value[0], value[1], value[2][0], value[2][1])
            self.drawText(text, RIGHT_SIDE_STEP_TEXT_FONT, RIGHT_SIDE_STEP_TEXT_SIZE, RIGHT_SIDE_STEP_TEXT_COLOR,
                          WINDOW_W-RIGHT_W+15, RIGHT_SIDE_CENTER_LINE_Y+10+n*18, 'topleft')

    def drawNext(self, next_text):
        """ 显示下一步的内容 """
        pygame.draw.rect(self.screen, RIGHT_SIDE_COLOR,
                         (WINDOW_W-RIGHT_W, WINDOW_H-B_BORDER-RIGHT_SIDE_BOTTOM_BLOCK_H,
                          RIGHT_SIDE_BOTTOM_BLOCK_W, RIGHT_SIDE_BOTTOM_BLOCK_H), 0)
        self.drawText(next_text, RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_BOTTOM_TEXT_SIZE, RIGHT_SIDE_TEXT_COLOR,
                      WINDOW_W - R_BORDER - RIGHT_SIDE_BOTTOM_BLOCK_W / 2,
                      WINDOW_H - B_BORDER - RIGHT_SIDE_BOTTOM_BLOCK_H / 2, 'center')

    def drawRestart(self, restart_surf):
        """ 显示按F1重新游戏 """
        restart_rect = restart_surf.get_rect()
        restart_rect.center = (L_BORDER+COL*SPACE/2, WINDOW_H/2)
        self.screen.blit(restart_surf, restart_rect)

    def drawPiece(self, cur_pos, piece_surf):
        """ 画棋子 """
        piece_rect = piece_surf.get_rect()
        piece_rect.center = (cur_pos[0], cur_pos[1])
        self.screen.blit(piece_surf, piece_rect)

    def drawRightSide(self):
        """ 画右边栏的屏幕 """
        pygame.draw.line(self.screen, RIGHT_SIDE_COLOR, (WINDOW_W-RIGHT_W+5, T_BORDER),
                         (WINDOW_W-RIGHT_W+5, WINDOW_H-B_BORDER))
        pygame.draw.line(self.screen, RIGHT_SIDE_COLOR, (WINDOW_W-RIGHT_W, T_BORDER+RIGHT_SIDE_BLOCK_H),
                         (WINDOW_W-R_BORDER, T_BORDER+RIGHT_SIDE_BLOCK_H))
        pygame.draw.line(self.screen, RIGHT_SIDE_COLOR, (WINDOW_W-RIGHT_W, RIGHT_SIDE_CENTER_LINE_Y),
                         (WINDOW_W-R_BORDER, RIGHT_SIDE_CENTER_LINE_Y))
        pygame.draw.rect(self.screen, RIGHT_SIDE_COLOR,
                         (WINDOW_W-RIGHT_W, T_BORDER, RIGHT_SIDE_BLOCK_W, RIGHT_SIDE_BLOCK_H), 0)
        pygame.draw.rect(self.screen, RIGHT_SIDE_COLOR,
                         (WINDOW_W-RIGHT_W, RIGHT_SIDE_CENTER_LINE_Y-RIGHT_SIDE_BLOCK_H,
                          RIGHT_SIDE_BLOCK_W, RIGHT_SIDE_BLOCK_H), 0)
        pygame.draw.rect(self.screen, RIGHT_SIDE_COLOR,
                         (WINDOW_W-RIGHT_W, WINDOW_H-B_BORDER-RIGHT_SIDE_BOTTOM_BLOCK_H,
                          RIGHT_SIDE_BOTTOM_BLOCK_W, RIGHT_SIDE_BOTTOM_BLOCK_H), 0)
        self.drawText('Players', RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_TEXT_SIZE, RIGHT_SIDE_TEXT_COLOR,
                      WINDOW_W-RIGHT_W+5, T_BORDER+RIGHT_SIDE_BLOCK_H, 'bottomleft')
        self.drawText('Human', RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_TEXT_SIZE, RIGHT_SIDE_STEP_TEXT_COLOR,
                      WINDOW_W-RIGHT_W+35, T_BORDER+RIGHT_SIDE_BLOCK_H+7, 'topleft')
        self.drawText('AI', RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_TEXT_SIZE, RIGHT_SIDE_STEP_TEXT_COLOR,
                      WINDOW_W-RIGHT_W+35, T_BORDER+RIGHT_SIDE_BLOCK_H+27, 'topleft')
        self.drawText('Step List', RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_TEXT_SIZE, RIGHT_SIDE_TEXT_COLOR,
                      WINDOW_W-RIGHT_W+5, RIGHT_SIDE_CENTER_LINE_Y, 'bottomleft')
        self.drawText('Click Start', RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_BOTTOM_TEXT_SIZE, RIGHT_SIDE_TEXT_COLOR,
                      WINDOW_W - R_BORDER - RIGHT_SIDE_BOTTOM_BLOCK_W / 2,
                      WINDOW_H - B_BORDER - RIGHT_SIDE_BOTTOM_BLOCK_H / 2, 'center')
        self.screen.blit(self.black_small, (WINDOW_W-RIGHT_W+15, T_BORDER+RIGHT_SIDE_BLOCK_H+10))
        self.screen.blit(self.white_small, (WINDOW_W-RIGHT_W+15, T_BORDER+RIGHT_SIDE_BLOCK_H+30))

    def drawChessBoard(self):
        """ 画棋盘，分别画出横线，竖线，点，横轴数字，纵轴数字 """
        self.screen.fill((128, 128, 128))
        for i in range(ROW):
            pygame.draw.line(self.screen, LINE_COLOR, (L_BORDER, T_BORDER+i*SPACE),
                             (L_BORDER+SPACE*(COL-1), T_BORDER+i*SPACE))
        for j in range(COL):
            pygame.draw.line(self.screen, LINE_COLOR, (L_BORDER+j*SPACE, T_BORDER),
                             (L_BORDER+j*SPACE, T_BORDER+SPACE*(ROW-1)))
        for p in POINT_LIST:
            pos = (L_BORDER+p[0]*SPACE, T_BORDER+p[1]*SPACE)
            pygame.draw.circle(self.screen, LINE_COLOR, pos, POINT_R)
        for m in range(1, ROW):
            self.drawText(str(m), AXIS_TEXT_FONT, AXIS_TEXT_SIZE, AXIS_TEXT_COLOR,
                          L_BORDER-AXIS_TEXT_SIZE/2, T_BORDER+AXIS_TEXT_SIZE/2+m*SPACE, 'bottomright')
        for n in range(0, COL):
            self.drawText(X_AXIS_LIST[n], AXIS_TEXT_FONT, AXIS_TEXT_SIZE, AXIS_TEXT_COLOR,
                          L_BORDER+n*SPACE, T_BORDER-int(AXIS_TEXT_SIZE/1.5), 'center')

    def drawText(self, text, font, size, color, x, y, site):
        """ 在窗口中指定位置显示文字 """
        text_font = pygame.font.Font(font, size)
        text_surf = text_font.render(text, True, color)
        text_rect = text_surf.get_rect()
        exec('text_rect.{}=({},{})'.format(site, x, y))
        self.screen.blit(text_surf, text_rect)

    def drawResult(self, result_text):
        """ 显示结果文字 """
        pygame.draw.rect(self.screen, RIGHT_SIDE_COLOR,
                         (WINDOW_W-RIGHT_W, WINDOW_H-B_BORDER-RIGHT_SIDE_BOTTOM_BLOCK_H,
                          RIGHT_SIDE_BOTTOM_BLOCK_W, RIGHT_SIDE_BOTTOM_BLOCK_H), 0)
        self.drawText(result_text, RIGHT_SIDE_TEXT_FONT, RIGHT_SIDE_BOTTOM_TEXT_SIZE, RIGHT_SIDE_TEXT_COLOR,
                      WINDOW_W-R_BORDER-RIGHT_SIDE_BOTTOM_BLOCK_W/2,
                      WINDOW_H-B_BORDER-RIGHT_SIDE_BOTTOM_BLOCK_H/2, 'center')
