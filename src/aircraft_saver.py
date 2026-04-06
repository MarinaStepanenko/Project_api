import json
import os.path

from src.aircraft_saver_manager import AircraftSaverManager


class AircraftSaver(AircraftSaverManager):
    """
    Создайте экземпляр этого класса-хранилище.
    вызовется функция _load_data()
    Данные из файла запишутся в self._data или пустой список.
    Сохраните ин-цию о самолете через save_to_file
    вызовется _save_data и перезапишет новую информацию в self._data
    """

    def __init__(self, filename: str = "aircraft_data.json"):
        self.filename = filename
        self._data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._data, f)

    def save_to_file(self, aircraft):

        data = {
            "callsign": aircraft.callsign,
            "velocity": aircraft.velocity,
            "country": aircraft.country,
            "geo_altitude": aircraft.geo_altitude
        }

        self._data.append(data)
        self._save_data()
        return data

    def delete_from_file(self, aircraft):
        pass

    def get_from_file(self, country):
        pass




