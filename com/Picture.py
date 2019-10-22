import pygame
import random
from pygame.locals import *
from os import path
from com  import BasicParameters

#######################################加载图片#######################################


#获取图片库和图片路径
img_dir = path.join(path.dirname(__file__),'pic')
#加载游戏进行中背景图片
background = pygame.image.load(path.join(img_dir,'starfield.png')).convert()
background = pygame.transform.scale(background,(WIDTH,1536))
height = -936

#加载玩家图片
player_img = pygame.image.load(path.join(img_dir,'player.png')).convert()
player_mini_img = pygame.transform.scale(player_img,(25, 19))
player_mini_img.set_colorkey(BLACK)

#加载玩家炮弹、导弹图片
bullet_img = pygame.image.load(path.join(img_dir,'bullet.png')).convert()
missile_img = pygame.image.load(path.join(img_dir,'missile.png')).convert_alpha()

#加载敌机炮弹图片
enemies_bullet_img = pygame.image.load(path.join(img_dir,'enemies_bullet.png')).convert()

#加载盾牌、闪电图片
powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt.png')).convert()

#加载敌机和火山石图片
enemies_images = []
lava_images = []
#敌机
enemies_list = [
    'enemies1.png',
    'enemies2.png',
    'enemies3.png'
]
#火山石
lava_list = [
    'lava_med.png',
    'lava_small1.png',
    'lava_small2.png',
    'lava_tiny.png'
]
for image in enemies_list:
    enemies_img = pygame.image.load(path.join(img_dir,image)).convert()
    enemies_img = pygame.transform.scale(enemies_img,(80, 60))
    enemies_images.append(enemies_img)
for image in lava_list:
    lava_images.append(pygame.image.load(path.join(img_dir,image)).convert())

#加载爆炸图片
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    #敌机、火山石爆炸
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(BLACK)
    #大爆炸
    img_lg = pygame.transform.scale(img,(75,75))
    explosion_anim['lg'].append(img_lg)
    #小爆炸
    img_sm = pygame.transform.scale(img,(32,32))
    explosion_anim['sm'].append(img_sm)
    #玩家爆炸
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)