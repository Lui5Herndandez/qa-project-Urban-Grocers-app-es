import requests
from configuration import BASE_URL, CREATE_USER, CREATE_KITS
from data import user_body, kit_body, headers


def create_user():
    url = BASE_URL + CREATE_USER
    response = requests.post(url, json=user_body, headers=headers)
    response_data = response.json()
    auth_token = response_data.get("auth_Token")
    response_data["auth_token"] = auth_token
    return response_data

def post_new_client_kit(auth_token):
    url = BASE_URL + CREATE_KITS
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=kit_body, headers=headers)
    return response
