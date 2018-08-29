import MyGame1
# A module is created to test whether the display board is of correct width
# screen is an instance of Screen which we can use to test variable values.
def test_displayboardwidth():
    screen = MyGame1.Screen()
    assert screen.width == 1000,"Screen was incorrect width."

def test_displayboardheight():
    screen = MyGame1.Screen()
    assert screen.height == 500,"Screen was incorrect height."

def test_constructZombie():
    zombie = MyGame1.Zombie(1, 1, 1, 1, 1)
    assert zombie,"zombie not constructed"
