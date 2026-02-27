import pytest

from api_methods import (
    delete_courier_by_id,
    login_courier_and_get_id,
    register_new_courier_and_return_login_password,
)
from helpers import generate_random_string  


@pytest.fixture
def new_courier():
    response, payload = register_new_courier_and_return_login_password()
    courier_data = {"response": response, "payload": payload}

    yield courier_data

    courier_id = login_courier_and_get_id(payload)
    if courier_id:
        delete_courier_by_id(courier_id)


@pytest.fixture
def courier_registration_data():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }

    yield payload

    courier_id = login_courier_and_get_id(payload)
    if courier_id:
        delete_courier_by_id(courier_id)