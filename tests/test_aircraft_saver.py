import json
import os.path

from src.aircraft_saver import AircraftSaver


def test_aircraft_saver_init(aircraft_saver):
    assert aircraft_saver.filename == "filename.json"


def test_save_to_file(first_aircraft, aircraft_saver):
    result = aircraft_saver.save_to_file(first_aircraft)
    expected = {
        "callsign": "TVF67AK ",
        "velocity": 300,
        "country": "France",
        "geo_altitude": 4511.04,
    }
    assert result == expected


def test_load_data_success(tmp_path):
    test_file = tmp_path / "valid.json"
    data = [{"callsign": "BDH2637", "velocity": 736}]
    with open(test_file, "w") as f:
        json.dump(data, f)

    saver = AircraftSaver(str(test_file))
    assert saver._data == [{"callsign": "BDH2637", "velocity": 736}]


def test_load_data_not_existing():
    test_file_not = "not / existing.json"
    saver = AircraftSaver(str(test_file_not))

    assert saver._data == []
    assert not os.path.exists("existing.json")


def test_load_data_error(tmp_path):
    test_file = tmp_path / "not valid json"
    with open(test_file, "w") as f:
        f.write("{corrupted")

    saver = AircraftSaver(filename=str(test_file))
    assert saver._data == []


def test_save_data(tmp_path):
    test_file = tmp_path / "file.json"
    saver = AircraftSaver(filename=str(test_file))

    test_data = [{"callsign": "TEST123", "velocity": 500}]
    saver._data = test_data

    saver._save_data()
    assert test_file.exists()

    # Проверяем содержимое файла
    with open(test_file, "r") as f:
        saved_data = json.load(f)

    assert saved_data == test_data
