import pygame,time

class Setup:
    def __init__(self,width,height):
        pygame.init()
        self.player = Player(480,220,10,20)
        self.users = pygame.sprite.Group()
        self.users.add(self.player)
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((1000,500))
        pygame.display.set_caption("MyGame")
        self.running = True

    def play(self):
        while self.running:
            time.sleep(0.01)
            self.player.move()
            self.draw()
            events()

    def draw(self):
        self.display.fill((0,0,0,0))
        self.users.draw(self.display)
        pygame.display.flip()

class Entity: # Parent class
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

# The following class is a subclass to entity which creates the player object
class Player(Entity, pygame.sprite.Sprite): # sub-class to Entity
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
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
        if btn[pygame.K_LEFT]:
            self.vel_x -= 5
        if btn[pygame.K_RIGHT]:
            self.vel_x += 5
        if btn[pygame.K_UP]:
            self.vel_y -= 5
        if btn[pygame.K_DOWN]:
            self.vel_y += 5

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def fire(self):
        raise NotImplementedError

def events(): #this has been changed to only track the pressing of keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

def __main__():
    global screen
    screen = Setup(1000,500)
    screen.play()
