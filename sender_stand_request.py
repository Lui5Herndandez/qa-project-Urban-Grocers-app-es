import requests
from configuration import BASE_URL, CREATE_USER, CREATE_KITS
from data import user_body

def create_user(user_body):
    url = BASE_URL + CREATE_USER
    response = requests.post(BASE_URL, json=user_body)
    return response

def post_new_user():
    response = requests.post(BASE_URL + CREATE_USER, json=user_body)
    response.raise_for_status()
    return response.json().get('authToken')

def post_new_client_kit(kit_body, authtoken):
    url = BASE_URL + CREATE_KITS
    headers = {"Authorization": f"Bearer {authtoken}"}
    response = requests.post(BASE_URL + CREATE_KITS, json=kit_body, headers=headers)
    return response
