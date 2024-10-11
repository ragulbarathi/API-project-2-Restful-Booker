import pytest
import requests
import allure


@pytest.mark.smoke
@allure.title("TC-6 Verify create Booking")
@allure.description("Verify create booking")
@allure.tag("smoke")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    HEADERS = {"Content-Type": "application/json"}
    DATA = {
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
    response = requests.post(url=URL, headers=HEADERS, json=DATA)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    return booking_id
