#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright By Eric in 2020

n = 1000
a = 100
s = 30
for i in range(s):
    dd = int(a * 0.9 ** i)
    n -= dd
    print (i, n, dd)
