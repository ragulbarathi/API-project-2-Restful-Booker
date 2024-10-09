import allure
import pytest
import requests


@pytest.mark.smoke
@allure.title("TC1-Verify ping request")
@allure.description("TC1-healthcheck of the app")
@allure.tag("smoke")
def test_tc1():
    url = "https://restful-booker.herokuapp.com/ping"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    assert response_data.status_code == 201


@pytest.mark.smoke
@allure.title("TC2-Verify booking details are available with valid booking id")
@allure.description("TC2-Tests the booking details of the user with an valid booking id and status code should be 200, "
                    "this is a positive tc")
@allure.tag("smoke")
def test_tc2():
    url = "https://restful-booker.herokuapp.com/booking/5"
    response_data = requests.get(url)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200


@pytest.mark.smoke
@allure.title("TC3-Verify booking details are not shown for null booking id")
@allure.description("TC3-Tests the booking details of the user with an null booking id and status code should be 404, "
                    "this is a negative tc")
@allure.tag("smoke")
def test_tc3():
    url = "https://restful-booker.herokuapp.com/booking/null"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    assert response_data.status_code == 404


@pytest.mark.smoke
@allure.title("TC4-Verify booking details are not shown for negative booking id")
@allure.description("TC4-Tests the booking details of the user with an negative number booking id and status code "
                    "should be 404,"
                    "this is a negative tc")
@allure.tag("smoke")
def test_tc4():
    url = "https://restful-booker.herokuapp.com/booking/-5"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    assert response_data.status_code == 404


@pytest.mark.smoke
@allure.title("TC5-Verify booking details are not shown for invalid booking id")
@allure.description("TC5-Tests the booking details of the user with an invalid booking id and status code "
                    "should be 404,"
                    "this is a negative tc")
@allure.tag("smoke")
def test_tc5():
    url = "https://restful-booker.herokuapp.com/booking/!@"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.headers)
    assert response_data.status_code == 404
