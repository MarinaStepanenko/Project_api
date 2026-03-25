from abc import abstractmethod, ABC


class APIAdapter(ABC):

    @abstractmethod
    def get_coordinates(self, country: str):
        pass

    @abstractmethod
    def get_airplanes(self):
        pass
