import allure
import requests
import pytest

from api_methods import login_courier_and_get_id
from urls import GET_ORDERS_LIST_URL
from data import ORDER_LIST_DATA, ORDER_LIST_IDS


@allure.feature("Order API")
@allure.story("Get orders list")
class TestListOfOrders:

    @pytest.mark.parametrize("order_list_data", ORDER_LIST_DATA, ids=ORDER_LIST_IDS)
    @allure.title("Тест на получение списка заказов")
    def test_get_list_of_orders(self, new_courier, order_list_data):
        with allure.step("Получение id курьера"):
            courier_id = login_courier_and_get_id(new_courier["payload"])

        with allure.step("Подготовка query-параметров"):
            order_params = order_list_data.copy()
            if "courierId" in order_params:
                order_params["courierId"] = courier_id

        with allure.step("Отправка запроса на получение списка заказов"):
            response = requests.get(GET_ORDERS_LIST_URL, params=order_params)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200
        with allure.step("Проверка структуры тела ответа"):
            assert "orders" in response.json()
