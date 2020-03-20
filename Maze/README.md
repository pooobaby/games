# Maze
用pygame编写的第四个小游戏，以后会不断更新

## 游戏说明:
* 问题：prim算法生成的迷宫还没有实现找寻终点和路径
* 共完成了三个程序，从易到难
* 主要实现了两种算法，递归回溯和prim，
* 通过测试，prim算法比回溯算法快了不止一两倍

## 系统文件：
- 【sample_maze.py】：简单迷宫，从走迷宫开始编写，生成迷宫用的方法中随机生成，简直就是垃圾
- 【recursion_tracing.py】：采用递归回溯算法编写的迷宫生成程序，可以直接生成迷宫路径和起终点，对于大型迷宫速度生成效率较慢
- 【prim.py】：采用prim算法编写的迷宫生成程序，比递归回溯算法快了好多，问题是不能生成迷宫路径和终点
- .\screenshot\...：游戏画面截屏

## 游戏画面截屏
* 用递归回溯算法生成的迷宫图片  
![用递归回溯算法生成的迷宫图片](https://github.com/pooobaby/games/blob/master/Maze/screenshot/recursion_tracing_0.jpg?raw=true)
*用递归回溯算法生成的迷宫路径
![用递归回溯算法生成的迷宫路径](https://github.com/pooobaby/games/blob/master/Maze/screenshot/recursion_tracing_1.jpg?raw=true)
*用prim算法生成的迷宫图片
![用prim算法生成的迷宫图片](https://github.com/pooobaby/games/blob/master/Maze/screenshot/prim_0.jpg?raw=true)
[1]:https://github.com/yeahatgithub
