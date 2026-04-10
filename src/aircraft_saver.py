"""
Модуль для сохранения данных о самолётах в JSON файл.
"""

import json
import os.path
from typing import Any, Dict, List

from src.aircraft_saver_manager import AircraftSaverManager


class AircraftSaver(AircraftSaverManager):
    """
    Создайте экземпляр этого класса-хранилище.
    вызовется функция _load_data()
    Данные из файла запишутся в self._data или пустой список.
    Сохраните ин-цию о самолете через save_to_file
    вызовется _save_data и перезапишет новую информацию в self._data
    """

    def __init__(self, filename: str = "aircraft_data.json") -> None:
        """Инициализирует хранилище и загружает данные из файла.

        Args:
            filename: Имя JSON файла для хранения данных
        """
        self.filename: str = filename
        self._data: List[Dict[str, Any]] = self._load_data()

    def _load_data(self) -> List[Dict[str, Any]]:
        """Загружает данные из JSON файла.

        Returns:
            List[Dict[str, Any]]: Список словарей с данными самолётов.
            При отсутствии файла или ошибке чтения возвращает пустой список.
        """
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_data(self) -> None:
        """Сохраняет текущие данные в JSON файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._data, f)

    def save_to_file(self, aircraft: Any) -> Dict[str, Any]:
        """Сохраняет информацию о самолёте в хранилище и файл.

        Args:
            aircraft: Объект самолёта с атрибутами callsign, velocity,
                     country, geo_altitude

        Returns:
            Dict[str, Any]: Словарь с сохранёнными данными самолёта
        """
        data: Dict[str, Any] = {
            "callsign": aircraft.callsign,
            "velocity": aircraft.velocity,
            "country": aircraft.country,
            "geo_altitude": aircraft.geo_altitude,
        }

        self._data.append(data)
        self._save_data()
        return data

    def delete_from_file(self, aircraft: Any) -> None:
        """Удаляет информацию о самолёте из хранилища (не реализовано).

        Args:
            aircraft: Объект самолёта для удаления
        """
        pass

    def get_from_file(self, country: str) -> None:
        """Получает самолёты по стране регистрации (не реализовано).

        Args:
            country: Название страны регистрации
        """
        pass
