import requests
from configuration import BASE_URL, CREATE_USER, CREATE_KITS
from data import user_body, kit_body


def create_user():
    url = BASE_URL + CREATE_USER
    response = requests.post(url, json=user_body)
    return response.json()["auth_Token"]

def post_new_client_kit(auth_token):
    url = BASE_URL + CREATE_KITS
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response.json()["authToken"]
