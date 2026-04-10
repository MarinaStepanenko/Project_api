from abc import ABC, abstractmethod


class AircraftSaverManager(ABC):

    @abstractmethod
    def save_to_file(self, aircraft):
        """
        Добавление информации о самолете в файл
        """
        pass

    @abstractmethod
    def get_from_file(self, country):
        """
        Получения данных из файла по указанным критериям(страна)
        """
        pass

    @abstractmethod
    def delete_from_file(self, aircraft):
        """
        Удаление информации о самолетах
        """
        pass
