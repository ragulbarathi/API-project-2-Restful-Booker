import pytest
import requests
import allure


@pytest.mark.smoke
@allure.title("TC-6 Verify create Booking")
@allure.description("Verify create booking")
@allure.tag("smoke")
@allure.severity(allure.severity_level.BLOCKER)
def test_create_booking(create_booking_id):
    pass
