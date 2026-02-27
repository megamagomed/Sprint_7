import allure
import requests
import pytest

from urls import CREATE_ORDER_URL
from helpers import generate_order_data


@allure.feature("Order API")
@allure.story("Create order")
class TestCreateOrder:
    @pytest.mark.parametrize(
        "color",
        [["BLACK"], ["GREY"], ["BLACK", "GREY"], []],
        ids=["black", "grey", "black_and_grey", "without_color"],
    )
    @allure.title("Тест на успешное создание заказа")
    def test_create_order_success(self, color):
        with allure.step("Подготовка тела запроса"):
            payload = generate_order_data(color)
        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(CREATE_ORDER_URL, json=payload)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 201
        with allure.step("Проверка наличия track в ответе"):
            assert "track" in response.json()
