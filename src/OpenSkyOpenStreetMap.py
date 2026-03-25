import requests

from src.apiadapter import APIAdapter


class ApiRequestException(Exception):
    pass


class OpenSkyOpenStreetMap(APIAdapter):

    def __init__(self):
        self.openstreetmap = "https://nominatim.openstreetmap.org/search"
        self.opensky = "https://opensky-network.org/api/states/all"
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
        self.airplanes = {
            "lamin": coordinates[0],
            "lamax": coordinates[1],
            "lomin": coordinates[2],
            "lomax": coordinates[3]
        }
        return self.airplanes

    def get_airplanes(self):
        params = self.airplanes
        response = requests.get(url=self.opensky, params=params)

        if response.status_code != 200:
            raise ApiRequestException(f"Opensky Api ошибка {response.status_code}, {response.reason}")

        data = response.json()
        return data


api1 = OpenSkyOpenStreetMap()
api1.get_coordinates("")
print(api1.get_airplanes())
