#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

"""
用程序证明MontyHall(三门问题)的概率，还是换门后的机率比较高啊
"""

import random


# noinspection PyPep8Naming
class MontyHall(object):
    def __init__(self):
        pass

    @staticmethod
    def noChangeDoor(n):
        door_list = ['A', 'B', 'C']
        count = 0
        choice_door = 'A'
        for i in range(n):
            door_ok = random.choice(door_list)
            if door_ok == choice_door:
                count += 1
        print('选定一扇门不换的概率：{:2d}%'.format(int(count/n*100)))

    @staticmethod
    def ChangeDoor(n):
        count = 0
        choice_door = 'A'
        for i in range(n):
            door_list = ['A', 'B', 'C']
            door_ok = random.choice(door_list)      # 选定一个门后有汽车
            if door_ok == choice_door:              # 按两种情况分别确定要打开哪扇门
                door_list.remove(choice_door)
                open_door = random.choice(door_list)
            else:
                door_list.remove(choice_door)
                door_list.remove(door_ok)
                open_door = door_list[0]

            door_list = ['A', 'B', 'C']             # 在所有的门中确定要换的那扇门
            door_list.remove(open_door)
            door_list.remove(choice_door)
            change_door = door_list[0]
            # print('CHOICE: %s, OK: %s, OPEN: %s, CHANGE: %s' % (choice_door, door_ok, open_door, change_door), end='')
            if door_ok == change_door:
                # print('    OK!!!!')
                count += 1
            # else:
                # print('    ------')
        print('决定换门后的概率：{:2d}%'.format(int(count / n * 100)))


def main():
    monty_hall = MontyHall()
    monty_hall.noChangeDoor(10000)
    monty_hall.ChangeDoor(10000)


if __name__ == '__main__':
    main()
