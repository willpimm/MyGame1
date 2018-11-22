import pygame,time, random, pygame.gfxdraw
pygame.init()

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

def detectCollision():
    collide = True
    while collide:
        collision = pygame.sprite.spritecollide(self.player,self.all_enemies,False)
        if collision:
            self.collide = False
        else:
            self.collide = True
            #zombie.rect.x = screen.player.rect.

# The following class is a subclass to entity which creates the player object
class Player(pygame.sprite.Sprite):
    SPEED = 5
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((153,50,204))
        self.rect = self.image.get_rect()
        self.moving_x = 0
        self.moving_y = 0
        self.x_direction = 0
        self.y_direction = 0

    def move_up(self):
        if self.y_direction == -1:
            if self.rect.y>0: self.rect.y -=self.SPEED

    def move_down(self):
        if self.y_direction == 1:
            if self.rect.y< 490: self.rect.y +=self.SPEED

    def move_left(self):
        if self.x_direction == -1:
            if self.rect.x>0: self.rect.x -= self.SPEED

    def move_right(self):
        if self.x_direction == 1:
            if self.rect.x<990: self.rect.x +=self.SPEED

    def shoot(self, x_move, y_move):
        bullets.add(Bullet(self.rect.x, self.rect.y, x_move, y_move))

class Bullet(pygame.sprite.Sprite):
    SPEED = 10 #speed constant, same for every bullet
    def __init__(self,x, y, x_move, y_move):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,10),pygame.SRCALPHA)
        pygame.gfxdraw.filled_circle(self.image, 10, 10, 14, (153,50,204))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = self.SPEED * x_move
        self.vel_y = self.SPEED * y_move

    def update(self):
        shoot_x_move = shoot_right - shoot_left
        print(shoot_x_move)
        shoot_y_move = shoot_down - shoot_up
        if shoot_x_move or shoot_y_move:
            player.shoot(shoot_x_move, shoot_y_move)
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

def draw():
    display.fill((0,0,0,0))
    users.draw(display)
    bullets.draw(display)
    all_enemies.draw(display)
    pygame.display.flip()

def get_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False, pygame.quit()
        if event.type == pygame.KEYDOWN: handle_keydown(event.key)
        if event.type == pygame.KEYUP: handle_keyup(event.key)

def handle_keydown(key):
    if key == pygame.K_UP: player.y_direction = -1
    elif key == pygame.K_DOWN: player.y_direction = 1
    elif key == pygame.K_LEFT: player.x_direction = -1
    elif key == pygame.K_RIGHT: player.x_direction = 1
    if key == pygame.K_w: pass
    if key == pygame.K_a: pass
    if key == pygame.K_s: pass
    if key == pygame.K_d: pass

def handle_keyup(key):
    if key == pygame.K_UP: player.y_direction = 0
    if key == pygame.K_DOWN: player.y_direction = 0
    if key == pygame.K_LEFT: player.x_direction = 0
    if key == pygame.K_RIGHT: player.x_direction = 0
    if key == pygame.K_w: pass
    elif key == pygame.K_a: pass
    elif key == pygame.K_s: pass
    elif key == pygame.K_d: pass


class Game():
    def __init__(self):
        self.users = pygame.sprite.Group()
        self.users.add(player)
        
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
        get_events()
        player.move_up()
        player.move_down()
        player.move_left()
        player.move_right()
        draw()

        for bullet in bullets.sprites():
            bullet.update()

        for zombie in all_enemies.sprites():
            zombie.move()
