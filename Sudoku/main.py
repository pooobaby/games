#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

import sys
from config import *
from command import Commander


def main():
    sys.setrecursionlimit(10000)
    commander = Commander()
    board = commander.createSudoku()
    commander.solveSudoku(board)
    # commander.solveSudoku(BOARD)


if __name__ == '__main__':
    main()
