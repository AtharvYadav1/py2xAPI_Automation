import json
import allure
import pytest

from src.Utils.utils import Utils
from src.helpers.api_requests_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_varification import *
from src.constants.api_constants import APIConstants



class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the paylaod and verfiy that booking id should not be null and status code should be 200 for the correct payload")

    def test_create_booking_positive(self):
        response= post_request(url= APIConstants.url_create_booking(self),
                               auth=None,
                               headers= Utils.common_header_json(self),
                               payload= payload_create_booking(),
                               is_json=False)

        bookindId = response.json()["bookingid"]
        verify_http_status_code(response_data= response, expected_data= 200)
