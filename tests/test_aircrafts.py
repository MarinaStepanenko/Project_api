import pytest

from src.aircrafts import Aircraft


def test_aircraft_init(first_aircraft):
    assert first_aircraft.param_list == [
        "39de4e",
        "TVF67AK ",
        "France",
        1775659958,
        1775659958,
        -5.7518,
        37.9108,
        4404.36,
        False,
        300,
        220.56,
        -9.1,
        None,
        4511.04,
        "7626",
        False,
        0,
    ]
    assert first_aircraft.country == "France"
    assert first_aircraft.velocity == 300
    assert first_aircraft.geo_altitude == 4511.04
    assert first_aircraft.callsign == "TVF67AK "


def test_aircraft_init_no_callsign(second_aircraft):
    assert second_aircraft.callsign == "отсутствует"


def test_aircraft_init_error():
    with pytest.raises(ValueError) as exc_info:
        a = Aircraft(
            param_list=[
                "4b1813",
                "EDW116  ",
                None,
                1775659959,
                1775659959,
                -3.4717,
                38.4767,
                11894.82,
                False,
                202.97,
                200.32,
                0,
                None,
                12077.7,
                "3751",
                False,
                0,
            ]
        )
    assert "Значение 'страна' не найдено" in str(exc_info.value)


def test_eq_velocity(second_aircraft, third_aircraft):
    assert second_aircraft == third_aircraft


def test_not_eq_velocity(first_aircraft, third_aircraft):
    assert first_aircraft != third_aircraft


def test_lt_velocity(second_aircraft, first_aircraft):
    assert second_aircraft < first_aircraft


def test_gt_velocity(first_aircraft, second_aircraft):
    assert first_aircraft > second_aircraft


def test_str_aircraft(first_aircraft):
    result = str(first_aircraft)
    assert isinstance(result, str)


def test_repr_returns_string(first_aircraft):
    result = repr(first_aircraft)
    assert isinstance(result, str)


def test_repr_contains_class_name(second_aircraft):
    result = repr(second_aircraft)
    assert "Самолёт" in result
