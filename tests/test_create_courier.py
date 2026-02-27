import allure
import requests
import pytest

from urls import CREATE_COURIER_URL
from helpers import generate_random_string

from api_methods import login_courier_and_get_id, delete_courier_by_id
from data import SAME_LOGIN_ERROR, CREATE_ACC_MISSING_REQUIRED_FIELD_ERROR


@allure.feature("Courier API")
@allure.story("Create courier")
class TestCreateCourier:

    @allure.title("Тест на успешное создание курьера")
    def test_create_courier_success(self, courier_registration_data):

        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(CREATE_COURIER_URL, data=courier_registration_data)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201

        with allure.step("Проверка тела ответа"):
            assert response.json() == {"ok": True}


    @allure.title("Тест на невозможность создания курьера с неуникальным login")
    def test_create_courier_with_non_unique_login_fail(self, new_courier):
        payload = {
            "login": new_courier["payload"]["login"],
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
        }

        with allure.step("Отправка запроса на создание дубликата"):
            response = requests.post(CREATE_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 409

        with allure.step("Проверка текста ошибки"):
            assert SAME_LOGIN_ERROR in response.json()["message"]

    @allure.title("Тест на невозможность создания курьера без обязательного поля")
    @pytest.mark.parametrize(
        "missing_field",
        ["login", "password"],
        ids=["without_login", "without_password"],
    )
    def test_create_courier_without_required_field_fail(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
        }

        with allure.step("Удаление обязательного поля"):
            payload.pop(missing_field)
        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(CREATE_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка текста ошибки"):
            assert response.json()["message"] == CREATE_ACC_MISSING_REQUIRED_FIELD_ERROR
