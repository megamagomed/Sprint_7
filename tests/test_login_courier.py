import allure
import requests
import pytest

from urls import LOGIN_COURIER_URL
from helpers import generate_random_string, login_courier


@allure.feature("Courier API")
@allure.story("Login courier")
class TestLoginCourier:

    @allure.title("Тест на успешную авторизацию")
    def test_login_courier_success(self, new_courier):
        with allure.step("Отправка запроса на авторизацию"):
            response = login_courier(new_courier["payload"])

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка наличия id в ответе"):
            assert "id" in response.json()

    @allure.title("Тест на невозможность авторизации без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login"], ids=["without_login"])
    def test_login_courier_without_required_field_fail(
        self, new_courier, missing_field
    ):
        payload = new_courier["payload"].copy()

        with allure.step("Удаление обязательного поля"):
            payload.pop(missing_field)
        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 400
        with allure.step("Проверка текста ошибки"):
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title(
        "Тест на невозможность авторизации с неправильным логином или паролем"
    )
    @pytest.mark.parametrize(
        "wrong_field", ["login", "password"], ids=["wrong_login", "wrong_password"]
    )
    def test_login_courier_with_wrong_field_fail(self, new_courier, wrong_field):
        payload = new_courier["payload"].copy()
        payload.pop("firstName")
        payload[wrong_field] = generate_random_string(10)

        with allure.step("Отправка запроса на авторизацию с неверными данными"):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 404
        with allure.step("Проверка текста ошибки"):
            assert response.json()["message"] == "Учетная запись не найдена"

   
    @allure.title("Тест на невозможность авторизации несуществующего курьера")
    def test_login_nonexistent_courier_fail(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
        }

        with allure.step("Отправка запроса на авторизацию"):
            response = requests.post(LOGIN_COURIER_URL, data=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 404
        with allure.step("Проверка текста ошибки"):
            assert response.json()["message"] == "Учетная запись не найдена"
