import pygame
import random
from pygame.locals import *
from os import path




#######################################基本参数配置#######################################



#定义游戏窗口、玩家血量条尺寸，游戏运行速度、炮火持续时间等参数
WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000
BAR_LENGTH = 100
BAR_HEIGHT = 10

#定义白、黑、红、绿、蓝、黄的RGB参数
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#初始化pygame模块，创建游戏窗口、游戏窗口命名、创建跟踪时间对象
pygame.init()
pygame.mixer.init()  #初始化音效
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aircraft Battle")
clock = pygame.time.Clock()

#定义文本字体
font_name = pygame.font.match_font('arial')
