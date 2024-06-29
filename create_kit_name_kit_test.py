import pytest
from sender_stand_request import create_user, post_new_client_kit
import data

def get_kit_body(name):
    body = (kit_body)
    body["Luis"] = name
    return body

def auth_token():
    response = create_user(data.user_body)
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    return response.json().get("authToken")

def positive_assert(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()['name'] == kit_body['name']

def negative_assert_code_400(kit_body, auth_token):
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_name_length_0():
    token_auth = auth_token()
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, token_auth)

def test_name_length_511(auth_token):
    name = {
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
        "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
        "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

    kit_body = get_kit_body(name)
    positive_assert(kit_body, auth_token)

def test_name_length_0(auth_token):
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)

def test_name_length_512(auth_token):
    name = {
        "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
        "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
        "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    kit_body = get_kit_body(name)
    negative_assert_code_400(kit_body, auth_token)

def test_special_characters(auth_token):
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body, auth_token)

def test_spaces(auth_token):
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)

def test_numbers(auth_token):
    kit_body = get_kit_body("123")
    positive_assert(kit_body, auth_token)

def test_no_name_parameter(auth_token):
    kit_body = {}
    negative_assert_code_400(kit_body, auth_token)

def test_name_as_number(auth_token):
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body, auth_token)