from typing import Any, Dict, List, Optional

import requests

from src.aircrafts import Aircraft
from src.apiadapter import APIAdapter


class ApiRequestException(Exception):
    """Исключение, возникающее при ошибках запросов к внешним API.

    Используется для обработки ошибок HTTP запросов к OpenStreetMap
    и OpenSky Network API.
    """

    pass


class OpenSkyOpenStreetMap(APIAdapter):
    """Адаптер для работы с API OpenSky Network и OpenStreetMap.

    Класс позволяет получить координаты страны через Nominatim API,
    а затем получить список самолётов над указанной территорией
    через OpenSky Network API.

    Attributes:
        openstreetmap (str): URL базового эндпоинта Nominatim API
        opensky (str): URL базового эндпоинта OpenSky Network API
        coordinates (Optional[Dict[str, str]]): Координаты области поиска
        airplanes (Optional[List[List[Any]]]): Сырые данные о самолётах от API
    """

    def __init__(self) -> None:
        """Инициализирует экземпляр класса с базовыми URL и пустыми данными."""
        self.openstreetmap = "https://nominatim.openstreetmap.org/search"
        self.opensky = "https://opensky-network.org/api/states/all"
        self.coordinates: Optional[Dict[str, str]] = None
        self.airplanes: Optional[List[List[Any]]] = None

    def get_coordinates(self, country: str) -> Dict[str, str]:
        """Получает географические координаты страны через Nominatim API.

        Отправляет запрос к OpenStreetMap Nominatim API для получения
        ограничивающего прямоугольника (bounding box) указанной страны.

        Args:
            country: Название страны на английском языке

        Returns:
            Dict[str, str]: Словарь с координатами:
                - lamin: Южная широта
                - lamax: Северная широта
                - lomin: Западная долгота
                - lomax: Восточная долгота

        Raises:
            ApiRequestException: Если статус ответа API не равен 200
            IndexError: Если страна не найдена (ответ API пуст)

        Example:
            >>> api = OpenSkyOpenStreetMap()
            >>> coords = api.get_coordinates("Russia")
            >>> print(coords['lamin'])
            '41.0'
        """
        headers_nominatim: Dict[str, str] = {"User-Agent": "test - app / 1.0"}

        params_nominatim: Dict[str, Any] = {"q": country, "format": "json", "limit": 1}

        response: requests.Response = requests.get(
            url=self.openstreetmap, headers=headers_nominatim, params=params_nominatim
        )

        if response.status_code != 200:
            raise ApiRequestException(
                f"Nominatim Api ошибка {response.status_code}. {response.reason}"
            )

        data: List[Dict[str, Any]] = response.json()

        if not data:
            raise IndexError(f"Страна '{country}' не найдена")

        coordinates: List[str] = data[0].get("boundingbox", [])

        self.coordinates = {
            "lamin": coordinates[0],
            "lamax": coordinates[1],
            "lomin": coordinates[2],
            "lomax": coordinates[3],
        }

        return self.coordinates


def get_airplanes(self) -> Optional[List[List[Any]]]:
    """Получить данные о самолётах через OpenSky API.

    Returns:
        Optional[List[List[Any]]]: Список состояний самолётов

    Raises:
        ApiRequestException: При ошибке HTTP запроса
        AttributeError: Если координаты не получены
    """
    if self.coordinates is None:
        raise AttributeError("Сначала вызовите get_coordinates()")

    response: requests.Response = requests.get(
        url=self.opensky, params=self.coordinates
    )

    if response.status_code != 200:
        raise ApiRequestException(
            f"Opensky Api ошибка {response.status_code}, {response.reason}"
        )

    data: Dict[str, Any] = response.json()
    self.airplanes = data.get("states")

    return self.airplanes


def get_aircraft(self) -> List[Aircraft]:
    """Преобразовать данные API в список объектов Aircraft.

    Returns:
        List[Aircraft]: Список объектов самолётов

    Raises:
        AttributeError: Если данные самолётов не получены
    """
    if self.airplanes is None:
        raise AttributeError("Сначала вызовите get_airplanes()")

    return [Aircraft(state) for state in self.airplanes]
