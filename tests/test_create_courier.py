import allure
import requests
import pytest

from urls import CREATE_COURIER_URL
from helpers import generate_random_string


@allure.feature("Courier API")
@allure.story("Create courier")
class TestCreateCourier:
    
    @allure.title("Тест на успешное создание курьера")
    def test_create_courier_success(self, new_courier):
        with allure.step("Проверка кода ответа"):
            assert new_courier["response"].status_code == 201

        with allure.step("Проверка тела ответа"):
            assert new_courier["response"].json() == {"ok": True}

    @allure.title("Тест на невозможность создания курьера с неуникальным login")
    @pytest.mark.parametrize(
        "same_credentials", [True, False], ids=["same_payload", "same_login_only"]
    )
    def test_create_courier_with_non_unique_login_fail(self, new_courier, same_credentials):
        if same_credentials:
            payload = new_courier["payload"]
        else:
            payload = {
                "login": new_courier["payload"]["login"],
                "password": generate_random_string(10),
                "firstName": generate_random_string(10),
            }

        with allure.step("Отправка запроса на создание дубликата"):
            duplicate_response = requests.post(CREATE_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert duplicate_response.status_code == 409

        with allure.step("Проверка текста ошибки"):
            assert "Этот логин уже используется" in duplicate_response.json()["message"]

    @allure.title("Тест на невозможность создания курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"], ids=["without_login", "without_password"])
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
            assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
