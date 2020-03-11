#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import pygame
from initialize import BaseInit
import levels


# noinspection PyPep8Naming
class GameMenu(BaseInit):
    def __init__(self):
        super().__init__()

    def showing(self):
        mouse_status = [False, False, False, False, False]  # 初始化鼠标状态列表
        while True:
            mouse_image = self.menu_mouse_focus         # 设置鼠标图片
            mouse_pos = pygame.mouse.get_pos()          # 获取鼠标坐标
            mouse_click = pygame.mouse.get_pressed()    # 获取鼠标按下时的按钮
            self.screen.blit(self.menu_bd, (0, 0))      # 画上背景
            menu_text_pos = self.drawButtons()          # 调用drawButtons()画按钮

            for m in range(len(self.menu_text)):  # 根据鼠标的位置改变鼠标状态列表中的值
                mouse_status[m] = menu_text_pos[m][0][0] < mouse_pos[0] < menu_text_pos[m][1][0] \
                                  and menu_text_pos[m][0][1] < mouse_pos[1] < menu_text_pos[m][1][1]

            for n in range(len(self.menu_text)):       # 当鼠标移动到菜单文字上时改变文字的颜色
                if mouse_status[n]:
                    focus_surf, focus_rect = self.textObject(self.menu_font, self.menu_text[n], self.menu_text_color[1],
                                                             menu_text_pos[n][1], 'bottomright')
                    self.screen.blit(focus_surf, focus_rect)

            if mouse_click[0] == 1:         # 在窗口中当鼠标按下时就更改鼠标图片
                mouse_image = self.menu_mouse_press

            if mouse_status[0] and mouse_click[0] == 1:     # 当按下about时
                pass
            elif mouse_status[1] and mouse_click[0] == 1:       # 当按下load时
                pass
            elif mouse_status[2] and mouse_click[0] == 1:       # 当按下start时调用startGame()
                self.startGame(mouse_pos)
            elif mouse_status[3] and mouse_click[0] == 1:       # 当按下config时
                pass
            elif mouse_status[4] and mouse_click[0] == 1:       # 当按下quit时调用quitGame()
                self.quitGame(mouse_pos)

            for event in pygame.event.get():  # 监听用户事件
                if event.type == pygame.QUIT:  # 关闭窗口时退出
                    exit()

            self.screen.blit(mouse_image, mouse_pos)        # 在光标的位置画鼠标图片
            self.clock.tick(self.fps)  # 设置FPS

            pygame.display.update()  # 刷新画面

    def quitGame(self, mouse_pos):
        """
        -- 退出程序
        :param mouse_pos: 鼠标的坐标值，(x, y)
        :return:
        """
        mouse_image = self.menu_mouse_press    # 更改鼠标图片
        while True:
            for event in pygame.event.get():  # 监听用户事件
                if event.type == pygame.MOUSEBUTTONUP:  # 当鼠标按键抬起时
                    pygame.time.wait(400)  # 暂停程序一段时间
                exit()      # 退出程序
            self.screen.blit(mouse_image, mouse_pos)  # 在光标的位置画鼠标图片
            pygame.display.update()  # 刷新画面

    def startGame(self, mouse_pos):
        """
        -- 开始游戏，调用载入函数，开始关卡，如果失败调用失败函数
        :param mouse_pos: mouse_pos: 鼠标的坐标值，(x, y)
        :return:bird_life：生命值
        """
        bird_life = self.bird_life     # 获取小鸟的生命值
        mouse_image = self.menu_mouse_press    # 更改鼠标图片
        while bird_life:
            for event in pygame.event.get():  # 监听用户事件
                if event.type == pygame.MOUSEBUTTONUP:  # 当鼠标按键抬起时
                    pygame.time.wait(400)  # 暂停程序一段时间
                    self.loading()   # 调用载入函数loading()
                    bird_life = levels.Level1().start(self.bird_life)       # 开始第1关，返回生命值
                    if bird_life == 'esc':
                        return bird_life
                    self.loading()   # 调用载入函数loading()
                    bird_life = levels.Level2().start(bird_life)  # 开始第2关，返回生命值
                    if bird_life == 'esc':
                        return bird_life
                    self.loading()   # 调用载入函数loading()
                    bird_life = levels.Level3().start(bird_life)  # 开始第3关，返回生命值
                    if bird_life == 'esc':
                        return bird_life

                    if bird_life == 0:      # 如果返回的生命值为０
                        self.losing()
                        return bird_life        # 返回0 ，退出循环
                    else:
                        pass                    # 暂时保留
            self.screen.blit(mouse_image, mouse_pos)  # 在光标的位置画鼠标图片
            self.clock.tick(self.fps)  # 设置FPS
            pygame.display.update()  # 刷新画面
        return bird_life

    def loading(self):
        """
        -- 游戏载入画面
        :return:
        """
        flag = True
        bird_x = self.loading_bird_pos[0][0]    # 小鸟的移动速度，为了代码简洁
        loading_surf, loading_rect = self.textObject(self.menu_font, self.loading_text, self.loading_text_color,
                                                     self.loading_text_pos, 'center')
        while flag:
            self.screen.blit(self.loading_bd, (0, 0))  # 画上背景
            bird_x = bird_x + self.loading_bird_v / self.fps
            bird_y = self.loading_bird_pos[0][1]
            if bird_x >= self.loading_bird_pos[1][0]:
                flag = False
            self.screen.blit(self.loading_bird_img, (bird_x, bird_y))   # 画小鸟
            self.screen.blit(loading_surf, loading_rect)    # 画上文字
            self.clock.tick(self.fps)  # 设置FPS
            pygame.display.update()  # 刷新画面

    def drawButtons(self):
        """
        -- 在窗口显示菜单文字，先获取所有文字的宽、高，再用遍历显示，返回菜单文字的坐标值数组
        :return: list: 菜单文字的坐标值，[((x1, y1), (x2, y2)), (...)]
        """
        menu_text_surf, menu_text_rect, width, height, menu_text_pos = [], [], [], [], []
        for n in range(len(self.menu_text)):
            n_text = self.menu_text[n]
            n_surf = self.menu_font.render(n_text, True, self.menu_text_color[0])
            n_rect = n_surf.get_rect()
            menu_text_surf.append(n_surf)
            menu_text_rect.append(n_rect)
            width.append(n_surf.get_width())
            height.append(n_surf.get_height())

        length = sum(width)
        spacing = (self.menu_text_pos[0][1]-self.menu_text_pos[0][0]-length)/(len(self.menu_text)-1)
        n_x = self.menu_text_pos[0][0] - spacing

        for n in range(len(self.menu_text)):
            n_x = n_x + width[n] + spacing
            menu_text_rect[n].bottomright = (n_x, self.menu_text_pos[1])
            menu_text_rect[n].topleft = (n_x-width[n], self.menu_text_pos[1]-height[n])
            menu_text_pos.append((menu_text_rect[n].topleft, menu_text_rect[n].bottomright))
            self.screen.blit(menu_text_surf[n], menu_text_rect[n])
        return menu_text_pos

    def losing(self):
        """
        -- 游戏结束后调用此页面，感觉写的有些复杂，以后再优化
        :return:
        """
        flag = True
        while flag:
            losing_surf, losing_rect = self.textObject(self.menu_font, self.losing_text, self.losing_text_color[0],
                                                       self.losing_text_pos, 'center')
            self.screen.blit(self.losing_bd, (0, 0))  # 画上背景
            self.screen.blit(losing_surf, losing_rect)  # 画上文字

            mouse_image = self.menu_mouse_focus  # 更改鼠标图片
            mouse_pos = pygame.mouse.get_pos()  # 获取鼠标坐标
            mouse_click = pygame.mouse.get_pressed()  # 获取鼠标按下时的按钮

            tl_x = losing_rect[0]
            tl_y = losing_rect[1]
            br_x = losing_rect[0] + losing_rect[2]
            br_y = losing_rect[1] + losing_rect[3]
            mouse_status = br_x > mouse_pos[0] > tl_x and br_y > mouse_pos[1] > tl_y

            if mouse_status:   # 当鼠标移动到菜单文字上时改变文字的颜色
                losing_surf, losing_rect = self.textObject(self.menu_font, self.losing_text, self.losing_text_color[1],
                                                           self.losing_text_pos, 'center')
                self.screen.blit(losing_surf, losing_rect)  # 画上文字

            if mouse_status and mouse_click[0] == 1:
                for event in pygame.event.get():  # 监听用户事件
                    if event.type == pygame.MOUSEBUTTONUP:  # 当鼠标按键抬起时
                        pygame.time.wait(400)  # 暂停程序一段时间
                        flag = False
                        return flag

            if mouse_click[0] == 1:         # 在窗口中当按下鼠标时就更改鼠标图片
                mouse_image = self.menu_mouse_press

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if mouse_status and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONUP:  # 当鼠标按键抬起时
                        pygame.time.wait(400)  # 暂停程序一段时间
                        flag = False

            self.screen.blit(mouse_image, mouse_pos)  # 在光标的位置画鼠标图片
            self.clock.tick(self.fps)  # 设置FPS
            pygame.display.update()  # 刷新画面
        return
