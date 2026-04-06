import requests

from src.aircrafts import Aircraft
from src.apiadapter import APIAdapter


class ApiRequestException(Exception):
    pass


class OpenSkyOpenStreetMap(APIAdapter):

    def __init__(self):
        self.openstreetmap = "https://nominatim.openstreetmap.org/search"
        self.opensky = "https://opensky-network.org/api/states/all"
        self.coordinates = None
        self.airplanes = None

    def get_coordinates(self, country: str) -> dict:

        headers_nominatim = {
            "User-Agent":
                "test - app / 1.0"
        }

        params_nominatim = {
            "q": country,
            "format": "json",
            "limit": 1
        }
        response = requests.get(url=self.openstreetmap, headers=headers_nominatim, params=params_nominatim)
        if response.status_code != 200:
            raise ApiRequestException(f"Nominatim Api ошибка {response.status_code}. {response.reason}")

        data = response.json()
        coordinates = data[0].get("boundingbox")
        self.coordinates = {
            "lamin": coordinates[0],
            "lamax": coordinates[1],
            "lomin": coordinates[2],
            "lomax": coordinates[3]
        }
        return self.coordinates

    def get_airplanes(self):
        params = self.coordinates
        response = requests.get(url=self.opensky, params=params)

        if response.status_code != 200:
            raise ApiRequestException(f"Opensky Api ошибка {response.status_code}, {response.reason}")

        data = response.json()
        self.airplanes = data.get("states")
        return self.airplanes

    def get_aircraft(self):
        states = self.airplanes
        planes = []
        for state in states:
            plane = Aircraft(state)
            planes.append(plane)
        return planes

if __name__ == "__main__":

    api = OpenSkyOpenStreetMap()

    # 2. Получаем координаты страны
    api.get_coordinates("Spain")
    api.get_airplanes()
    # 3. Получаем список объектов Aircraft
    aircraft = api.get_aircraft()


    # 4. Берём первый самолёт из списка (если есть)
    if aircraft:
        for a in aircraft:

            print(a.param_list)  # ← выводим страну
    else:
        print("Самолётов не найдено")
