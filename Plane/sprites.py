#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import random
import pygame
from initialize import Init


# 游戏精灵父类
# noinspection PyPep8Naming
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()                          # 调用父类的初始化方法
        self.image = pygame.image.load(image_name)  # 定义对象的属性(图像)
        self.rect = self.image.get_rect()           # 定义对象的属性(位置)
        self.speed = speed                          # 定义速度
        self.speed_x = speed                        # 定义自己飞机的水平速度
        self.speed_y = speed                        # 定义自己飞机的垂直速度

    def update(self):
        self.rect.y += self.speed                   # 在屏幕的垂直方向上移动

    def updateObliqueLeft(self):                    # 在屏幕上向左斜方移动
        self.rect.x += self.speed
        self.rect.y += self.speed

    def updateObliqueRight(self):                   # 在屏幕上向向斜方移动
        self.rect.x -= self.speed
        self.rect.y += self.speed


# 窗口背景子类
class BackGround(GameSprite):
    def update(self):
        super().update()                            # 调用父类的update方法
        if self.rect.y >= self.rect.height:         # ??? 如果背景图片的y超过屏幕高度，y值变为高度的负值
            self.rect.y = -self.rect.height


# noinspection PyPep8Naming
# 自己的飞机子类
class Own(GameSprite):
    def __init__(self):
        super().__init__(Init.OWN_IMAGE, 0)              # 调用父类方法,定义自己飞机的图像和和初始速度
        self.rect.centerx = Init.SCREEN_RECT.centerx     # 设置Own的位置，centerx指图像中心的的x值
        self.rect.y = Init.SCREEN_RECT.height - self.rect.height
        self.bullets = pygame.sprite.Group()        # 创建子弹精灵组

    def update(self):
        """ Own在水平方向移动 """
        self.rect.x += self.speed_x                 # 移动的偏移量就是速度的值
        if self.rect.x < 0:                         # 控制Own不能离开屏幕
            self.rect.x = 0
        elif self.rect.x > Init.SCREEN_RECT.width - self.rect.width:
            self.rect.x = Init.SCREEN_RECT.width - self.rect.width
        """ Own在垂直方向移动 """
        self.rect.y += self.speed_y
        if self.rect.y < 0:                         # 控制Own不能离开屏幕
            self.rect.y = 0
        elif self.rect.y > Init.SCREEN_RECT.height - self.rect.height:
            self.rect.y = Init.SCREEN_RECT.height - self.rect.height

    def fireOne(self):
        """ 创建子弹精灵-1粒 """
        bullet = Bullet()
        bullet.rect.centerx = self.rect.centerx     # 指定子弹精灵初始位置
        bullet.rect.y = self.rect.y - 30            # 子弹显示的y值在飞机上方
        self.bullets.add(bullet)                    # 将子弹添加到子弹精灵组
        return bullet

    def fireTwo(self):
        """ 创建子弹精灵-2粒 """
        bullet_l = Bullet()
        bullet_l.rect.centerx = self.rect.centerx - self.rect.width / 2     # 指定左边子弹精灵初始位置
        bullet_l.rect.y = self.rect.y - 30          # 子弹显示的y值在飞机上方
        bullet_r = Bullet()
        bullet_r.rect.centerx = self.rect.centerx + self.rect.width / 2     # 指定右边子弹精灵初始位置
        bullet_r.rect.y = self.rect.y - 30          # 子弹显示的y值在飞机上方
        self.bullets.add(bullet_l, bullet_r)        # 将子弹添加到子弹精灵组
        return bullet_l, bullet_r

    def fireThree(self):
        """ 创建子弹精灵-3粒 """
        bullet_one = self.fireOne()
        bullet_two_l, bullet_two_r = self.fireTwo()
        self.bullets.add(bullet_one, bullet_two_l, bullet_two_r)                      # 将子弹添加到子弹精灵组
        return bullet_one, bullet_two_l, bullet_two_r

    def fireFour(self):
        """ 创建子弹精灵-4粒 """
        bullet_one, bullet_two_l, bullet_two_r = self.fireThree()
        bullet_ol = Bullet('LEFT')
        bullet_ol.rect.centerx = self.rect.centerx - self.rect.width / 2     # 指定左边倾斜子弹精灵初始位置
        bullet_ol.rect.y = self.rect.y - 30          # 子弹显示的y值在飞机上方
        bullet_or = Bullet('RIGHT')
        bullet_or.rect.centerx = self.rect.centerx + self.rect.width / 2     # 指定右边倾斜子弹精灵初始位置
        bullet_or.rect.y = self.rect.y - 30          # 子弹显示的y值在飞机上方
        self.bullets.add(bullet_one, bullet_two_l, bullet_two_r, bullet_ol, bullet_or)    # 将子弹添加到子弹精灵组


# 被击中的精灵子类
class SpriteDown(GameSprite):
    def __init__(self, image, pos, flag):
        """
        -- 根据传入的参数，显示图像
        :param image: 需要显示的图像
        :param pos: surface.rect
        :param flag: 0, 1
        """
        super().__init__(image)
        self.killed_pos = pos
        self.rect.x = self.killed_pos[0]
        self.rect.y = self.killed_pos[1]
        self.flag = flag

    def update(self):
        super().update()        # 调用父类的update方法
        if self.flag == 1:      # 如果是道具，判断是否飞出屏幕, 及时删除释放出内存空间
            if self.rect.y >= Init.SCREEN_RECT.height:
                self.kill()
        else:                   # 如果不是道具，经过一段路后就删除
            if self.rect.y > self.killed_pos[1] + self.rect.height:
                self.kill()


# 子弹子类
class Bullet(GameSprite):
    def __init__(self, flag='VERTICAL'):
        """
        -- 根据传入的参数，生成子弹
        :param flag: 'VERTICAL', 'LEFT', 'RIGHT'
        """
        super().__init__(Init.BULLET_IMAGE, -6)      # 调用父类方法,定义子弹的图像和初始速度
        self.flag = flag

    def update(self):
        if self.flag == 'LEFT':                 # 根据flag的值，选择调用哪种子弹的运行轨迹
            super().updateObliqueLeft()
        elif self.flag == 'RIGHT':
            super().updateObliqueRight()
        else:
            super().update()
        if self.rect.y < 0 or Init.SCREEN_RECT.width < self.rect.x < 0:
            self.kill()         # kill()是精灵基类中的方法


# 蓝色敌机子类，飞行轨迹与红色不同
class EnemyBlue(GameSprite):
    def __init__(self):
        self.x = [-1, 1]                                # 蓝色敌机的运动方向是随机的
        super().__init__(Init.ENEMY_BLUE_IMAGE)              # 调用父类方法,定义敌机图像和初始速度
        self.speed = 1                                  # 蓝色敌机的速度为1，分成xy两个轴的速度
        self.speed_x = random.choice(self.x)
        self.rect.y = -self.rect.height                 # 敌机出现时的y值
        max_x = Init.SCREEN_RECT.width - self.rect.width     # 敌机出现时的最大x值
        self.rect.x = random.randint(0, max_x)          # 随机生成敌机出现时的x值

    def update(self):
        super().update()                                # 调用父类的update方法
        if self.rect.x <= 0 or self.rect.x >= Init.SCREEN_RECT.width - self.rect.width:  # 当超过屏幕时取反向速度
            self.speed_x = -self.speed_x
        self.rect.x += self.speed_x
        if self.rect.y >= Init.SCREEN_RECT.height:           # 判断敌机是否飞出屏幕, 及时删除释放出内存空间
            self.kill()


# 红色敌机子类
class EnemyRed(GameSprite):
    def __init__(self):
        super().__init__(Init.ENEMY_RED_IMAGE)               # 调用父类方法,定义敌机图像和初始速度
        self.speed = random.randint(2, 5)               # 随机定义敌机的速度，如果是1则显示在屏幕上不动
        self.rect.y = -self.rect.height                 # 敌机出现时的y值
        max_x = Init.SCREEN_RECT.width - self.rect.width     # 敌机出现时的最大x值
        self.rect.x = random.randint(0, max_x)          # 随机生成敌机出现时的x值

    def update(self):
        super().update()                                # 调用父类的update方法
        if self.rect.y >= Init.SCREEN_RECT.height:           # 判断敌机是否飞出屏幕, 及时删除释放出内存空间
            self.kill()


# 准备开始子类
class ReadyGo(GameSprite):
    def __init__(self):
        super().__init__(Init.READY_IMAGE, 0)               # 调用父类方法,定义准备图像
        self.rect.x = 128
        self.rect.y = 200

    def update(self):
        super().update()                                # 调用父类的update方法
