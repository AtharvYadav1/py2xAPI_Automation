#common json response validation


def verify_http_status_code(response_data , expected_data):
    assert response_data.status_code == expected_data, "Status code invalid"


def json_key_not_null(key):
    assert key != 0, "Failed - Invalid or Null Key"
    assert key >0 ,  "Failed - Invalid or Null Key"


def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key


def verify_response_key_should_not_be_none(key):
    assert key is not None


def verify_response_delete(response):
    assert "Created" in response


def verify_response_key(key, expected_data):
    assert key == expected_data