from src.aircrafts import Aircraft
from src.OpenSkyOpenStreetMap import OpenSkyOpenStreetMap


def test_get_aircraft():
    api = OpenSkyOpenStreetMap()
    api.airplanes = [
        [
            "39de4e",
            "TVF67AK ",
            "France",
            1775659958,
            1775659958,
            -5.7518,
            37.9108,
            4404.36,
            False,
            155.07,
            220.56,
            -9.1,
            None,
            4511.04,
            "7626",
            False,
            0,
        ],
        [
            "4b1813",
            "EDW116  ",
            "Switzerland",
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
        ],
    ]
    result = api.get_aircraft()

    assert len(result) == 2

    for plane in result:
        assert isinstance(plane, Aircraft)
