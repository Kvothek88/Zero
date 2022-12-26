import pygame
import os
import math
import random

pygame.init()

screen = pygame.display.set_mode((900,540))
pygame.display.set_caption("Megaman")

bg = pygame.image.load(os.path.join('images','back.png'))
bg2 = pygame.image.load(os.path.join('images','back2.png'))
land = pygame.image.load(os.path.join('images','land.png'))
walkRight = [pygame.image.load(os.path.join('images','R1.png')), pygame.image.load(os.path.join('images','R2.png')), pygame.image.load(os.path.join('images','R3.png')), pygame.image.load(os.path.join('images','R4.png')), pygame.image.load(os.path.join('images','R5.png')), pygame.image.load(os.path.join('images','R6.png')), pygame.image.load(os.path.join('images','R7.png')), pygame.image.load(os.path.join('images','R8.png')), pygame.image.load(os.path.join('images','R9.png'))]
walkLeft = [pygame.image.load(os.path.join('images','L1.png')), pygame.image.load(os.path.join('images','L2.png')), pygame.image.load(os.path.join('images','L3.png')), pygame.image.load(os.path.join('images','L4.png')), pygame.image.load(os.path.join('images','L5.png')), pygame.image.load(os.path.join('images','L6.png')), pygame.image.load(os.path.join('images','L7.png')), pygame.image.load(os.path.join('images','L8.png')), pygame.image.load(os.path.join('images','L9.png'))]
jumpRight = [pygame.image.load(os.path.join('images','JR1.png')), pygame.image.load(os.path.join('images','JR2.png')), pygame.image.load(os.path.join('images','JR3.png')), pygame.image.load(os.path.join('images','JR4.png')), pygame.image.load(os.path.join('images','JR5.png'))]
jumpLeft = [pygame.image.load(os.path.join('images','JL1.png')), pygame.image.load(os.path.join('images','JL2.png')), pygame.image.load(os.path.join('images','JL3.png')), pygame.image.load(os.path.join('images','JL4.png')), pygame.image.load(os.path.join('images','JL5.png'))]
standRight = pygame.image.load(os.path.join('images','standright.png'))
standLeft = pygame.image.load(os.path.join('images','standleft.png'))
runShootRight = [pygame.image.load(os.path.join('images','SR1.png')), pygame.image.load(os.path.join('images','SR2.png')), pygame.image.load(os.path.join('images','SR3.png')), pygame.image.load(os.path.join('images','SR4.png')), pygame.image.load(os.path.join('images','SR5.png')), pygame.image.load(os.path.join('images','SR6.png')), pygame.image.load(os.path.join('images','SR7.png')), pygame.image.load(os.path.join('images','SR8.png')), pygame.image.load(os.path.join('images','SR9.png'))]
runShootLeft = [pygame.image.load(os.path.join('images','SL1.png')), pygame.image.load(os.path.join('images','SL2.png')), pygame.image.load(os.path.join('images','SL3.png')), pygame.image.load(os.path.join('images','SL4.png')), pygame.image.load(os.path.join('images','SL5.png')), pygame.image.load(os.path.join('images','SL6.png')), pygame.image.load(os.path.join('images','SL7.png')), pygame.image.load(os.path.join('images','SL8.png')), pygame.image.load(os.path.join('images','SL9.png'))]
jumpShootRight = [pygame.image.load(os.path.join('images','JSR1.png')), pygame.image.load(os.path.join('images','JSR2.png')), pygame.image.load(os.path.join('images','JSR3.png')), pygame.image.load(os.path.join('images','JSR4.png')), pygame.image.load(os.path.join('images','JSR5.png'))]
jumpShootLeft = [pygame.image.load(os.path.join('images','JSL1.png')), pygame.image.load(os.path.join('images','JSL2.png')), pygame.image.load(os.path.join('images','JSL3.png')), pygame.image.load(os.path.join('images','JSL4.png')), pygame.image.load(os.path.join('images','JSL5.png'))]
jumpShootUpRight = [pygame.image.load(os.path.join('images','JSUR1.png')), pygame.image.load(os.path.join('images','JSUR2.png')), pygame.image.load(os.path.join('images','JSUR3.png')), pygame.image.load(os.path.join('images','JSUR4.png')), pygame.image.load(os.path.join('images','JSUR5.png'))]
jumpShootUpLeft = [pygame.image.load(os.path.join('images','JSUL1.png')), pygame.image.load(os.path.join('images','JSUL2.png')), pygame.image.load(os.path.join('images','JSUL3.png')), pygame.image.load(os.path.join('images','JSUL4.png')), pygame.image.load(os.path.join('images','JSUL5.png'))]
shootRight = pygame.image.load(os.path.join('images','shootright.png'))
shootLeft = pygame.image.load(os.path.join('images','shootleft.png'))
projectileRight = pygame.image.load(os.path.join('images','projectileRight.png'))
projectileLeft = pygame.image.load(os.path.join('images','projectileLeft.png'))
diagonalRight = pygame.image.load(os.path.join('images','diagonalRight.png'))
diagonalLeft = pygame.image.load(os.path.join('images','diagonalLeft.png'))
UpRight = pygame.image.load(os.path.join('images','UR.png'))
UpLeft = pygame.image.load(os.path.join('images','UL.png'))
deadRight = [pygame.image.load(os.path.join('images','DR1.png')), pygame.image.load(os.path.join('images','DR4.png'))]
deadLeft = [pygame.image.load(os.path.join('images','DL1.png')), pygame.image.load(os.path.join('images','DL4.png'))]
runShootUpRight = [pygame.image.load(os.path.join('images','RUR1.png')), pygame.image.load(os.path.join('images','RUR2.png')), pygame.image.load(os.path.join('images','RUR3.png')), pygame.image.load(os.path.join('images','RUR4.png')), pygame.image.load(os.path.join('images','RUR5.png')), pygame.image.load(os.path.join('images','RUR6.png')), pygame.image.load(os.path.join('images','RUR7.png')), pygame.image.load(os.path.join('images','RUR8.png')), pygame.image.load(os.path.join('images','RUR9.png'))]
runShootUpLeft = [pygame.image.load(os.path.join('images','RUL1.png')), pygame.image.load(os.path.join('images','RUL2.png')), pygame.image.load(os.path.join('images','RUL3.png')), pygame.image.load(os.path.join('images','RUL4.png')), pygame.image.load(os.path.join('images','RUL5.png')), pygame.image.load(os.path.join('images','RUL6.png')), pygame.image.load(os.path.join('images','RUL7.png')), pygame.image.load(os.path.join('images','RUL8.png')), pygame.image.load(os.path.join('images','RUL9.png'))]
head = pygame.image.load(os.path.join('images','head.png'))
enemyleft = [pygame.image.load(os.path.join('images/enemy','EL00.png')), pygame.image.load(os.path.join('images/enemy','EL1.png')), pygame.image.load(os.path.join('images/enemy','EL2.png')), pygame.image.load(os.path.join('images/enemy','EL3.png')), pygame.image.load(os.path.join('images/enemy','EL4.png')), pygame.image.load(os.path.join('images/enemy','EL5.png')), pygame.image.load(os.path.join('images/enemy','EL6.png')), pygame.image.load(os.path.join('images/enemy','EL7.png')), pygame.image.load(os.path.join('images/enemy','EL8.png')), pygame.image.load(os.path.join('images/enemy','EL9.png')),pygame.image.load(os.path.join('images/enemy','EL01.png')),pygame.image.load(os.path.join('images/enemy','EL02.png')),pygame.image.load(os.path.join('images/enemy','EL03.png')),pygame.image.load(os.path.join('images/enemy','EL04.png'))]
enemyright = [pygame.image.load(os.path.join('images/enemy','ER00.png')), pygame.image.load(os.path.join('images/enemy','ER1.png')), pygame.image.load(os.path.join('images/enemy','ER2.png')), pygame.image.load(os.path.join('images/enemy','ER3.png')), pygame.image.load(os.path.join('images/enemy','ER4.png')), pygame.image.load(os.path.join('images/enemy','ER5.png')), pygame.image.load(os.path.join('images/enemy','ER6.png')), pygame.image.load(os.path.join('images/enemy','ER7.png')), pygame.image.load(os.path.join('images/enemy','ER8.png')), pygame.image.load(os.path.join('images/enemy','ER9.png')),pygame.image.load(os.path.join('images/enemy','ER01.png')),pygame.image.load(os.path.join('images/enemy','ER02.png')),pygame.image.load(os.path.join('images/enemy','ER03.png')),pygame.image.load(os.path.join('images/enemy','ER04.png'))]
punchleft = [pygame.image.load(os.path.join('images/enemy','EPL1.png')), pygame.image.load(os.path.join('images/enemy','EPL2.png')),pygame.image.load(os.path.join('images/enemy','EPL3.png'))]
punchright = [pygame.image.load(os.path.join('images/enemy','EPR1.png')), pygame.image.load(os.path.join('images/enemy','EPR2.png')),pygame.image.load(os.path.join('images/enemy','EPR3.png'))]
explosion = [pygame.image.load(os.path.join('images','EX1.png')), pygame.image.load(os.path.join('images','EX2.png')), pygame.image.load(os.path.join('images','EX3.png')), pygame.image.load(os.path.join('images','EX4.png')), pygame.image.load(os.path.join('images','EX5.png')), pygame.image.load(os.path.join('images','EX6.png')), pygame.image.load(os.path.join('images','EX7.png')), pygame.image.load(os.path.join('images','EX8.png')), pygame.image.load(os.path.join('images','EX9.png'))]
menu = pygame.image.load(os.path.join('images','menu.png'))

#music = pygame.mixer.music.load(os.path.join('sounds','guile.mp3'))
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play(-1)
shieldSound = pygame.mixer.Sound(os.path.join('sounds','forcefield.wav'))
shieldSound.set_volume(2)
beam = pygame.mixer.Sound(os.path.join('sounds','beam.wav'))
beam.set_volume(0.2)
shieldblast = pygame.mixer.Sound(os.path.join('sounds','shieldblast.wav'))
shieldblast.set_volume(0.2)
blast = pygame.mixer.Sound(os.path.join('sounds','blast.wav'))
seismiccharge = pygame.mixer.Sound(os.path.join('sounds','seismiccharge.wav'))
seismiccharge.set_volume(0.6)
clock = pygame.time.Clock()
LIGHTRED = (255,0,0,128)
bg_x = 0
bg_y = 0
gravity = 16
start = False

class Shot():
    def __init__(self,x,y,rot,side,id):
        self.x = x
        self.y = y
        self.vel = 9
        self.rot = rot
        self.side = side
        self.id = id

    def draw(self,screen):
        pygame.draw.circle(screen, (0,0,0),(self.x,self.y), 4)
    
    def shotmove(self):
        if self.x < 900 and self.x > 0 and self.y < 383:
            if self.side == "Right":
                if self.rot > 0 and self.rot < 18:
                    self.x += round(math.sqrt(abs(self.rot))*0.6)
                    self.y += 9
                elif self.rot >= 18 and self.rot < 36:
                    self.x += round(math.sqrt(abs(self.rot))*0.8)
                    self.y += 9
                elif self.rot >= 36 and self.rot < 50:
                    self.x += round(math.sqrt(abs(self.rot))*1.2)
                    self.y += 9
                elif self.rot >= 50 and self.rot < 58:
                    self.x += round(math.sqrt(abs(self.rot))*1.6)
                    self.y += 9
                elif self.rot >= 58 and self.rot < 61:
                    self.x += round(math.sqrt(abs(self.rot))*1.8)
                    self.y += 9
                else:
                    self.x += round(math.sqrt(abs(self.rot))*2.2)
                    self.y += 9                                           
            else:
                if self.rot <= 0 and self.rot > -18:
                    self.x -= round(math.sqrt(abs(self.rot))*0.6)
                    self.y += 9
                elif self.rot <= -18 and self.rot > -36:
                    self.x -= round(math.sqrt(abs(self.rot))*0.8)
                    self.y += 9
                elif self.rot <= -36 and self.rot > -50:
                    self.x -= round(math.sqrt(abs(self.rot))*1.2)
                    self.y += 9
                elif self.rot <= -50 and self.rot > -58:
                    self.x -= round(math.sqrt(abs(self.rot))*1.6)
                    self.y += 9
                elif self.rot <= -58 and self.rot > -61:
                    self.x -= round(math.sqrt(abs(self.rot))*1.8)
                    self.y += 9
                else:
                    self.x -= round(math.sqrt(abs(self.rot))*2.2)
                    self.y += 9 
        else:
            shots_dict[self.id].pop(shots_dict[self.id].index(shot))
        if man.shield:
            if self.x > man.x -10 and self.x < man.x +65:
                if self.y > man.y - 10 and self.y < man.y + 60:
                    if len(shots_dict[self.id]) > 0:                  
                        shieldblast.play()
                        shots_dict[self.id].pop(shots_dict[self.id].index(shot))
        else:
            if self.x > man.x and self.x < man.x + 45:
                if self.y > man.y and self.y < man.y + 60:
                    if len(shots_dict[self.id]) > 0:
                        blast.play()
                        man.hitpoints -= 10
                        shots_dict[self.id].pop(shots_dict[self.id].index(shot))


class projectile():
    def __init__(self,x,y,facing,up):
        self.x = x
        self.y = y
        self.vel = 22
        self.facing = facing
        self.up = up


    def draw(self,screen):
        if self.facing == 1:
            if self.up:
                if man.isJump:
                    pygame.draw.circle(screen, (0,0,0),(self.x+12,self.y-22), 6)
                    screen.blit(diagonalRight, (self.x-1,self.y-33))
                else:
                    if man.right:
                        pygame.draw.circle(screen, (0,0,0),(self.x+18,self.y-13), 6)
                        screen.blit(diagonalRight, (self.x+3,self.y-23))
                    else:
                        pygame.draw.circle(screen, (0,0,0),(self.x+10,self.y-13), 6)
                        screen.blit(diagonalRight, (self.x-4,self.y-24))
            else:
                pygame.draw.circle(screen, (0,0,0),(self.x+15,self.y+11), 6)
                screen.blit(projectileRight, (self.x+2,self.y+5))
        else:
            if self.up:
                if man.isJump:
                    pygame.draw.circle(screen, (0,0,0),(self.x+13,self.y-22), 6)
                    screen.blit(diagonalLeft, (self.x+1,self.y-32))
                else:
                    pygame.draw.circle(screen, (0,0,0),(self.x+13,self.y-11), 6)
                    screen.blit(diagonalLeft, (self.x+3,self.y-22))
            else:
                pygame.draw.circle(screen, (0,0,0),(self.x+7,self.y+12), 6)
                screen.blit(projectileLeft, (self.x-2,self.y+5))
         

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 6
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.up = False
        self.walkCount = 0
        self.dyingCount = 0
        self.falling = False
        self.facing = "Right"
        self.shield = False
        self.isShoot = False
        self.hitpoints = 100
        self.dead = False
        self.hit = False
    
    def draw(self,screen):
        circle = pygame.Surface((86, 86), pygame.SRCALPHA)
        # Shield draw
        if self.shield == True:
            if self.facing == "Right":
                if self.right:
                    if man.isShoot:
                        pos = (self.x-9,self.y-19)
                    else:
                        pos = (self.x-11,self.y-19)
                else:
                    if man.isShoot:
                        pos = (self.x-16,self.y-19)
                    else:
                        pos = (self.x-20,self.y-19)
            if self.facing == "Left":
                if self.left:
                    if man.isShoot:
                        pos = (self.x-13,self.y-19)
                    else:
                        pos = (self.x-18,self.y-19)
                else:
                    if man.isShoot:
                        pos = (self.x-10,self.y-19)
                    else:
                        pos = (self.x-14,self.y-19)
            pygame.draw.circle(circle, LIGHTRED,(43,43), 43)
            screen.blit(circle, pos)
        if shieldLoop == 0:
            self.shield = False
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        # Hit animation
        if self.hit and not self.dead:
            if robotalive[1]:
                if hitloop[1] > 0:
                    if self.x < robot.x:
                        self.x -= 10
                        screen.blit(deadRight[0], (self.x, self.y-5))
                    else:
                        self.x += 10
                        screen.blit(deadLeft[0], (self.x, self.y-5))
            if robotalive[2]:
                if hitloop[2] > 0:
                    if self.x < robot2.x:
                        self.x -= 10
                        screen.blit(deadRight[0], (self.x, self.y-5))
                    else:
                        self.x += 10
                        screen.blit(deadLeft[0], (self.x, self.y-5))
        else:
            # Run Left
            if self.left and not self.falling:
                if self.isShoot:
                    if man.up:
                        screen.blit(runShootUpLeft[self.walkCount//3], (self.x,self.y-3))
                    else:
                        screen.blit(runShootLeft[self.walkCount//3], (self.x,self.y-3))
                    self.isShoot = False
                else:
                    screen.blit(walkLeft[self.walkCount//3], (self.x,self.y-3))           
                self.walkCount += 1
            # Run Right
            elif self.right and not self.falling:
                if self.isShoot:
                    if man.up:
                        screen.blit(runShootUpRight[self.walkCount//3], (self.x,self.y-3))
                    else:
                        screen.blit(runShootRight[self.walkCount//3], (self.x,self.y-3))
                    self.isShoot = False
                else:
                    screen.blit(walkRight[self.walkCount//3], (self.x,self.y-3))
                self.walkCount += 1
            # Stand Right
            elif self.facing == "Right" and not self.isJump and not self.dead:
                if self.isShoot:
                    if self.up:
                        screen.blit(UpRight, (self.x,self.y-4))
                        self.isShoot = False
                    else:
                        screen.blit(shootRight, (self.x,self.y-3))
                        self.isShoot = False                    
                else:
                    screen.blit(standRight, (self.x,self.y-4))
            # Stand Left
            elif self.facing == "Left" and not self.isJump and not self.dead:
                if self.isShoot:
                    if self.up:
                        screen.blit(UpLeft, (self.x,self.y-4))
                        self.isShoot = False
                    else:
                        screen.blit(shootLeft, (self.x,self.y-3))
                        self.isShoot = False                    
                else:
                    screen.blit(standLeft, (self.x,self.y-4))
            
            #Jump Animation
            if self.isJump:
                if not self.isShoot:
                    if self.facing == "Right":
                        if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                            screen.blit(jumpRight[0], (self.x,self.y))
                        elif 6 >= self.jumpCount > 4:
                            screen.blit(jumpRight[1], (self.x,self.y))
                        elif 4 >= self.jumpCount > 0:
                            screen.blit(jumpRight[2], (self.x,self.y))
                        else:
                            screen.blit(jumpRight[3], (self.x,self.y-15))
                    else:
                        if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                            screen.blit(jumpLeft[0], (self.x,self.y))
                        elif 6 >= self.jumpCount > 4:
                            screen.blit(jumpLeft[1], (self.x,self.y))
                        elif 4 >= self.jumpCount > 0:
                            screen.blit(jumpLeft[2], (self.x,self.y))
                        else:
                            screen.blit(jumpLeft[3], (self.x,self.y-15))
                else:
                    if not self.up:
                        if self.facing == "Right":
                            if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                                screen.blit(jumpShootRight[0], (self.x,self.y))
                            elif 6 >= self.jumpCount > 4:
                                screen.blit(jumpShootRight[1], (self.x,self.y))
                            elif 4 >= self.jumpCount > 0:
                                screen.blit(jumpShootRight[2], (self.x,self.y))
                            else:
                                screen.blit(jumpShootRight[3], (self.x,self.y-15))
                        else:
                            if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                                screen.blit(jumpShootLeft[0], (self.x,self.y))
                            elif 6 >= self.jumpCount > 4:
                                screen.blit(jumpShootLeft[1], (self.x,self.y))
                            elif 4 >= self.jumpCount > 0:
                                screen.blit(jumpShootLeft[2], (self.x,self.y))
                            else:
                                screen.blit(jumpShootLeft[3], (self.x,self.y-15))
                    else:
                        if self.facing == "Right":
                            if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                                screen.blit(jumpShootUpRight[0], (self.x,self.y))
                            elif 6 >= self.jumpCount > 4:
                                screen.blit(jumpShootUpRight[1], (self.x,self.y))
                            elif 4 >= self.jumpCount > 0:
                                screen.blit(jumpShootUpRight[2], (self.x,self.y))
                            else:
                                screen.blit(jumpShootUpRight[3], (self.x,self.y-15))
                        else:
                            if 10 >= self.jumpCount > 6 or -10 <= self.jumpCount < -9:
                                screen.blit(jumpShootUpLeft[0], (self.x,self.y))
                            elif 6 >= self.jumpCount > 4:
                                screen.blit(jumpShootUpLeft[1], (self.x,self.y))
                            elif 4 >= self.jumpCount > 0:
                                screen.blit(jumpShootUpLeft[2], (self.x,self.y))
                            else:
                                screen.blit(jumpShootUpLeft[3], (self.x,self.y-15))
        # Dead animation
        if self.dead:
            if self.facing == "Right":
                screen.blit(deadRight[1], (self.x,self.y+10))
            if self.facing == "Left":
                screen.blit(deadLeft[1], (self.x,self.y+10))


class Weapon():
    def __init__(self,x,y,id):
        self.x = x
        self.y = y
        self.rot = 0
        self.cannon = pygame.image.load(os.path.join('images','cannon.png'))
        self.rect = self.cannon.get_rect()
        self.hitpoints = 50
        self.id = id

    def draw(self):
        if self.hitpoints > 0:
            if man.x > self.x:
                self.rot = round(math.degrees(math.atan(abs(man.x+man.width/2-self.x)/(man.y-self.y))))
                self.target = pygame.transform.rotate(self.cannon, self.rot)
                screen.blit(self.target, (self.x, self.y - round(self.rot*0.07)))
            else:
                self.rot = -round(math.degrees(math.atan(abs(man.x+man.width/2-self.x)/(man.y-self.y))))
                self.target = pygame.transform.rotate(self.cannon, self.rot)
                screen.blit(self.target, (self.x + round(self.rot*0.3), self.y + round(self.rot*0.07)))
            # Weapon health bar
            if alive_dict[1]:
                pygame.draw.rect(screen,(255,0,0), (bg_x-489, 17, 50, 10))
                pygame.draw.rect(screen,(0,255,55), (bg_x-489, 17, weapon_dict[1].hitpoints, 10))
            if alive_dict[2]:
                pygame.draw.rect(screen,(255,0,0), (bg_x-1289, 17, 50, 10))
                pygame.draw.rect(screen,(0,255,55), (bg_x-1289, 17, weapon_dict[2].hitpoints, 10))
            if alive_dict[3]:
                pygame.draw.rect(screen,(255,0,0), (bg_x+911, 17, 50, 10))
                pygame.draw.rect(screen,(0,255,55), (bg_x+911, 17, weapon_dict[3].hitpoints, 10))
            if alive_dict[4]:
                pygame.draw.rect(screen,(255,0,0), (bg_x+1211, 17, 50, 10))
                pygame.draw.rect(screen,(0,255,55), (bg_x+1211, 17, weapon_dict[4].hitpoints, 10))
            if alive_dict[5]:
                pygame.draw.rect(screen,(255,0,0), (bg_x+1611, 17, 50, 10))
                pygame.draw.rect(screen,(0,255,55), (bg_x+1611, 17, weapon_dict[5].hitpoints, 10))


class Enemy():
    def __init__(self,x,y,width,height,id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id
        self.vel = 3
        self.direction = -1
        self.health = 300

    def moveleft(self):
        if 0 < eloop <= 10:
            screen.blit(enemyleft[1], (self.x,self.y-2))
        elif 10 < eloop <= 20:
            screen.blit(enemyleft[2], (self.x,self.y-4))
        elif 20 < eloop <= 30:
            screen.blit(enemyleft[3], (self.x,self.y-5))
        elif 30 < eloop <= 40:
            screen.blit(enemyleft[4], (self.x,self.y-4))
        elif 40 < eloop <= 50:
            screen.blit(enemyleft[5], (self.x,self.y-2))                
        elif 50 < eloop <= 60:
            screen.blit(enemyleft[6], (self.x,self.y-4))
        elif 60 < eloop <= 70:
            screen.blit(enemyleft[7], (self.x,self.y-5)) 
        elif 70 < eloop <= 80:
            screen.blit(enemyleft[8], (self.x,self.y-4))
        elif 80 < eloop <= 90:
            screen.blit(enemyleft[9], (self.x,self.y-2))
        elif 90 < eloop <= 92:
            screen.blit(punchleft[0], (self.x,self.y)) 
        elif 92 < eloop <= 94:
            screen.blit(punchleft[1], (self.x-30,self.y))
        elif 94 < eloop <= 96:
            screen.blit(punchleft[2], (self.x-40,self.y))
        elif 96 < eloop <= 98:
            screen.blit(punchleft[1], (self.x-30,self.y))
        elif 98 < eloop <= 101:
            screen.blit(enemyleft[10], (self.x,self.y))
        elif 101 < eloop <= 104:
            screen.blit(enemyleft[11], (self.x-1,self.y))
        elif 104 < eloop <= 107:
            screen.blit(enemyleft[12], (self.x-3,self.y+2))
        elif 107 < eloop <= 110:
            screen.blit(enemyleft[13], (self.x-9,self.y+2))
        elif 110 < eloop <= 200:
            screen.blit(enemyleft[0], (self.x,self.y))

    def moveright(self):
        if 0 < eloop <= 10:
            screen.blit(enemyright[1], (self.x,self.y-2))
        elif 10 < eloop <= 20:
            screen.blit(enemyright[2], (self.x,self.y-4))
        elif 20 < eloop <= 30:
            screen.blit(enemyright[3], (self.x,self.y-5))
        elif 30 < eloop <= 40:
            screen.blit(enemyright[4], (self.x,self.y-4))
        elif 40 < eloop <= 50:
            screen.blit(enemyright[5], (self.x,self.y-2))                
        elif 50 < eloop <= 60:
            screen.blit(enemyright[6], (self.x,self.y-4))
        elif 60 < eloop <= 70:
            screen.blit(enemyright[7], (self.x,self.y-5)) 
        elif 70 < eloop <= 80:
            screen.blit(enemyright[8], (self.x,self.y-4))
        elif 80 < eloop <= 90:
            screen.blit(enemyright[9], (self.x,self.y-2))
        elif 90 < eloop <= 92:
            screen.blit(punchright[0], (self.x,self.y)) 
        elif 92 < eloop <= 94:
            screen.blit(punchright[1], (self.x,self.y))
        elif 94 < eloop <= 96:
            screen.blit(punchright[2], (self.x,self.y))
        elif 96 < eloop <= 98:
            screen.blit(punchright[1], (self.x,self.y))
        elif 98 < eloop <= 101:
            screen.blit(enemyright[10], (self.x,self.y))
        elif 101 < eloop <= 104:
            screen.blit(enemyright[11], (self.x,self.y))
        elif 104< eloop <= 107:
            screen.blit(enemyright[12], (self.x,self.y))
        elif 107 < eloop <= 110:
            screen.blit(enemyright[13], (self.x,self.y))
        elif 110 < eloop <= 200:
            screen.blit(enemyright[0], (self.x,self.y))

    def draw(self):
        global eloop
        global endpoint
        global endloop
        if endpoint[1]:
            if self.id == 1:
                self.direction = 1
        if endpoint[2]:
            if self.id == 2:
                self.direction = -1
        if self.id == 1 and not endpoint[1]:
            if man.x < self.x:
                self.direction = -1
            else:
                self.direction = 1
        if self.id == 2 and not endpoint[2]:
            if man.x < self.x:
                self.direction = -1
            else:
                self.direction = 1
        
        if eloop == 0:
            eloop += 1
        if eloop > 200:
            eloop = 0
        if eloop < 90:
            self.x += round(self.vel * self.direction)

        if self.id == 1:
            if self.x - x_axis_reset >= -500 and not endpoint[1]:
                if self.direction == -1:
                    self.moveleft()
                else:
                    self.moveright()
            if self.x - x_axis_reset < -500:
                endpoint[1] = True
                endloop[1] = 1
            if endpoint[1]:
                self.moveright()
            if endloop[1] >= 1:
                endloop[1] += 1
            if endloop[1] > 300:
                endpoint[1] = False
                endloop[1] = 0

        if self.id == 2:
            if self.x - x_axis_reset <= -600 and not endpoint[2]:
                if self.direction == -1:
                    self.moveleft()
                else:
                    self.moveright()
            if self.x - x_axis_reset > -600:
                endpoint[2] = True
                endloop[2] = 1
            if endpoint[2]:
                self.moveleft()
            if endloop[2] >= 1:
                endloop[2] += 1
            if endloop[2] > 300:
                endpoint[2] = False
                endloop[2] = 0

        if robotalive[1]:
            if self.id == 1:
                pygame.draw.rect(screen,(255,0,0), (self.x-11, self.y - 23, round(300/3), 15))
                pygame.draw.rect(screen,(0,255,55), (self.x-11, self.y - 23, round(self.health/3), 15))
        if robotalive[2]:
            if self.id == 2:
                pygame.draw.rect(screen,(255,0,0), (self.x-11, self.y - 23, round(300/3), 15))
                pygame.draw.rect(screen,(0,255,55), (self.x-11, self.y - 23, round(self.health/3), 15))

def explode(explosionloop,temp,id):
    if explosionloop[id] >= 1:
        explosionloop[id] += 1
    if 1 < explosionloop[id] <= 3:
        screen.blit(explosion[0], (temp[id][0] - 2, temp[id][1]))
    elif 3 < explosionloop[id] <= 5:
        screen.blit(explosion[1], (temp[id][0] - 2, temp[id][1]))
    elif 5 < explosionloop[id] <= 7:
        screen.blit(explosion[2], (temp[id][0] - 2, temp[id][1]))
    elif 7 < explosionloop[id] <= 9:
        screen.blit(explosion[3], (temp[id][0] - 2, temp[id][1]))
    elif 9 < explosionloop[id] <= 11:
        screen.blit(explosion[4], (temp[id][0] - 2, temp[id][1]))
    elif 11 < explosionloop[id] <= 13:
        screen.blit(explosion[5], (temp[id][0] - 2, temp[id][1]))
    elif 13 < explosionloop[id] <= 15:
        screen.blit(explosion[6], (temp[id][0] - 2, temp[id][1]))
    elif 15 < explosionloop[id] <= 17:
        screen.blit(explosion[7], (temp[id][0] - 2, temp[id][1]))
    elif 17 < explosionloop[id] <= 19:
        screen.blit(explosion[8], (temp[id][0] - 2, temp[id][1]))
    if explosionloop[id] > 19:
        explosionloop[id] = 0


def redrawGameWindow():
    screen.blit(bg, (bg_x, bg_y))
    screen.blit(bg, (bg_x-900, bg_y))
    screen.blit(bg2, (bg_x+900, bg_y))
    screen.blit(bg, (bg_x-1800, bg_y))
    screen.blit(bg, (bg_x+1800, bg_y))
    screen.blit(land, (bg_x - 500, 0))
    screen.blit(land, (bg_x - 1300, 0))
    screen.blit(land, (bg_x + 900, 0))
    screen.blit(land, (bg_x + 1200, 0))
    screen.blit(land, (bg_x + 1600, 0))
    screen.blit(head, (720, 485))
    pygame.draw.rect(screen,(255,200,0), (756, 494, 100, 20))
    pygame.draw.rect(screen,(255,37,37), (756, 494, man.hitpoints, 20))
    text = font.render('Score: ' + str(score + weaponKillCount*50), 1, (255,0,0))
    for i in range(1,6):
        if alive_dict[i]:
            weapon_dict[i].draw()
    if man.falling:
        if man.facing == "Right":
            screen.blit(jumpRight[4], (man.x, man.y))
        else:
            screen.blit(jumpLeft[4], (man.x, man.y))
    else:
        man.draw(screen)
    if robotalive[1] == True:
        robot.draw()
    if robotalive[2] == True:
        robot2.draw()
    for ray in rays:
        ray.draw(screen)
    for i in range(1,6):
        for shot in shots_dict[i]:
            shot.draw(screen)
    explode(explosionloop,temp, 1)
    explode(explosionloop,temp, 2)
    screen.blit(text, (20,480))
    if man.dead:
        text2 = font2.render('GAME OVER', 1, (255,0,0))
        screen.blit(text2, (bg.get_width()/2-143,bg.get_height()/2-45))
    #if not start:
        #screen.blit(menu, (0, 0))   
    pygame.display.update()

# mainloop
font = pygame.font.SysFont('comicsans',30, True)
font2 = pygame.font.SysFont('comicsans',50, True)
rays = []
shots_dict = {1:[],2:[],3:[],4:[],5:[]}
shootLoop = 0
shieldLoop = 0
weaponLoop = {1:0,2:20,3:40,4:60,5:80}
man = Player(450,329,52,58)
robot = Enemy(650,287,76,100,1)
robot2 = Enemy(-1500,287,76,100,2)
robotalive = {1:True,2:True}
endpoint = {1:False,2:False}
endloop = {1:0,2:0}
explosionloop = {1:0,2:0}
temp = {1:[0,0],2:[0,0]}
weapon_dict = {1:0,2:0,3:0,4:0,5:0}
weapon_dict[1] = Weapon(bg_x-476,30,1)
weapon_dict[2] = Weapon(bg_x-1276,30,2)
weapon_dict[3] = Weapon(bg_x+924,30,3)
weapon_dict[4] = Weapon(bg_x+1224,30,4)
weapon_dict[5] = Weapon(bg_x+1624,30,5)
alive_dict = {1:True,2:True,3:True,4:True,5:True}
respawn_dict = {1:0,2:0,3:0,4:0,5:0}
weaponKillCount = 0
hitloop = {1:0,2:0}
eloop = 0
enemyrespawn = {1:0,2:0}
playerRespawn = 0
score = 0
x_axis_reset = 0
running = True


while running:
    clock.tick(27) 

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    if shieldLoop > 0:
        shieldLoop += 1
    if shieldLoop > 525:
        shieldLoop = 0

    # Weapon loop
    for i in range(1,6):
        if alive_dict[i]:
            if weaponLoop[i] == 0:
                if man.x >= weapon_dict[i].x:
                    if weapon_dict[i].rot < 30:
                        shots_dict[i].append(Shot(weapon_dict[i].x + weapon_dict[i].rot*0.7 + 7, weapon_dict[i].y + 29, weapon_dict[i].rot, "Right", i))
                        weaponLoop[i] = 1
                    else:
                        shots_dict[i].append(Shot(weapon_dict[i].x + weapon_dict[i].rot*0.7, weapon_dict[i].y + 29, weapon_dict[i].rot, "Right", i))
                        weaponLoop[i] = 1
                else:
                    if weapon_dict[i].rot > -30:
                        shots_dict[i].append(Shot(weapon_dict[i].x + 9, weapon_dict[i].y + 25, weapon_dict[i].rot, "Left",i))
                        weaponLoop[i] = 1
                    else:
                        shots_dict[i].append(Shot(weapon_dict[i].x, weapon_dict[i].y + 25, weapon_dict[i].rot, "Left",i))
                        weaponLoop[i] = 1
            if weaponLoop[i] > 0:
                weaponLoop[i] += 1
            if weaponLoop[i] > 100:
                weaponLoop[i] = 0
    

    # Shots list
    for i in range(1,6):
        for shot in shots_dict[i]:
            if alive_dict[i]:
                shot.shotmove()
            else:
                shot.shotmove()

    for i in range(1,6):
        if alive_dict[i]:
            if weapon_dict[i].hitpoints <= 0:
                del weapon_dict[i]
                alive_dict[i] = False
                weaponKillCount += 1

    # Cannon respawn
    if alive_dict[1] == False:
        respawn_dict[1] += 1
    if respawn_dict[1] > 100:
        alive_dict[1] = True
        respawn_dict[1] =0
        weapon_dict[1] = Weapon(bg_x-476,30,1)
    if alive_dict[2] == False:
        respawn_dict[2] += 1
    if respawn_dict[2] > 300:
        alive_dict[2] = True
        respawn_dict[2] =0
        weapon_dict[2] = Weapon(bg_x-1276,30,2)
    if alive_dict[3] == False:
        respawn_dict[3] += 1
    if respawn_dict[3] > 100:
        alive_dict[3] = True
        respawn_dict[3] =0
        weapon_dict[3] = Weapon(bg_x+924,30,3)
    if alive_dict[4] == False:
        respawn_dict[4] += 1
    if respawn_dict[4] > 300:
        alive_dict[4] = True
        respawn_dict[4] =0
        weapon_dict[4] = Weapon(bg_x+1224,30,4)
    if alive_dict[5] == False:
        respawn_dict[5] += 1
    if respawn_dict[5] > 100:
        alive_dict[5] = True
        respawn_dict[5] =0
        weapon_dict[5] = Weapon(bg_x+1624,30,5)    

    # Enemy loop
    if eloop >= 0:
        eloop += 1
    if eloop > 200:
        eloop = 0
    if robotalive[1] == True:
        if robot.health <= 0:
            seismiccharge.play()
            temp[1][0] = robot.x
            temp[1][1] = robot.y
            explosionloop[1] = 1
            robotalive[1] = False
            del robot
            score += 200
            endpoint[1] = False
    if robotalive[2] == True:
        if robot2.health <= 0:
            seismiccharge.play()
            temp[2][0] = robot2.x
            temp[2][1] = robot2.y
            explosionloop[2] = 1
            robotalive[2] = False
            del robot2
            score += 200
            endpoint[2] = False

    if robotalive[1] == False:
        enemyrespawn[1] += 1
    if enemyrespawn[1] > 100:
        robotalive[1] = True
        enemyrespawn[1] = 0
        robot = Enemy(bg_x+650,287,76,100,1)
        endloop[1] = 0

    if robotalive[2] == False:
        enemyrespawn[2] += 1
    if enemyrespawn[2] > 100:
        robotalive[2] = True
        enemyrespawn[2] = 0
        robot2 = Enemy(bg_x-1500,287,76,100,2)
        endloop[2] = 0


    # Player hit loop
    if hitloop[1] >= 1:
        hitloop[1] += 1
    if hitloop[1] == 3:
        man.hitpoints -= 10
    if hitloop[1] > 7:
        hitloop[1] = 0
        man.hit = False

    if hitloop[2] >= 1:
        hitloop[2] += 1
    if hitloop[2] == 3:
        man.hitpoints -= 10
    if hitloop[2] > 7:
        hitloop[2] = 0
        man.hit = False

    if man.hit == False and robotalive[1] == True:
        if man.x < robot.x:
            if 92 < eloop <= 98:
                if abs(man.x + man.width/2 - robot.x) <= 30 and man.y >= 287:
                    man.hit = True
                    hitloop[1] = 1
            else:
                if abs(man.x + man.width/2 - robot.x) <= 5 and man.y >= 287:
                    man.hit = True
                    hitloop[1] = 1
        else:
            if 92 < eloop <= 98:
                if abs(man.x + man.width/2 - robot.x - robot.width) <= 30 and man.y >= 287:
                    man.hit = True
                    hitloop[1] = 1
            else:
                if abs(man.x + man.width/2 - robot.x - robot.width) <= 5 and man.y >= 287:
                    man.hit = True
                    hitloop[1] = 1

    if man.hit == False and robotalive[2] == True:
        if man.x < robot2.x:
            if 92 < eloop <= 98:
                if abs(man.x + man.width/2 - robot2.x) <= 30 and man.y >= 287:
                    man.hit = True
                    hitloop[2] = 1
            else:
                if abs(man.x + man.width/2 - robot2.x) <= 5 and man.y >= 287:
                    man.hit = True
                    hitloop[2] = 1
        else:
            if 92 < eloop <= 98:
                if abs(man.x + man.width/2 - robot2.x - robot2.width) <= 30 and man.y >= 287:
                    man.hit = True
                    hitloop[2] = 1
            else:
                if abs(man.x + man.width/2 - robot2.x - robot2.width) <= 5 and man.y >= 287:
                    man.hit = True
                    hitloop[2] = 1          

    # Hole
    if bg_x+1452 < man.x < bg_x+1542 and not man.isJump:
        man.y += gravity
        man.falling = True
    if robotalive[1] == True:
        if 1439 < robot.x - x_axis_reset < 1542:
            robot.y += gravity
            if robot.y > 540:
                robotalive[1] = False
                del robot
                score += 200

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Rays list
    for ray in rays.copy():
        if ray.x < 900 and ray.x > 0 and ray.y > 0:
            if ray.up:
                ray.x += ray.vel * ray.facing
                ray.y -= ray.vel
            else:
                ray.x += ray.vel * ray.facing
            if alive_dict[1]:
                if ray.x > weapon_dict[1].x and ray.x < weapon_dict[1].x + 23:
                    if ray.y > weapon_dict[1].y and ray.y < weapon_dict[1].y + 36:
                        blast.play()
                        weapon_dict[1].hitpoints -= 10
                        score += 10
                        rays.remove(ray)
            if alive_dict[2]:
                if ray.x > weapon_dict[2].x and ray.x < weapon_dict[2].x + 23:
                    if ray.y > weapon_dict[2].y and ray.y < weapon_dict[2].y + 36:
                        blast.play()
                        weapon_dict[2].hitpoints -= 10
                        score += 10
                        rays.remove(ray)
            if alive_dict[3]:
                if ray.x > weapon_dict[3].x and ray.x < weapon_dict[3].x + 23:
                    if ray.y > weapon_dict[3].y and ray.y < weapon_dict[3].y + 36:
                        blast.play()
                        weapon_dict[3].hitpoints -= 10
                        score += 10
                        rays.remove(ray)
            if alive_dict[4]:
                if ray.x > weapon_dict[4].x and ray.x < weapon_dict[4].x + 23:
                    if ray.y > weapon_dict[4].y and ray.y < weapon_dict[4].y + 36:
                        blast.play()
                        weapon_dict[4].hitpoints -= 10
                        score += 10
                        rays.remove(ray)
            if alive_dict[5]:
                if ray.x > weapon_dict[5].x and ray.x < weapon_dict[5].x + 23:
                    if ray.y > weapon_dict[5].y and ray.y < weapon_dict[5].y + 36:
                        blast.play()
                        weapon_dict[5].hitpoints -= 10
                        score += 10
                        rays.remove(ray)
            if robotalive[1] == True:
                if ray.x > robot.x and ray.x < robot.x + robot.width:
                    if ray.y > 267:
                        blast.play()
                        robot.health -= 10
                        score += 10
                        rays.remove(ray)   
            if robotalive[2] == True:
                if ray.x > robot2.x and ray.x < robot2.x + robot2.width:
                    if ray.y > 267:
                        blast.play()
                        robot2.health -= 10
                        score += 10
                        rays.remove(ray)       
        else:
            rays.pop(rays.index(ray))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > 5*man.width and not man.falling and not man.dead:
        if keys[pygame.K_LCTRL]:
            man.x -= round(man.vel*1.8)
        else:
            man.x -= man.vel
        man.left = True
        man.right = False
        man.facing = "Left"
        for ray in rays:
            if len(rays) > 0:
                ray.vel = 22
    elif keys[pygame.K_RIGHT] and man.x < 900 - 6*man.width and not man.falling and not man.dead:
        if keys[pygame.K_LCTRL]:
            man.x += round(man.vel*1.8)
        else:
            man.x += man.vel
        man.left = False
        man.right = True
        man.facing = "Right"
        for ray in rays:
            if len(rays) > 0:
                ray.vel = 22
    elif keys[pygame.K_LEFT] and man.x <= 5*man.width and not man.falling and not man.dead:
        if bg_x < 1800 - man.width:
            if keys[pygame.K_LCTRL]:
                bg_x += round(man.vel*1.8)
                if robotalive[1] == True:
                    robot.x += round(man.vel*1.8)
                if robotalive[2] == True:
                    robot2.x += round(man.vel*1.8)
                x_axis_reset += round(man.vel*1.8)
                for i in range(1,6):
                    if alive_dict[i]:
                        weapon_dict[i].x += round(man.vel*1.8)
                for i in range(1,6):
                    for shot in shots_dict[i].copy():
                        shot.x += round(man.vel*1.8)
                if len(rays)>0:
                    for ray in rays:
                        if ray.facing == 1:
                            ray.vel = 34
                        else:
                            ray.vel = 10
            else:
                bg_x += man.vel
                if robotalive[1] == True:
                    robot.x += man.vel
                if robotalive[2] == True:
                    robot2.x += man.vel
                x_axis_reset += man.vel
                for i in range(1,6):
                    if alive_dict[i]:
                        weapon_dict[i].x += man.vel
                for i in range(1,6):
                    for shot in shots_dict[i].copy():
                        shot.x += man.vel
                if len(rays)>0:
                    for ray in rays:
                        if ray.facing == 1:
                            ray.vel = 28
                        else:
                            ray.vel = 16
        man.left = True
        man.right = False
        man.facing = "Left"
    elif keys[pygame.K_RIGHT] and man.x > 900 - man.width- 6*man.width and not man.falling and not man.dead:
        if bg_x + 1800 > man.vel:
            if keys[pygame.K_LCTRL]:
                bg_x -=  round(man.vel*1.8)
                if robotalive[1] == True:
                    robot.x -=  round(man.vel*1.8)
                if robotalive[2] == True:
                    robot2.x -=  round(man.vel*1.8)
                x_axis_reset -=  round(man.vel*1.8)
                for i in range(1,6):
                    if alive_dict[i]:
                        weapon_dict[i].x -= round(man.vel*1.8)
                for i in range(1,6):
                    for shot in shots_dict[i].copy():
                        shot.x -= round(man.vel*1.8)
                if len(rays)>0:
                    for ray in rays:
                        if ray.facing == 1:
                            ray.vel = 10
                        else:
                            ray.vel = 34
            else:
                bg_x -= man.vel
                if robotalive[1] == True:
                    robot.x -= man.vel
                if robotalive[2] == True:
                    robot2.x -= man.vel
                x_axis_reset -= man.vel
                for i in range(1,6):
                    if alive_dict[i]:
                        weapon_dict[i].x -= man.vel
                for i in range(1,6):
                    for shot in shots_dict[i].copy():
                        shot.x -= man.vel
                if len(rays)>0:
                    for ray in rays:
                        if ray.facing == 1:
                            ray.vel = 16
                        else:
                            ray.vel = 28
        man.left = False
        man.right = True
        man.facing = "Right"
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
        for ray in rays:
            if len(rays) > 0:
                ray.vel = 22

    if keys[pygame.K_LALT] and not man.dead:
        shieldSound.play()
        man.shield = True
        shieldLoop = 1
    
    # Rays list
    if keys[pygame.K_z] and shootLoop == 0 and not man.dead:
        if len(rays) < 5:
            beam.play()
            if man.facing == "Right":
                rays.append(projectile(man.x + man.width + 3, man.y + 13, 1, man.up))
            else:
                rays.append(projectile(man.x - 18, man.y + 13, -1, man.up))
        shootLoop = 1
    
    if keys[pygame.K_z] and not man.dead:
        man.isShoot = True
    
    if keys[pygame.K_UP] and not man.dead:
        man.up = True

    if not keys[pygame.K_UP] and not man.dead:
        man.up = False

    if keys[pygame.K_s]:
        start = True

    if not man.dead:   
        if not(man.isJump):
            if keys[pygame.K_SPACE] and not man.falling:
                man.isJump = True
                man.left = False
                man.right = False
        else:
            man.left = False
            man.right = False
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.4 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
    
    if man.hitpoints <= 0 or man.falling:
        man.dead = True
        playerRespawn += 1
        alive_dict = {1:False,2:False,3:False,4:False,5:False}
        man.shield = False
        pygame.mixer.stop()
    if playerRespawn > 100:
        man.falling = False
        man.dead = False
        playerRespawn =0
        bg_x -= x_axis_reset
        man.x = 450
        man.y = 329
        weapon_dict[1].x -= x_axis_reset
        weapon_dict[2].x -= x_axis_reset
        weapon_dict[3].x -= x_axis_reset 
        weapon_dict[4].x -= x_axis_reset 
        weapon_dict[5].x -= x_axis_reset
        man.hitpoints = 100
        weaponKillCount = 0
        x_axis_reset = 0
        alive_dict = {1:True,2:True,3:True,4:True,5:True}
        score = 0
        robotalive[1] = False
        del robot
        enemyrespawn[1] = 99
        robotalive[2] = False
        del robot2
        enemyrespawn[2] = 99

    redrawGameWindow()

pygame.quit()