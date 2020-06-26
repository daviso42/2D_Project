
import pygame as pg
from Picture_Color import *
from Sounds import *
pg.init()

keys = pg.key.get_pressed()

class player(object):
      '''
      UserS
      '''
      def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.hitbox = (self.x +20 , self.y, 40, 64)
            self.vel = 4
            self.svel = 6
            self.dvel = 2
            self.isJump = False
            self.isSJump = False
            self.jumpCount = 10
            self.isDuck = False
            self.right = False
            self.left = False
            self.standing = True
            self.sprint = False
            self.fire = False
            self.eatSlugs = False
            
      def draw(self,window):
            if self.right:
                  window.blit(char_R, (self.x,self.y))
            else:
                  window.blit(char_L, (self.x,self.y))
            self.hitbox = (self.x +20 , self.y, 40, 64)
            pg.draw.rect(window, RED, self.hitbox, 2)

class proj(object):
      '''
      Shooting items
      '''
      def __init__ (self,x,y,width,height,color,facing):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.facing = facing
            self.vel = 10 * facing
            self.slugCount = 30
            self.slugDelay = 0
            self.hitbox = (self.x, self.y, self.width, self.height)
            self.skip = False

      def draw(self,win, weapon):
            if weapon == 'Chicken Leg':
                  if self.facing == 1:                  
                        win.blit(chklg_R, (self.x,self.y))
                  else:
                        win.blit(chklg_L, (self.x,self.y))
            else:
                  if self.facing ==1:
                        win.blit(Slug, (self.x,self.y))
                  else:
                        win.blit(Slug, (self.x,self.y))
            self.hitbox = (self.x, self.y, self.width, self.height)
            pg.draw.rect(win, GREEN, self.hitbox, 2)



class bad(object):
      def __init__ (self, x, y, width, height, right):
            self.x = x
            self.y = y
            self.yinit = y
            self.width = width
            self.height = height
            self.health = 2
            #self.path = path
            #self.end = end
            self.right = False
            self.moving = 1
            self.vel = 4
            self.hitbox = (self.x + 15  , self.y-5, 30, 40)

      def move(self, move, edge, standing, vel):
            # Get enemies to move with the background
            #spawn = [0,edge-self.width]
            #choice = []
            
            if self.right and self.x < edge - self.width and standing:
                  self.x += self.vel 
            elif self.right and self.x < edge - self.width: 
                  self.x += -(self.vel*move) + vel
            elif self.right:
                  self.right = False
            if not self.right and self.x > 0 + self.width and standing:
                  self.x -= self.vel 
            elif not self.right and self.x > 0 + self.width:
                  self.x -= (self.vel*move) + vel
            
            elif not self.right:
                  self.right = True
            '''
            if self.x > 0 and self.x + self.width < edge-10:
                  self.x -= self.vel * move
            else:
                  for val in spawn:
                        choice.append(abs(val-self.x))
                  self.x = spawn[choice.index(max(choice))] - 1
            '''      
            

      def draw(self, win, enemy):
            if enemy == 'ghost':
                  if not self.right:
                        win.blit(Ghost_L , (self.x,self.y))
                        self.moving = -1
                  else:
                        win.blit(Ghost_R , (self.x,self.y))
                        self.moving = 1
            self.hitbox = (self.x+15  , self.y-5, 30, 40)
            pg.draw.rect(window, RED, self.hitbox, 2)

class background:
      def __init__(self,image, x, y, width, height, facing):
            self.image = image
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.facing = facing
            self.vel = 5
            self.dvel = 2
            self.svel =7
            #self.count = 0

      def move(self):
            if self.facing == 1:
                  self.x -= self.vel
            if self.facing == -1:
                  if self.x <= 0:
                        self.x += self.vel
            #if self.x + self.width 
            #window = pg.display.set_mode((set_width,set_height))
      def draw(self,win, image):
            win.blit(image, (self.x, self.y))

      

def sin(x,y):
      y = round(mth.sin(x))
      return y


def redraw(window):
      # Redraw the screen every time
      #window.blit(sbackground, (back.x,back.y))
      for bkg in backgroundlst:
            bkg.draw(window, sbackground)
      guy.draw(window)

      #enemy.draw(window, 'ghost')
      for bullet in bullets:
            bullet.draw(window, 'Chicken Leg')
      for slug in slugs:
            slug.draw(window,'Slug')
      for badguy in bad_guys:
            badguy.draw(window, 'ghost')
      pg.draw.line(sbackground,WHITE,(0,ground),(set_width,ground))
      pg.display.update()      
      

def check_hitbox(box1, box2, facing, lst, index):
    # checks hitboxes for all enemies and projectiles  
      if facing == 1:
            if (box1[0] + box1[2] >= box2[0] and box1[0] + box1[2] <= box2[0] + box2[2]) and (box1[1] + box1[3] >= box2[1] and box1[1] <= box2[1] + box2[3]):
                  hit_sound.play()
                  lst.pop(index)
                  return True
                  
            else:
                  return False
      if facing == -1:
            if (box1[0] >= box2[0] and box1[0] <= box2[0] + box2[2]) and (box1[1] + box1[3] >= box2[1] and box1[1] <= box2[1] + box2[3]):
                  hit_sound.play()
                  lst.pop(index)
                  return True
                  
            else:
                  return False

def check_speed(standing, sprint, duck, player_move, enemy_move):
      if standing:
            return 0
      elif duck and not standing and (player_move == enemy_move):
            return back.svel
      elif sprint and not standing and (player_move == enemy_move):
            return back.dvel
      else:
            return back.vel
      
#def check_standing(                       


guy = player(500, ground-64, 64, 64)
guy.draw(window)
# enemy = bad(900, ground - 65, 55,30,False)
back = background(sbackground, 0, 0, set_width, set_height,1)
bullets = []
slugs = []
bad_guys = []
backgroundlst =[back]






