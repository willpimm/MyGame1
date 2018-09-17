import pygame,time
from enum import Enum

class Setup:
    def __init__(self,width,height):
        pygame.init()
        self.player = Player(480,220,10,20)
        self.users = pygame.sprite.Group()
        self.users.add(self.player)
        self.width = width
        self.height = height
        pygame.display.set_caption("MyGame")
        self.running = True
        self.play()
        self.screen = Setup(1000,500)

    def play(self):
        print("3")
        while self.running:
            self.player.press()
            self.draw()


    def draw(self):
        self.screen.fill((0,0,0,0))
        self.users.draw(screen)
        self.users.update()
        self.screen.flip()


class Entity(): # Parent class
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #self.health = health

class Zombie(Entity): # sub-class to Entity
    def __init__(self,x,y,width,height,health):
        super().__init__(x,y,width,height,health)

    def draw_zombie(self):
        pass

    def move(self):
        if player.x > zombie.x:
            zombie.x+=1
        else:
            player.x-=1
        if player.y > zombie.y:
            zombie.y+=1
        else:
            zombie.y-=1

class Direction(Enum):
    N = (0,-1)
    S = (0,1)
    E = (1,0)
    W = (-1,0)
    NE = (-0.5,0.5)
    NW = (-0.5,-0.5)
    SE = (0.5,0.5)
    SW = (0.5,-0.5)

# The following class is a subclass to entity which creates the player object
class Player(Entity, pygame.sprite.Sprite): # sub-class to Entity

    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((153,50,204))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.press()

    def press(self):
        self.velx = 0
        btn = pygame.key.get_pressed()
        if btn[pygame.K_LEFT]:
            self.vel_x = -5
        if btn[pygame.K_RIGHT]:
            self.vel_x = 5

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def fire(self):
        raise NotImplementedError
"""
    def draw_player(self):
        pygame.display.set_mode((1000,500)).fill(pygame.Color(0,0,0,0))
        self.rect = self.image.get_rect()
        pygame.display.flip()



    def movex(self):
        if self.left:
            player.x-= 5
            self.draw_player()
            release()
        if not self.left:

        else:
            print("3")
            self.x +=5
            self.draw_player()


    def movey(self):
        if self.up:
            self.y-=5
        if self.down:
            self.y+=5
        self.draw_player()
"""

class Bullet(Player):
    def __init__(self,up,down,left,right,size):
        #super().__init__()
        self.size = size

    def draw_bullet(self):
        pass
        #raise NotImplementedError
        #pygame.draw.circle(pygame.display.set_mode((screen.width,screen.height)),[105,105,105],(bullet.x,bullet.y), 8)

#This class will...
class Board():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        pygame.display.set_caption("MyGame")


# event is a FIFO queue. Empties event queue and handles quit event. get() removes the first event in the queue
"""
class Game():
        def __init__():


def press():
    vector = pygame.math.Vector2
    btn = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left = True
                player.movex()
            if event.key == pygame.K_RIGHT:
                player.right = True
                player.movex()
            if event.key == pygame.K_UP:
                player.up = True
                player.movey()
            if event.key == pygame.K_DOWN:
                player.down = True
                player.movey()

#def release():
#    if btn[pygame.K_LEFT]:
"""
def __main__():
    global screen
    screen = Setup(1000,500)
    screen.draw()
    Setup()
