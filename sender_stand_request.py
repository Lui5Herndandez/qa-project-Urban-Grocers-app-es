import requests
from configuration import BASE_URL, CREATE_USER, CREATE_KITS

def create_user(user_body):
    url = BASE_URL + CREATE_USER
    response = requests.post(BASE_URL, json=user_body)
    return response

def post_new_user():
    response = requests.post(BASE_URL/ CREATE_USER, json={})
    response.raise_for_status()
    return response.json().get('auth_Token')

def post_new_client_kit(kit_body, auth_token):
    url = BASE_URL + CREATE_KITS
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(BASE_URL/ CREATE_KITS, json=kit_body, headers=headers)
    return response
