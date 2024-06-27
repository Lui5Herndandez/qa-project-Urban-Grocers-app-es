import requests
from configuration import BASE_URL, CREATE_USER, CREATE_KITS


def post_new_user():
    response = requests.post(BASE_URL/ CREATE_USER, json={})
    response.raise_for_status()
    return response.json().get('auth_Token')

def post_new_client_kit(kit_body, auth_token):
    headers = {'Authorization': auth_token}
    response = requests.post(BASE_URL/ CREATE_KITS, json=kit_body, headers=headers)
    return response