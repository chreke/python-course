import pytest
from hypothesis import given, strategies

from roman_numerals import roman_numeral, numeral_to_int

@pytest.mark.parametrize("integer, expected", [
    (1, "I"),
    (5, "V"),
    (10, "X"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M"),
])
def test_simple_numerals(integer, expected):
    assert roman_numeral(integer) == expected

@pytest.mark.parametrize("integer, expected", [
    (4, "IV"),
    (6, "VI"),
    (39, "XXXIX"),
    (246, "CCXLVI"),
    (789, "DCCLXXXIX"),
    (2421, "MMCDXXI"),
    (2022, "MMXXII"),
])
def test_complex_numerals(integer, expected):
    assert roman_numeral(integer) == expected


@given(strategies.integers(min_value=1, max_value=10000))
def test_numeral_to_int(integer):
    numeral = roman_numeral(integer)
    assert numeral_to_int(numeral) == integer
