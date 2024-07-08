from sender_stand_request import create_user, post_new_client_kit
import data


def get_kit_body(name):
    body = data.kit_body.copy()
    body["Luis"] = name
    return body


def auth_token():
    response = create_user()
    return response["auth_token"]


def positive_assert(kit_body, token):
    response = post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body['name']


def negative_assert_code_400(kit_body, token):
    response = post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_name_length_0():
    token = auth_token()
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, token)


def test_name_length_511():
    token = auth_token()
    name = {
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    kit_body = get_kit_body(name)
    positive_assert(kit_body, token)


def test_name_length_512():
    token = auth_token()
    name = {
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    kit_body = get_kit_body(name)
    negative_assert_code_400(kit_body, token)


def test_special_characters():
    token = auth_token()
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body, token)


def test_spaces():
    token = auth_token()
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body, token)


def test_numbers():
    token = auth_token()
    kit_body = get_kit_body("123")
    positive_assert(kit_body,token)


def test_no_name_parameter():
    token = auth_token()
    kit_body = {}
    negative_assert_code_400(kit_body, token)


def test_name_as_number():
    token = auth_token()
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body, token)
