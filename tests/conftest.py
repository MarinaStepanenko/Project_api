import pytest

from src.aircraft_saver import AircraftSaver
from src.aircrafts import Aircraft


@pytest.fixture()
def first_aircraft():
    return Aircraft(
        param_list=[
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
    )


@pytest.fixture()
def second_aircraft():
    return Aircraft(
        param_list=[
            "4b1813",
            None,
            "Spain",
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


@pytest.fixture()
def third_aircraft():
    return Aircraft(
        param_list=[
            "4b1813",
            "GHF116  ",
            "Portugal",
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


@pytest.fixture()
def aircraft_saver():
    return AircraftSaver("filename.json")
