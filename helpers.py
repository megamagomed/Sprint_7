import random
import string

import requests

from urls import CREATE_COURIER_URL, LOGIN_COURIER_URL
from faker import Faker



def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    response = requests.post(CREATE_COURIER_URL, data=payload)
    return response, payload


def login_courier_and_get_id(payload):
    login_response = login_courier(payload)
    return login_response.json().get("id")


def login_courier(payload):
    login_payload = {
        "login": payload["login"],
        "password": payload["password"],
    }
    return requests.post(LOGIN_COURIER_URL, data=login_payload)


def delete_courier_by_id(courier_id):
    return requests.delete(f"{CREATE_COURIER_URL}/{courier_id}")


def generate_order_data(color):
    fake = Faker()
    order_data = {
        "firstName": fake.name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1,237),
        "phone": fake.phone_number(),
        "rentTime": fake.random_digit_not_null(),
        "deliveryDate": fake.date(pattern="%Y-%m-%d"),
        "comment": fake.sentence(),
        "color": color,
    }
    return order_data

