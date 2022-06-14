from shouter import shouter

def test_shout_empty_string():
    assert shouter("") == "!"

def test_shout_string():
    assert shouter("foo") == "FOO!"

def test_shout_with_exclamation_points():
    assert shouter("Hello, world!") == "HELLO, WORLD!"
