from src.aircraft_saver import AircraftSaver
from src.OpenSkyOpenStreetMap import OpenSkyOpenStreetMap


def user_interaction():
    """
    Ввести название страны для запроса информации о самолетах
    из opensky - network.org.
    Получить топ N самолетов по высоте полета(N запрашивать у пользователя).
    Получить самолеты по стране их регистрации.
    """
    country = input("Для поиска введите название страны на английском _ ").strip()
    while True:
        try:
            n = int(
                input(
                    "Введите кол-во самолётов по статистике высоты, которое необходимо увидеть _ "
                )
            )
            if n > 0:
                break
            else:
                print("Введите число больше 0")
        except ValueError:
            print("Значение должно быть числом больше нуля")

    filter_country = input(
        "Введите страну регистрации в/с для просмотра нужных самолётов _ "
    ).strip()

    api = OpenSkyOpenStreetMap()

    try:
        api.get_coordinates(country)
    except Exception as e:
        print(f"Страна не найдена, проверьте написание. Ошибка {e}")
        return

    api.get_airplanes()
    aircraft_list = api.get_aircraft()

    if not aircraft_list:
        print(f"Самолётов над страной {country} не найдено")
        return
    print(f"Всего найдено {len(aircraft_list)} самолётов над страной {country}")

    aircraft_save = input(
        "Желаете сохранить результаты вашего поиска? Введите 'да' или 'нет' "
    )
    if aircraft_save.strip() == "да":
        b = AircraftSaver()
        for a in aircraft_list:
            b.save_to_file(a)

    sorted_list = sorted(aircraft_list, key=lambda x: x.geo_altitude, reverse=True)

    sorted_by_country = [item for item in sorted_list if item.country == filter_country]
    if not sorted_by_country:
        print(
            f"Топ {n} самолётов по высоте страны регистрации {filter_country} не найдено.\nИзмените поиск"
        )
    for i, plane in enumerate(sorted_by_country[:n], 1):
        print(
            f"{i}. Позывной: {plane.callsign}, скорость: {plane.velocity:.0f} м/с, "
            f"страна регистрации: {plane.country}, "
            f"высота: {plane.geo_altitude:.0f}"
        )


user_interaction()
