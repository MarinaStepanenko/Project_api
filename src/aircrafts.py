"""
Модуль с классом Aircraft для представления данных о самолёте.
"""

from typing import Any, List, Union


class Aircraft:
    """Класс, представляющий самолёт с данными от OpenSky Network API.

    Инкапсулирует информацию о самолёте: позывной, страну регистрации,
    скорость, высоту и другие параметры из состояния OpenSky API.

    Attributes:
        param_list (List[Any]): Исходный список параметров от OpenSky API
        country (str): Страна регистрации самолёта
        velocity (Union[int, float]): Скорость самолёта (м/с)
        geo_altitude (Union[int, float]): Географическая высота (м)
        callsign (str): Позывной самолёта (или "отсутствует")
    """

    def __init__(self, param_list: List[Any]) -> None:
        """Инициализирует объект Aircraft из списка параметров OpenSky API.

        Позиции в param_list:
            1: Позывной (callsign)
            2: Страна регистрации (country)
            9: Скорость (velocity)
            -4: Географическая высота (geo_altitude)

        Args:
            param_list: Список параметров самолёта от OpenSky API

        Raises:
            ValueError: Если страна регистрации отсутствует
            (param_list[2] пустой)
        """
        self.param_list: List[Any] = param_list

        if not param_list[2]:
            raise ValueError("Значение 'страна' не найдено")
        self.country: str = param_list[2]

        self.velocity: Union[int, float] = (
            param_list[9] if param_list[9] is not None else 0
        )
        self.geo_altitude: Union[int, float] = (
            param_list[-4] if param_list[-4] is not None else 0
        )

        if not param_list[1]:
            self.callsign: str = "отсутствует"
        else:
            self.callsign = param_list[1]

    def __lt__(self, other: "Aircraft") -> bool:
        """Сравнение: меньше (по скорости)."""
        return self.velocity < other.velocity

    def __gt__(self, other: "Aircraft") -> bool:
        """Сравнение: больше (по скорости)."""
        return self.velocity > other.velocity

    def __eq__(self, other: "Aircraft") -> bool:
        """Сравнение: равно (по скорости)."""
        return self.velocity == other.velocity

    def __str__(self) -> str:
        """Человеко-читаемое представление самолёта."""
        return (
            f"Самолёт {self.callsign}, {self.country}. "
            f"Географическая высота {self.geo_altitude:.0f}, "
            f"скорость {self.velocity:.0f}"
        )

    def __repr__(self) -> str:
        """Техническое представление (совпадает с __str__)."""
        return self.__str__()
