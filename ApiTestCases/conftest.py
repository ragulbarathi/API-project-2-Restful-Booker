import pytest
import requests
from dotenv import load_dotenv
import os


@pytest.fixture()
def create_token():
    load_dotenv(override=True)
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
    response = requests.post(url=URL, headers=HEADERS, json=DATA)
    booking_id = response.json()["bookingid"]
    print(booking_id)
    return booking_id


@pytest.fixture()
def get_booking_by_id(bid):
    url = "https://restful-booker.herokuapp.com/booking/" + str(bid)
    response_data = requests.get(url)
    return response_data
