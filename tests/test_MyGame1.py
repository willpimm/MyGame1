from MyGame1 import *
import pygame, MyGame1
pygame.init()
# A module is created to test whether the display board is of correct width
# screen is an instance of Screen which we can use to test variable values.

def test_input_left():
    MyGame1.player = MyGame1.Player(0,0)
    handle_keydown(pygame.K_LEFT)
    assert MyGame1.player.x_direction == -1,"left input not working"

def test_input_right():
    MyGame1.player = MyGame1.Player(0,0)
    handle_keydown(pygame.K_RIGHT)
    assert MyGame1.player.x_direction == 1,"right input not working"

def test_input_up():
    MyGame1.player = MyGame1.Player(0,0)
    handle_keydown(pygame.K_UP)
    assert MyGame1.player.y_direction == -1,"up input not working"

def test_input_down():
    MyGame1.player = MyGame1.Player(0,0)
    handle_keydown(pygame.K_DOWN)
    assert MyGame1.player.y_direction == 1,"down input not working"

"""
def test_construct_Player():
    player = MyGame1.Player(480,220)
    assert player, "player not constructed"

def test_player_width():
    player = MyGame1.Player(480,220)
    assert player.rect.width == 10,"Player incorrect width"

def test_player_height():
    player = MyGame1.Player(480,220)
    assert player.rect.height == 20,"Player inccorect height"

def test_player_stays_in_boundries_left():
    player = MyGame1.Player(0,0)
    player.move()
    assert player.rect.x >=0 ,"Player out of bounds"

def test_player_stays_in_boundries_right():
    player = MyGame1.Player(1000,490)
    player.move()
    assert player.rect.x<1001,"Player out of bounds"

def test_player_stays_in_boundries_up():
    player = MyGame1.Player(0,0)
    player.move()
    assert player.rect.y>-1,"Player out of bounds"

def test_player_stays_in_boundries_down():
    player = MyGame1.Player(0,500)
    player.move()
    assert player.rect.y< 501,"player out of bounds"

def test_player_moves_left():
    player = MyGame1.Player(0,0)
    player.move(-1,0)
    assert player.rect.x == -1 and player.rect.y == 0

def test_construct_Zombie():
    zombie = MyGame1.Zombie(1, 1, 1, 1, 1)
    assert zombie,"zombie not constructed"
"""
