from src.helpers import time_to_float


def test_time_to_float():
    assert time_to_float("12:00") == 12
    assert time_to_float("12:30") == 12.5
