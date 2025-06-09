import pytest

from tests.test_helpers.api_test_cases import MISSING_PARAMS, ROUTES


def test_temperature_conversion(client):
    response = client.get(
        "/convert/temperature?val=100&from_unit=celsius&to_unit=kelvin"
    )
    assert response.status_code == 200
    assert response.get_json()["result"] == pytest.approx(373.15, abs=1e-4)


def test_length_conversion(client):
    response = client.get("/convert/length?val=12&from_unit=inches&to_unit=feet")
    assert response.status_code == 200
    assert response.get_json()["result"] == pytest.approx(1.0, abs=1e-4)


def test_weight_conversion(client):
    response = client.get("/convert/weight?val=1000&from_unit=grams&to_unit=kilograms")
    assert response.status_code == 200
    assert response.get_json()["result"] == pytest.approx(1.0, abs=1e-4)


@pytest.mark.parametrize(
    "route",
    ROUTES,
)
@pytest.mark.parametrize(
    "query, missing_param",
    MISSING_PARAMS,
)
def test_missing_params_all_routes(client, route, query, missing_param):
    response = client.get(f"/convert/{route}?{query}")
    assert response.status_code == 400
    assert "Missing parameter" in response.get_json()["error"]
    assert missing_param in response.get_json()["error"]
