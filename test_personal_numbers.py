import datetime
import pytest

from personal_numbers import personal_number_to_date


def test_twelve_digit_personal_number():
    assert personal_number_to_date("199010291234") == datetime.date(1990, 10, 29)

def test_ten_digit_personal_number():
    assert personal_number_to_date("901029-1234") == datetime.date(1990, 10, 29)

def test_person_older_than_100():
    assert personal_number_to_date("101029+1234") == datetime.date(1910, 10, 29)

def test_invalid_personal_number():
    with pytest.raises(ValueError):
        personal_number_to_date("1234")
