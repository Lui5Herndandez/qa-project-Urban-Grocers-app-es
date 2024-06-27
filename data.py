import copy

user_body = {
    "username": "Luis",
    "password": "password123"
}

kit_body = {
    "name": "Luis Hernandez"
}

def get_kit_body(name):
    body = (kit_body)
    body["Luis"] = name
    return body

headers = {
    "Content-Type": "application/json"
}