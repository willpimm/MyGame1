import pygame,time, random, pygame.gfxdraw
pygame.init()

"""
            while self.safe:
                collision = pygame.sprite.spritecollide(self.player,self.all_enemies,False)
                if collision:
                    self.safe = False
                else:
                    self.safe = True
                    #zombie.rect.x = screen.player.rect.
"""
class Entity: # Parent class
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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
        if player.rect.x > self.rect.x:
            self.rect.x+=1
        else:
            self.rect.x-=1
        if player.rect.y > self.rect.y:
            self.rect.y+=1
        else:
            self.rect.y-=1

# The following class is a subclass to entity which creates the player object
class Player(Entity, pygame.sprite.Sprite): # sub-class to Entity
    SPEED = 5
    def __init__(self,x,y):
        #super().__init__(x,y,width,height)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((153,50,204))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moving_x = 0
        self.moving_y = 0
        self.pos_x = 0
        self.pos_y = 0

    def move(self,x,y):
        if player.moving_y == -1 and self.rect.y>0:
            player.rect.y -=10
            self.pos_y +=self.SPEED
        if player.moving_y == 1 and self.rect.y < 490:
            player.rect.y +=10
            self.pos_y += self.SPEED
        if player.moving_x == -1 and self.rect.x>0:
            player.rect.x -=10
            self.pos_x -= self.SPEED
        if player.moving_x == 1 and self.rect.x<990:
            player.rect.x +=10
            self.pos_x +=self.SPEED

    def shoot(self, x_move, y_move):
        bullets.add(Bullet(self.rect.x, self.rect.y, x_move, y_move))

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

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

def inputs(): # added if not line, to handle releases
    btn = pygame.key.get_pressed()
    if btn[pygame.K_LEFT]:
        player.moving_x = -1
    if btn[pygame.K_RIGHT]:
        player.moving_x = 1
    if not btn[pygame.K_RIGHT] and not btn[pygame.K_LEFT]:
        player.moving_x = 0
    if btn[pygame.K_UP]:
        player.moving_y = -1
    if btn[pygame.K_DOWN]:
        player.moving_y = 1
    if not btn[pygame.K_UP] and not btn[pygame.K_DOWN]:
        player.moving_y = 0
    if btn[pygame.K_SPACE]:
        pass

def draw():
    display.fill((0,0,0,0))
    users.draw(display)
    bullets.draw(display)
    all_enemies.draw(display)
    pygame.display.flip()

def __main__():
    global player, users, all_enemies, bullets, display, running
    player = Player(480,220)
    users = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    display = pygame.display.set_mode((1000,500))
    running = True
    users.add(player)
    pygame.display.set_caption("MyGame")

    shoot_up, shoot_left, shoot_down, shoot_right = 0, 0, 0, 0

    for z in range(10):
        all_enemies.add(Zombie())

    while running:
        time.sleep(0.01)
        inputs()
        player.move(0,0)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: shoot_up = 1
                elif event.key == pygame.K_a: shoot_left = 1
                elif event.key == pygame.K_s: shoot_down = 1
                elif event.key == pygame.K_d: shoot_right = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w: shoot_up = 0
                elif event.key == pygame.K_a: shoot_left = 0
                elif event.key == pygame.K_s: shoot_down = 0
                elif event.key == pygame.K_d: shoot_right = 0

        shoot_x_move = shoot_right - shoot_left
        shoot_y_move = shoot_up - shoot_down
        if shoot_x_move or shoot_y_move:
            player.shoot(shoot_x_move, shoot_y_move)


        for bullet in bullets.sprites():
            bullet.update()

        for zombie in all_enemies.sprites():
            zombie.move()
