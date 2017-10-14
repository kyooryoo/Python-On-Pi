# the offical sample code is available at:
# http://media.wiley.com/product_ancillary/6X/11184644/DOWNLOAD/raspberrysnake.py

from pygame.locals import *
import pygame
import random
import sys
import time

pygame.init()
fpsClock=pygame.time.Clock()

gameSurface=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pi Snake")

foodColor=pygame.Color(0,255,0)
bgColor=pygame.Color(255,255,255)
snakeColor=pygame.Color(0,0,0)
textColor=pygame.Color(255,0,0)

snakePos=[120,240]
snakeSeg=[[120,240],[120,220]]
foodPosition=[400,300]
foodSpawned=1
Dir="D"
changeDir=Dir
Score=0
Speed=5
SpeedCount=0

def finish():
 # set property of the message
 finishFont=pygame.font.Font(None,56)
 # set content of the message
 msg="Game Over! Score = " + str(Score)
 # render the message
 finishSurf=finishFont.render(msg,True,textColor)
 # prepare a rectangle
 finishRect=finishSurf.get_rect()
 finishRect.midtop=(400,10)
 # draw the rectangle over message text
 gameSurface.blit(finishSurf, finishRect)
 pygame.display.flip()
 time.sleep(5)
 pygame.quit()
 exit(0)

while 1:
 for event in pygame.event.get():
  if event.type==QUIT:
   pygame.quit()
   exit(0)
  elif event.type==KEYDOWN:
   if event.key==ord("d") or event.key==K_RIGHT:
    changeDir="R"
   if event.key==ord("a") or event.key==K_LEFT:
    changeDir="L"
   if event.key==ord("w") or event.key==K_UP:
    changeDir="U"
   if event.key==ord("S") or event.key==K_DOWN:
    changeDir="D"
   if event.key==K_ESCAPE:
    pygame.event.post(pygame.event.Event(QUIT))
    pygame.quit()
    exit(0)

 # only allow snake turn 90 degree
 # forbit snake turn 180 degree
 if changeDir=="R" and not Dir=="L":
  Dir=changeDir
 if changeDir=="L" and not Dir=="R":
  Dir=changeDir
 if changeDir=="U" and not Dir=="D":
  Dir=changeDir
 if changeDir=="D" and not Dir=="U":
  Dir=changeDir

 # For every time of direction change
 # a new position is defined by the snake head size
 if Dir=="R":
  snakePos[0]+=20
 if Dir=="L":
  snakePos[0]-=20
 if Dir=="U":
  snakePos[1]-=20
 if Dir=="D":
  snakePos[1]+=20

 snakeSeg.insert(0,list(snakePos))
 if snakePos[0]==foodPosition[0] and snakePos[1]==foodPosition[1]:
  foodSpawned=0
  Score=Score+1
  SpeedCount=SpeedCount+1
  if SpeedCount==5:
   SpeedCount=0
   Speed=Speed+1
 else:
  snakeSeg.pop()

 if foodSpawned==0:
  x=random.randrange(1,40)
  y=random.randrange(1,30)
  foodPosition=[int(x*20),int(y*20)]
  foodSpawned=1

 gameSurface.fill(bgColor)
 for position in snakeSeg:
  pygame.draw.rect(gameSurface,snakeColor,Rect(position[0],position[1],20,20))
 pygame.draw.circle(gameSurface,foodColor,(foodPosition[0]+10,foodPosition[1]+10),10,0)
 pygame.display.flip()
 if snakePos[0]>780 or snakePos[0]<0:
  finish()
 if snakePos[1]>580 or snakePos[1]<0:
  finish()
 for snakeBody in snakeSeg[1:]:
  if snakePos[0]==snakeBody[0] and snakePos[1]==snakeBody[1]:
   finish()
 fpsClock.tick(Speed)
