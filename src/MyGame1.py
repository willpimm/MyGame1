import pygame,time

class Entity(): # Parent class
    def __init__(self,x,y,width,height,health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health

class Zombie(Entity): # sub-class to Entity
    def __init__(self,x,y,width,height,health):
        super().__init__(x,y,width,height,health)

    def move():
        if you.x > zombie.x:
            zombie.x+=1
        else:
            zombie.x-=1
        if you.y > zombie.y:
            zombie.y+=1
        else:
            zombie.y-=1

class Player(Entity): # sub-class to Entity
    def __init__(self,x,y,width,height,health):
        super().__init__(x,y,width,height,health)
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def inputt():
        running = True
        while running:
            btn = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if btn[pygame.K_LEFT] and you.x>0:
                you.x -=0.126
                you.left = True
            if btn[pygame.K_RIGHT] and you.x <960:
                you.x+=0.125
                you.right = True
            if btn[pygame.K_UP] and you.y>0:
                you.y -=0.125 # Because co-ordinates have origin top left in python
                you.up = True
            if btn[pygame.K_DOWN] and you.y<440:
                you.y+=0.125
                you.down = True
            if btn[pygame.K_SPACE]:
                Bullet.direction()
            Screen.draw()

class Bullet(Player):
    def __init__(self,up,down,left,right,size):
        self.size = size
        self.x = x

    def direction(self):
        if you.up == True:
            print("hi")
        if you.down == True:
            bullet.direction == down
        if you.left == True:
            bullet.direction == left
        if you.right == True:
            bullet.direction == right

class Screen():
    def __init__(self):
        self.width = 1000
        self.height = 500

    def draw():
        board.fill(pygame.Color(0,0,0,0))
        pygame.draw.rect(board,[153,50,204],[you.x,you.y,you.width,you.height])
        pygame.draw.circle(board,[105,105,105],(bullet.x,bullet.y), 8)
        pygame.display.flip()

    def display():
        pygame.display.set_caption("MyGame")
        Player.inputt()


def __main__():
    pygame.init()

    board = pygame.display.set_mode((1000,500))
    you = Player(480,220,40,60,100,10)
    Screen.display()
    pygame.quit()
