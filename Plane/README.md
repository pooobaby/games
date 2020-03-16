# Plane
用pygame编写的第二个小游戏，以后会不断更新

## 游戏说明:
* 目前只做了一个关卡，有三种敌机，自己飞机的子弹类型有四种
* 在游戏中空格键是暂停，游戏结束后ESC键是重新开始
* 暂时没有加入音效
* 游戏窗口尺寸为512*768

## 关卡内元素介绍
1. ENEMY_RED：红色小敌机，数量多，出现频率高，击落后有机率出现钱币，可以加分
2. ENEMY_BLUE：蓝色中型敌机，出现频率低，需要多颗子弹击落，击落后有机率出现星星，可以加强火力
3. ENEMY_BOSS：绿色大型敌机，出现频率低，可以发射子弹，需要很多颗子弹击落，击落后得分较高
4. BULLET_BOSS: 绿色大型敌机发射的子弹
5. OWN: 自己的飞机
6. OWN_BULLET: 自己飞机发射的子弹

## 系统文件：
- 【start.py】：开始游戏的主文件
- 【level_01.py】：游戏第一关
- 【sprites.py】：建立游戏精灵类文件
- 【initialize.py】：系统设置文件，包含各种游戏基本元素的设定值
- .\fonts\\...：游戏使用的字体
- .\images\\...：游戏使用的图像文件
- .\screenshot\...：游戏画面截屏

## 游戏画面截屏
* 游戏载入图片  
![游戏载入](https://github.com/pooobaby/games/blob/master/Plane/screenshot/loading.jpg?raw=true)
* 第一关-图A  
![第一关-A](https://github.com/pooobaby/games/blob/master/Plane/screenshot/level_01_a.jpg?raw=true)
* 第一关-图B  
![第一关-B](https://github.com/pooobaby/games/blob/master/Plane/screenshot/level_01_b.jpg?raw=true)
* 游戏结束  
![游戏结束](https://github.com/pooobaby/games/blob/master/Plane/screenshot/gameover.jpg?raw=true)
