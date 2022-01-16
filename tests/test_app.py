import json
from unittest.mock import patch
from src.app import app

with open("tests/padel_requests/response.json", "rb") as file:
    RESPONSE_SCHEDULE = json.load(file)

with open("tests/padel_requests/response_availability.json", "rb") as file:
    RESPONSE_AVAILABILITY = json.load(file)

with open("tests/padel_requests/response_fixed_time.json", "rb") as file:
    RESPONSE_FIXED_TIME = json.load(file)


@patch("src.padel_requests.base.requests")
def test_get_schedule(requests, snapshot):
    requests.post().json.return_value = RESPONSE_SCHEDULE
    data = '{"idCuadro": "5", "fecha": "16/09/2021"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerCuadro"
    with app.test_client() as test_app:
        result = test_app.get("/get_schedule/conecta/2021-09-16")

    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1].get("headers") is not None
    assert requests.post.call_args[1].get("cookies") is not None
    assert requests.post.call_args[1].get("data") == data
    assert result.status_code == 200
    snapshot.assert_match(result.json)


@patch("src.padel_requests.base.requests")
def test_get_availability(requests, snapshot):
    # pylint: disable=line-too-long
    requests.post().json.return_value = RESPONSE_AVAILABILITY
    data = '{"idCuadro": "5", "idRecurso": "19", "idmodalidad": 5, "fecha": "16/09/2021", "hora": "1174"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerInformacionHuecoLibre"
    with app.test_client() as test_app:
        result = test_app.get("/get_availability/conecta/19/2021-09-16/1174")

    origin = "http://www.clubconecta.cl"
    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1]["headers"]["Origin"] == origin
    assert requests.post.call_args[1]["cookies"]["i18next"] == "es-CL"
    assert requests.post.call_args[1].get("data") == data
    assert result.status_code == 200
    snapshot.assert_match(result.json)


@patch("src.padel_requests.base.requests")
def test_get_fixed_times(requests, snapshot):
    # pylint: disable=line-too-long
    requests.post().json.return_value = RESPONSE_FIXED_TIME
    data = '{"id": "15", "idmodalidad": 3, "fecha": "16/09/2021", "idHorario": "1174"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerInformacionHorarioPrefijadoLibre"
    with app.test_client() as test_app:
        result = test_app.get("/get_fixed_time_info/conecta/15/2021-09-16/1174")

    origin = "http://www.clubconecta.cl"
    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1]["headers"]["Origin"] == origin
    assert requests.post.call_args[1]["cookies"]["i18next"] == "es-CL"
    assert requests.post.call_args[1].get("data") == data
    assert result.status_code == 200
    snapshot.assert_match(result.json)
