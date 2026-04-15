from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class APIAdapter(ABC):
    """Абстрактный адаптер для работы с API."""

    @abstractmethod
    def get_coordinates(self, country: str) -> Dict[str, str]:
        """Получить координаты страны.

        Args:
            country: Название страны

        Returns:
            Dict[str, str]: Координаты страны
        """
        pass

    @abstractmethod
    def get_airplanes(self) -> Optional[List[List[Any]]]:
        """Получить данные о самолётах.

        Returns:
            Optional[List[List[Any]]]: Список самолётов или None
        """
        pass
