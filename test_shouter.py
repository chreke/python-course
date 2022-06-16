from shouter import shout

def test_shout():
    assert shout("hello") == "HELLO!"

def test_shout_with_exclamation_point():
    assert shout("Hello, world!") == "HELLO, WORLD!"
