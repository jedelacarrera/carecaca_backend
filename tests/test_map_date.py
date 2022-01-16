from src.padel_requests import map_date


def test_map_date():
    assert map_date("2020-11-12") == "12/11/2020"
    assert map_date("2020.11.12") == "12/11/2020"
    assert map_date("2020/11/12") == "12/11/2020"
    assert map_date("2020-1-2") == "02/01/2020"
