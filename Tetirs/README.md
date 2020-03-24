# Tetris
俄罗斯方块小游戏

## 游戏说明:
* 感谢[@yeahatgithub][1]的程序，内核基本没变，界面进行了修改
* 在游戏中F1是开始，F2是暂停，方向键控制方块，空格键快速下落
* 暂时没有加入音效
* 游戏窗口尺寸为800*600

## 游戏界面元素介绍
1. 游戏可以显示关卡，得分，最高分，历史游戏记录，消除行数
2. 历史游戏记录保存在Hi-score.txt文件中
3. 每消除一行，左下方的小蜗牛就前进一步，过关时，抵达控制杆，同时游戏左侧的灯泡变亮，蜗牛返回起点重新开始

## 系统文件：
- 【start.py】：开始游戏的主文件
- 【display.py】：游戏画面显示类
- 【resource.py】：游戏元素生成类
- 【state.py】：游戏状态控制类
- 【wall.py】：方块墙区域类
- 【piece.py】：方块生成类
- 【initialize.py】：系统设置文件，包含各种游戏基本元素的设定值
- .\fonts\\...：游戏使用的字体
- .\images\\...：游戏使用的图像文件
- .\screenshot\...：游戏画面截屏
- .\zip\Tetirs.zip：用pyinstaller打包的可执行文件压缩包，下载后解压即可执行

## 游戏画面截屏
* 游戏图片  
![游戏载入](https://github.com/pooobaby/games/blob/master/Tetirs/screenshot/tetirs.jpg?raw=true)

[1]:https://github.com/yeahatgithub
