import pygame

background = [1, 1, 2, 2, 2, 1]
screen = [0]*6                         #a new blank screen
for i in range(6):
    screen[i] = background[i]
print(screen)
# [1, 1, 2, 2, 2, 1]
playerpos = 3
screen[playerpos] = 8
print(screen)
screen[playerpos] = background[playerpos]
playerpos = playerpos - 1
screen[playerpos] = 8
print(screen)