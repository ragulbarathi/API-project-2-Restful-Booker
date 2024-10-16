import pytest
import requests
import allure


class Test_crud(object):

    @pytest.mark.smoke
    @allure.title("TC-6 Verify create Booking")
    @allure.description("Verify create booking")
    @allure.tag("smoke")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_booking_post(self, create_booking_id):
        pass

    @pytest.mark.smoke
    @allure.title("TC-7 Verify create Auth Token")
    @allure.description("Verify create Token")
    @allure.tag("smoke")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_token(self, create_token):
        pass

    @pytest.mark.smoke
    @allure.title("TC-8 Verify update booking")
    @allure.description("Update Booking")
    @allure.tag("smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_booking_put(self, create_booking_id, create_token):
        baseurl = "https://restful-booker.herokuapp.com"
        basepath = "/booking/" + str(create_booking_id)
        put_url = baseurl + basepath
        cookie = "token=" + str(create_token)
        Headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "cookie": cookie}
        json_payload = {
            "firstname": "Ragul",
            "lastname": "Ravibarathi",
            "totalprice": 9999,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-02-01"
            },
            "additionalneeds": "Breakfast,Lunch,Dinner"
        }
        response = requests.put(url=put_url, headers=Headers, json=json_payload)
        assert response.status_code == 200, f"Expected 200 but found {response.status_code}"

    @pytest.mark.smoke
    @allure.title("TC-9 Verify Partial update on  booking")
    @allure.description("Partial Update Booking")
    @allure.tag("smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_partialUpdate_booking(self, create_booking_id, create_token):
        baseurl = "https://restful-booker.herokuapp.com"
        basepath = "/booking/" + str(create_booking_id)
        put_url = baseurl + basepath
        cookie = "token=" + str(create_token)
        Headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "cookie": cookie}
        json_payload = {
            "totalprice": 10500
        }
        response = requests.patch(url=put_url, headers=Headers, json=json_payload)
        print(response.json())
        assert response.status_code == 200, f"Expected 200 but found {response.status_code}"

    @pytest.mark.smoke
    @allure.title("TC-10 Verify Delete  booking")
    @allure.description("Delete Booking")
    @allure.tag("smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_booking(self, create_booking_id, create_token):
        baseurl = "https://restful-booker.herokuapp.com"
        x = str(create_booking_id)
        basepath = "/booking/" + x
        del_url = baseurl + basepath
        cookie = "token=" + str(create_token)
        Headers = {"Content-Type": "application/json",
                   "cookie": cookie}

        response = requests.delete(url=del_url, headers=Headers)
        print(f"after delete request this is the response body->{response}")
        assert response.status_code == 201, f"Expected 201 but found {response.status_code}"
        print("response verification->")
        fetch = requests.get(url=del_url)
        print(fetch.status_code)
        assert fetch.status_code == 404
        print("After get request assertion")
