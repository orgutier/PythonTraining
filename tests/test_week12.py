from unittest.mock import patch, MagicMock
import pytest
from exercises.week12.solution import fetch_user_name, fetch_many, APIError


def _mock_response(status_code, json_data):
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = json_data
    return mock


@patch("exercises.week12.solution.requests.get")
def test_fetch_user_name_success(mock_get):
    mock_get.return_value = _mock_response(200, {"name": "Leanne Graham"})
    assert fetch_user_name(1) == "Leanne Graham"


@patch("exercises.week12.solution.requests.get")
def test_fetch_user_name_failure(mock_get):
    mock_get.return_value = _mock_response(404, {})
    with pytest.raises(APIError):
        fetch_user_name(1)


@patch("exercises.week12.solution.requests.get")
def test_fetch_many(mock_get):
    mock_get.return_value = _mock_response(200, {"name": "Same Name"})
    result = fetch_many([1, 2, 3])
    assert result == {1: "Same Name", 2: "Same Name", 3: "Same Name"}

# NOTE: requests.get is mocked -- this hook never touches a live endpoint.
# fetch_many is checked via deterministic shared-state, not timing.
