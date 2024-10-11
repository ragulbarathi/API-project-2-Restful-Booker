import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    print("Creating Token....")
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
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
    response = requests.post(url=URL, headers=HEADERS, data=DATA)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    return booking_id


def test_consume(create_token, create_booking_id):
    print("Token->", create_token)
    print("Booking id->", create_booking_id)
