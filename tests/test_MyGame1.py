import MyGame1
# A module is created to test whether the display board is of correct width
# screen is an instance of Screen which we can use to test variable values.

def test_display_board_width():
    screen = MyGame1.Setup(1000,500)
    assert screen.width == 1000,"Screen was incorrect width."

def test_display_board_height():
    screen = MyGame1.Setup(1000,500)
    assert screen.height == 500,"Screen was incorrect height."

def test_construct_Player():
    player = MyGame1.Player(480,220,10,20)
    assert player, "player not constructed"

def test_player_width():
    player = MyGame1.Player(480,220,10,20)
    assert player.width == 10,"Player incorrect width"

def test_player_height():
    player = MyGame1.Player(480,220,10,20)
    assert player.height == 20,"Player inccorect height"

def test_player_stays_in_boundries_left():
    player = MyGame1.Player(0,0,10,20)
    player.move_left()
    assert player.x >=0 ,"Player out of bounds"

def test_player_stays_in_boundries_right():
    player = MyGame1.Player(1000,490,10,20)
    player.move_right()
    assert player.x<1001,"Player out of bounds"

def test_player_stays_in_boundries_up():
    player = MyGame1.Player(0,0,10,20)
    player.move_up()
    assert player.y>-1,"Player out of bounds"

def test_player_stays_in_boundries_down():
    player = MyGame1.Player(0,500,10,20)
    player.move_down()
    assert player.y< 501,"player out of bounds"

"""
def test_construct_Zombie():
    zombie = MyGame1.Zombie(1, 1, 1, 1, 1)
    assert zombie,"zombie not constructed"

"""
