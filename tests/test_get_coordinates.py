from unittest.mock import MagicMock, Mock, patch

import pytest

from src.OpenSkyOpenStreetMap import ApiRequestException, OpenSkyOpenStreetMap


@patch("requests.get")
def test_get_coordinates_success(mock_requests_get: Mock) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"boundingbox": ["42658.2", "823", "-2382", "-3827"]}
    ]
    mock_requests_get.return_value = mock_response
    api = OpenSkyOpenStreetMap()
    country = "Russia"
    result = api.get_coordinates(country)
    expected = {"lamin": "42658.2", "lamax": "823", "lomin": "-2382", "lomax": "-3827"}
    assert result == expected
    mock_requests_get.assert_called_once()


@patch("requests.get")
def test_get_coordinates_failed(mock_requests_get: Mock) -> None:
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.reason = "Not Found"
    mock_requests_get.return_value = mock_response
    api = OpenSkyOpenStreetMap()
    with pytest.raises(ApiRequestException) as exc_info:
        api.get_coordinates("Not Exisiting")
    assert "Nominatim Api ошибка 404. Not Found" in str(exc_info.value)
