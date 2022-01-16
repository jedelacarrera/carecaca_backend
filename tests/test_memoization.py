from unittest.mock import Mock, patch
from src.memoization_decorator import cache_decorator, client


def test_cache_decorator():
    client.data = {}
    mock = Mock(return_value=5)

    @cache_decorator("function", 60)
    def function(value):
        return mock(value)

    assert len(mock.call_args_list) == 0
    response = function(10)
    assert response == 5
    assert len(mock.call_args_list) == 1
    assert mock.call_args_list[0][0][0] == 10
    items = client.data.items()
    assert len(items) == 1
    item = next(iter(items))
    assert item[0] == ("function", 10)
    assert item[1][0] == 5
    assert isinstance(item[1][1], float)

    response = function(10)
    assert response == 5
    assert len(mock.call_args_list) == 1


@patch("src.memoization_decorator.time")
def test_expiration_value(time_mock):
    client.data = {}
    time_mock.time.side_effect = [1000, 1001, 1011, 1011]
    mock = Mock()
    mock.side_effect = [5, 6]

    @cache_decorator("expiration_function", 10)
    def function(value):
        return mock(value)

    response = function("my-date")

    assert response == 5
    assert len(mock.call_args_list) == 1
    assert mock.call_args_list[0][0][0] == "my-date"
    assert len(time_mock.time.call_args_list) == 1

    keys = client.data.keys()
    assert len(keys) == 1
    assert client.data.get(next(iter(keys))) == (5, 1010)

    response = function("my-date")

    assert response == 5
    assert len(mock.call_args_list) == 1
    assert len(time_mock.time.call_args_list) == 2

    keys = client.data.keys()
    assert len(keys) == 1
    assert client.data.get(next(iter(keys))) == (5, 1010)

    response = function("my-date")

    assert response == 6
    assert len(mock.call_args_list) == 2
    assert mock.call_args_list[1][0][0] == "my-date"
    assert len(time_mock.time.call_args_list) == 4

    keys = client.data.keys()
    assert len(keys) == 1
    assert client.data.get(next(iter(keys))) == (6, 1021)
