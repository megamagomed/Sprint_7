import random
import string

import requests

from urls import CREATE_COURIER_URL, LOGIN_COURIER_URL
from faker import Faker


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_order_data(color):
    fake = Faker()
    order_data = {
        "firstName": fake.name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 237),
        "phone": fake.phone_number(),
        "rentTime": fake.random_digit_not_null(),
        "deliveryDate": fake.date(pattern="%Y-%m-%d"),
        "comment": fake.sentence(),
        "color": color,
    }
    return order_data
