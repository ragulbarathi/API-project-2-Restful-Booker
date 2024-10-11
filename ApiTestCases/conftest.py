import allure
import pytest
import requests


@pytest.fixture
def baseurl():
    return "https://restful-booker.herokuapp.com/booking"


@pytest.fixture
def basepath():
    return create_booking()


@pytest.fixture()
def create_booking():
    URL = baseurl()
    HEADERS = {'Content-Type: application/json'}
    BODY = {
        "firstname": "Ragul",
        "lastname": "Ravibarathi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=HEADERS, data=BODY)
    assert response.status_code == 201, f" Expected 201 but found {response.status_code}"
    booking_id=response.json()["bookingid"]
    return booking_id
