import pygame
import random
FONT_PX = 15
pygame.init()
winSur = pygame.display.set_mode((1710,1000))     #创建窗口
font = pygame.font.SysFont('fangsong', 20)
bg_suface = pygame.Surface((1710,1000), flags=pygame.SRCALPHA)      #落雨范围
pygame.Surface.convert(bg_suface)
bg_suface.fill(pygame.Color(0, 0, 0, 13))
winSur.fill((0, 0, 0))
# 数字
texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
colums = int(1000 / FONT_PX)
drops = [0 for i in range(colums)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(20)       #下落速度
    winSur.blit(bg_suface, (0, 0))
    for i in range(len(drops)):
        text = random.choice(texts)
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
        drops[i] += 1
        if drops[i] * 10 > 600 or random.random() > 0.95:
            drops[i] = 0
    pygame.display.flip()

import sys
import pygame
pygame.init()
a=pygame.display.set_mode((600,400))
a.fill((0,0,0))
pygame.display.set_caption("Hello World!")
f = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],50)
text = f.render()