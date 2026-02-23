import pytest

from api_methods import (
    delete_courier_by_id,
    login_courier_and_get_id,
    register_new_courier_and_return_login_password,
)

@pytest.fixture
def new_courier():
    response, payload = register_new_courier_and_return_login_password()
    courier_data = {"response": response, "payload": payload}

    yield courier_data

    courier_id = login_courier_and_get_id(payload)
    if courier_id:
        delete_courier_by_id(courier_id)


