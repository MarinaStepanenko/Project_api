class Aircraft:

    def __init__(self, param_list: list):
        self.param_list = param_list

        if not param_list[2]:
            raise ValueError("Значение 'страна' не найдено"
            )
        self.country = param_list[2]

        self.velocity = param_list[9] if param_list[9] is not None else 0
        self.geo_altitude = param_list[-4] if param_list[-4] is not None else 0

        if not param_list[1]:
            self.callsign = "отсутствует"
        self.callsign = param_list[1]

    def __lt__(self, other):
        return self.velocity < other.velocity

    def __gt__(self, other):
        return self.velocity > other.velocity

    def __eq__(self, other):
        return self.velocity == other.velocity

    def __str__(self):
        return f"Самолёт {self.callsign}, {self.country}. Географическая высота {self.geo_altitude:.0f}, скорость {self.velocity:.0f}"

    def __repr__(self):
        return self.__str__()

