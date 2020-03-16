#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from setting import *


class GameResource(object):
    def __init__(self):
        self.img_path = 'images/'
        self.newgame_img = None
        self.pausing_img = None
        self.continue_img = None
        self.gameover_img = None
        self.snail_img = None
        self.bg_img = None
        self.switch_img = None

    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(GAME_NEWGAME_FILE).convert_alpha()
        return self.newgame_img

    def load_pausing_img(self):
        if not self.pausing_img:
            self.pausing_img = pygame.image.load(GAME_PAUSING_FILE).convert_alpha()
        return self.pausing_img

    def load_continue_img(self):
        if not self.continue_img:
            self.continue_img = pygame.image.load(GAME_CONTINUE_FILE).convert_alpha()
        return self.continue_img

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(GAME_OVER_FILE).convert_alpha()
        return self.gameover_img

    def load_bg_img(self, difficulty):
        self.bg_img = pygame.image.load(BACKGROUND_LIST[0])
        for n, value in enumerate(BACKGROUND_LIST):
            if (difficulty - 1) % len(BACKGROUND_LIST) == n:
                self.bg_img = pygame.image.load(value)
        return self.bg_img

    def load_snail_img(self):
        if not self.snail_img:
            self.snail_img = pygame.image.load(SNAIL_FILE).convert_alpha()
        return self.snail_img

    def load_switch_img(self, switch_state):
        if not self.switch_img:
            self.switch_img = pygame.image.load(switch_state).convert_alpha()
        return self.switch_img
