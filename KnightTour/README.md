# KnightTour
用pygame编写的练习算法小程序，以后会不断更新

## 游戏说明:
* 问题：用回溯算法解决骑士游历问题，并用窗口直观显示
* 从算法到程序完全是自己完成，对回溯算法有了更深刻的了解
* 但是这个不是真正的骑士游历问题的解法，真正的深度遍历是需要用递归实现的，最后不重复的走遍棋盘上的所有空格，需要从起点沿一条路线一直走下去，直到不能走为止，然后沿原路退回，清除棋盘标记后，再重新试探，先不写了，了解即可

## 系统文件：
- 【back_tracing.py】：主程序，实现回溯算法
- .\images\...：骑士图片，标记图片
- .\fonts\...：字体文件
- .\screenshot\...：程序画面截屏

## 游戏画面截屏
* 骑士游历问题棋盘分析  
![骑士游历问题棋盘分析](https://github.com/pooobaby/games/blob/master/KnightTour/screenshot/chessboard.jpg?raw=true)
* 用回溯算法解决的骑士游历问题
![用回溯算法解决的骑士游历问题](https://github.com/pooobaby/games/blob/master/KnightTour/screenshot/back_tracing.jpg?raw=true)
