import pytest
from hypothesis import given, strategies

from average import average

@given(strategies.lists(strategies.integers(), min_size=1))
def test_average(integers):
    assert isinstance(average(integers), float)

def test_empty_sequence():
    with pytest.raises(ValueError):
        average([])
