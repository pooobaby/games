#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import threading
from sprites import *
from initialize import Init


# noinspection PyPep8Naming
# 主游戏类
class PlaneGame(object):
    def __init__(self):
        self.score = 0
        self.bullet_grade = 1  # 初始的子弹等级
        self.ready_time = pygame.time.get_ticks()   # 用来控制显示ready画面的时钟
        self.star_enemy_life = Init.STAR_ENEMY_LIFE  # 星星敌机需要几颗子弹
        self.bullet_type = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
        self.screen = pygame.display.set_mode(Init.SCREEN_RECT.size)

        self.clock = pygame.time.Clock()  # 创建游戏时钟
        self.__createSprite()  # 调用私有方法, 创建精灵和组

        pygame.time.set_timer(Init.CREATE_ENEMY_EVENT, Init.ENEMY_TIMER)  # 设置定时器事件
        pygame.time.set_timer(Init.OWN_FIRE_EVENT, Init.BULLET_TIMER)
        pygame.time.set_timer(Init.BONUS_ENEMY_EVENT, Init.BONUS_TIMER)
        pygame.time.set_timer(Init.STAR_ENEMY_EVENT, Init.START_TIMER)
        self.life_num = Init.LIFE_NUMS

    def __createSprite(self):
        """ 私有方法，创建精灵和组 """
        bg1 = BackGround(Init.BACKGROUND)  # 创建背景和组
        bg2 = BackGround(Init.BACKGROUND)
        bg2.rect.y = -bg2.rect.height  # ???
        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.ready_go_group = pygame.sprite.Group()   # 创建ready组
        self.ready_go_group.add(ReadyGo())
        self.enemy_red_group = pygame.sprite.Group()  # 创建红色敌机组
        self.enemy_down_group = pygame.sprite.Group()  # 创建被击中敌机组
        self.bonus_enemy_group = pygame.sprite.Group()  # 创建加分敌机组
        self.gold_coin_group = pygame.sprite.Group()  # 创建金币组
        self.star_enemy_group = pygame.sprite.Group()  # 创建星星敌机组
        self.star_coin_group = pygame.sprite.Group()  # 创建星星组
        self.own_died_group = pygame.sprite.Group()  # 创建自己死亡飞机的组
        self.__resetOwn()  # 创建自己的飞机和组

    def start(self):
        """ 游戏开始 """
        while True:
            self.clock.tick(Init.FPS)  # 刷新帧率
            self.__eventHandler()  # 事件监听
            self.__checkCollide()  # 碰撞检测
            self.__updateSprites()  # 更新/绘制画面

            pygame.display.update()  # 更新屏幕显示
            self.__gameOver()  # 游戏结束

    def __eventHandler(self):
        """ 事件监听(监听定时器常量) """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 判断是否退出游戏
                PlaneGame.quit()
            elif event.type == Init.CREATE_ENEMY_EVENT:  # 当事件值等于CREATE_ENEMY_EVENT时，将敌机精灵添加到组
                enemy = EnemyRed()
                self.enemy_red_group.add(enemy)
            elif event.type == Init.BONUS_ENEMY_EVENT:  # 当事件值等于BONUS_ENEMY_EVENT时，将加分敌机加入到组
                bonus_enemy = EnemyRed()
                self.bonus_enemy_group.add(bonus_enemy)
            elif event.type == Init.STAR_ENEMY_EVENT:  # 当事件值等于STAR_ENEMY_EVENT时，将星星敌机加入到组
                self.star_enemy_life = Init.STAR_ENEMY_LIFE  # 赋予新的星星敌机生命值
                star_enemy = EnemyBlue()
                self.star_enemy_group.add(star_enemy)
            elif event.type == Init.OWN_FIRE_EVENT:  # 当事件值等于OWN_FIRE_EVENT时，按子弹等级开火
                for n in self.bullet_type:
                    grade = 4 if self.bullet_grade > 4 else self.bullet_grade
                    if grade == n:
                        exec('self.own.fire{}()'.format(self.bullet_type[n]))

        keys_pressed = pygame.key.get_pressed()  # 使用键盘提供的方法获取按键, 得到一个按键元组
        if keys_pressed[pygame.K_RIGHT]:  # 按右方向键时向右移动，水平速度为4
            self.own.speed_y = 0  # 同时将垂直方向的速度变为0
            self.own.speed_x = Init.MOVE_SPEED
        elif keys_pressed[pygame.K_LEFT]:  # 按左方向键时向右移动，水平速度为4
            self.own.speed_y = 0
            self.own.speed_x = -Init.MOVE_SPEED
        elif keys_pressed[pygame.K_UP]:  # 按上方向键时向右移动，垂直速度为-4
            self.own.speed_x = 0  # 同时将水平方向的速度变为0
            self.own.speed_y = -Init.MOVE_SPEED
        elif keys_pressed[pygame.K_DOWN]:  # 按下方向键时向右移动，垂直速度为4
            self.own.speed_x = 0
            self.own.speed_y = Init.MOVE_SPEED
        elif keys_pressed[pygame.K_SPACE]:  # 按空格键时暂停游戏
            self.__gamePause(True)
        else:  # 按其他键或不按时不移动
            self.own.speed_x = 0
            self.own.speed_y = 0

    def __checkCollide(self):
        """ 碰撞检测 """
        # 当子弹和敌机碰撞，敌机爆炸，得分加1，groupcollide()是精灵基类中的方法，返回一个字典，子弹是键，敌机是值
        killers = pygame.sprite.groupcollide(self.own.bullets, self.enemy_red_group, True, True)  # 子弹摧毁敌机
        if len(killers) > 0:  # 如果返回值长度大于0时，得分加1
            self.score += 1
            enemy_down = SpriteDown(Init.ENEMY_DOWN_IMAGE, list(killers.keys())[0].rect, 0)  # 取出碰撞字典中的键用来定位显示爆炸
            self.enemy_down_group.add(enemy_down)

        # 当敌机和已机碰撞，飞机数量减1，1秒后重新显示一架飞机
        died_1 = pygame.sprite.groupcollide(self.enemy_red_group, self.own_group, True, True)  # 敌机撞毁自己飞机
        died_2 = pygame.sprite.groupcollide(self.bonus_enemy_group, self.own_group, True, True)  # 加分敌机撞毁自己飞机
        died_3 = pygame.sprite.groupcollide(self.star_enemy_group, self.own_group, True, True)  # 星星敌机撞毁自己飞机
        died_owns = {**died_1, **died_2, **died_3}  # 合并字典
        if len(died_owns) > 0:  # 列表有内容代表发生碰撞了
            self.life_num -= 1  # 飞机数量减1
            own_died = SpriteDown(Init.OWN_DOWN_IMAGE, list(died_owns.keys())[0].rect, 0)
            self.own_died_group.add(own_died)
            self.s = threading.Timer(1, self.__resetOwn)  # 设置一个多线程定时调用函数，1秒后开始执行
            self.s.start()

        # 当子弹和加分敌机碰撞，出现金币继续下落
        bonus_enemies = pygame.sprite.groupcollide(self.own.bullets, self.bonus_enemy_group, True, True)
        if len(bonus_enemies) > 0:
            self.score += 1
            gold_coin = SpriteDown(Init.GOLD_COIN_IMAGE, list(bonus_enemies.keys())[0].rect, 1)
            self.gold_coin_group.add(gold_coin)

        # 当已机和硬币碰撞，得分+5，金币消失
        gold = pygame.sprite.groupcollide(self.gold_coin_group, self.own_group, True, False)
        if len(gold) > 0:
            self.score += 5

        # 当子弹和星星敌机碰撞，子弹消失，超过3颗子弹后出现星星继续下落
        if self.star_enemy_life <= 0:
            star_enemy = pygame.sprite.groupcollide(self.own.bullets, self.star_enemy_group, True, True)
            if len(star_enemy) > 0:
                self.score += 5
                star_coin = SpriteDown(Init.STAR_IMAGE, list(star_enemy.keys())[0].rect, 1)
                self.star_coin_group.add(star_coin)
        else:
            star_enemies = pygame.sprite.groupcollide(self.own.bullets, self.star_enemy_group, True, False)
            if len(star_enemies) > 0:
                self.star_enemy_life -= 1

        # 当已机和星星碰撞，得分+10，子弹等级+1
        star = pygame.sprite.groupcollide(self.star_coin_group, self.own_group, True, False)
        if len(star) > 0:
            self.score += 10
            self.bullet_grade += 1

    def __resetOwn(self):
        """ 自己飞机重生 """
        self.own = Own()  # 创建自己的飞机精灵和精灵组
        self.own_group = pygame.sprite.Group(self.own)
        self.bullet_grade = 1  # 初始的子弹等级

    def __infoDisplay(self, text, pos, angle):
        """
        -- 显示游戏信息
        :param text: 文字内容
        :param pos: 位置[x, y]
        :param angle: 用来定位的角
        :return:
        """
        score_font = pygame.font.Font(Init.SYS_FONT, 24)
        score_text = score_font.render(text, True, (255, 255, 255))
        text_rect = score_text.get_rect()
        exec('text_rect.{}={}'.format(angle, pos))
        self.screen.blit(score_text, text_rect)

    def __updateSprites(self):
        """ 更新/绘制精灵组 """
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.__infoDisplay('score ' + str(self.score), [20, 10], 'topleft')
        self.__infoDisplay('level 01', [492, 10], 'topright')
        self.__infoDisplay('life ' + str(self.life_num), [230, 10], 'topleft')

        if pygame.time.get_ticks() < self.ready_time + 3000:    # 显示ready画面3秒
            self.ready_go_group.update()
            self.ready_go_group.draw(self.screen)

        if pygame.time.get_ticks() > self.ready_time + 4000:    # ready画面1秒后开始显示游戏元素
            self.enemy_red_group.update()
            self.enemy_red_group.draw(self.screen)    # 显示敌机
            self.bonus_enemy_group.update()
            self.bonus_enemy_group.draw(self.screen)  # 显示加分敌机
            self.star_enemy_group.update()
            self.star_enemy_group.draw(self.screen)  # 显示星星敌机
            self.enemy_down_group.update()
            self.enemy_down_group.draw(self.screen)  # 显示敌机爆炸
            self.own.bullets.update()
            self.own.bullets.draw(self.screen)  # 显示子弹
            self.own_died_group.update()
            self.own_died_group.draw(self.screen)  # 显示已方飞机爆炸
            self.gold_coin_group.update()
            self.gold_coin_group.draw(self.screen)  # 显示金币
            self.star_coin_group.update()
            self.star_coin_group.draw(self.screen)  # 显示星星
            self.own_group.update()
            self.own_group.draw(self.screen)  # 显示已方飞机

    def __gamePause(self, pause=False):
        """ 暂停游戏， 按任意键退出"""
        self.__infoDisplay('Any key to continue...', Init.SCREEN_CENTER, 'center')
        pygame.display.update()  # 更新屏幕显示
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    PlaneGame.quit()
                elif event.type == pygame.KEYDOWN:
                    pause = False

    def __gameOver(self):
        """ 游戏结束，按ESC重新开始 """
        if self.life_num == 0:  # 如果飞机数量为0，退出游戏
            game_over = pygame.image.load(Init.GAME_OVER)  # 显示GAMEOVER图片
            self.screen.blit(game_over, (50, 150))
            self.__infoDisplay('press ESC play again...', Init.SCREEN_CENTER, 'center')
            pygame.display.update()  # 更新屏幕显示
            flag = True
            while flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        PlaneGame.quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  # 按SPACE重新开始游戏
                            flag = False
                            PlaneGame().start()

    @staticmethod
    def quit():
        """ 静态函数，退出游戏 """
        pygame.quit()
        exit()
