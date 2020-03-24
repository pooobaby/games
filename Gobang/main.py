#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from drawing import Display
from status import State
from setup import *


def main():
    """ 主程序 """
    state = State()
    display = Display(state.screen)
    display.drawChessBoard()
    display.drawRightSide()
    while True:
        checkEvents(state, display)
        state.clock.tick(FPS)
        pygame.display.update()


# noinspection PyPep8Naming
def checkEvents(state, display):
    """ 检查事件程序 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                state.reStart()
                display.drawChessBoard()
                display.drawRightSide()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and state.startGame():
                human_piece = state.humanPiece()
                if human_piece:
                    display.drawMain(human_piece[0], human_piece[1], human_piece[2], human_piece[3], human_piece[4])
                    if not human_piece[3]:
                        return
                    pygame.display.flip()
                    ai_piece = state.aiPiece()
                    display.drawMain(ai_piece[0], ai_piece[1], ai_piece[2], ai_piece[3], ai_piece[4])
                    pygame.display.flip()


if __name__ == '__main__':
    main()
