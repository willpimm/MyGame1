import pygame,time, random, pygame.gfxdraw

class Setup:
    def __init__(self,width,height):
        pygame.init()
        self.player = Player(480,220,10,20)
        self.users = pygame.sprite.Group()
        self.users.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((1000,500))
        pygame.display.set_caption("MyGame")
        self.safe = True
        self.running = True

        for z in range(10):
            self.all_enemies.add(Zombie())

    def play(self):
        while self.running:
            time.sleep(0.01)
            self.player.move()
            self.draw()
            self.player.events()

            for bullet in self.bullets.sprites():
                bullet.move()

            for zombie in self.all_enemies.sprites():
                zombie.move()

                """
                while self.safe:
                    collision = pygame.sprite.spritecollide(self.player,self.all_enemies,False)
                    if collision:
                        self.safe = False
                    else:
                        self.safe = True
                        #zombie.rect.x = screen.player.rect.
"""
    def draw(self):
        self.display.fill((0,0,0,0))
        self.users.draw(self.display)
        self.bullets.draw(self.display)
        self.all_enemies.draw(self.display)
        pygame.display.flip()

class Entity: # Parent class
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        #self.health = health

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((124,252,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1000)
        self.rect.y = random.randint(0,500)
        self.display = pygame.display.set_mode((1000,500))

    def move(self):
        if screen.player.rect.x > self.rect.x:
            self.rect.x+=1
        else:
            self.rect.x-=1
        if screen.player.rect.y > self.rect.y:
            self.rect.y+=1
        else:
            self.rect.y-=1

# The following class is a subclass to entity which creates the player object
class Player(Entity, pygame.sprite.Sprite): # sub-class to Entity
    SPEED = 5

    def __init__(self,x,y,width,height):
        #super().__init__(x,y,width,height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((153,50,204))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def move(self):
        self.vel_x = 0
        self.vel_y = 0
        btn = pygame.key.get_pressed()
        if btn[pygame.K_LEFT] and self.rect.x>0:
            self.left = True
            self.vel_x -= self.SPEED
        if btn[pygame.K_RIGHT] and self.rect.x<990:
            self.right = True
            self.vel_x += self.SPEED
        if btn[pygame.K_UP] and self.rect.y>0:
            self.up = True
            self.vel_y -= self.SPEED
        if btn[pygame.K_DOWN] and self.rect.y<480:
            self.down = True
            self.vel_y += self.SPEED
        if btn[pygame.K_SPACE]:
            self.fire()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def fire(self):
        x_mult = self.vel_x / self.SPEED
        y_mult = self.vel_y / self.SPEED
        screen.bullets.add(Bullet(self.rect.x, self.rect.y, x_mult, y_mult))
        #divides players x and y velo by speed, returning 1 if player is moving in a positive direction and -1 if negative
        #this allows them the bullet to multiply by it's speed

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

class Bullet(Entity,pygame.sprite.Sprite):
    SPEED = 10 #speed constant, same for every bullet

    def __init__(self,x, y, x_move, y_move):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__(x,y,width,height)
        self.image = pygame.Surface((10,10),pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.image, 10, 10, 14, (153,50,204))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = self.SPEED * x_move
        self.vel_y = self.SPEED * y_move

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

def __main__():
    global screen
    screen = Setup(1000,500)
    screen.play()
