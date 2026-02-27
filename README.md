# Sprint_7
## Проверка API сервиса "Яндекс Самокат"
## Шахназаров Магомед
## Когорта 20


## Структура тестов
### 1. Тестирование создания курьера (`tests/test_create_courier.py`)
- `test_create_courier_success` — успешное создание курьера
- `test_create_courier_with_non_unique_login_fail` — нельзя создать курьера с занятым `login`
- `test_create_courier_without_required_field_fail` — ошибка при отсутствии обязательного поля

### 2. Тестирование авторизации курьера (`tests/test_login_courier.py`)
- `test_login_courier_success` — успешная авторизация
- `test_login_courier_without_required_field_fail` — ошибка без обязательного поля
- `test_login_courier_with_wrong_field_fail` — ошибка при неверном `login` или `password`
- `test_login_nonexistent_courier_fail` — ошибка для несуществующего курьера

### 3. Тестирование создания заказа (`tests/test_create_order.py`)
- `test_create_order_success` — успешное создание заказа (с разными вариантами `color`)

### 4. Тестирование получения списка заказов (`tests/test_list_of_orders.py`)
- `test_get_list_of_orders` — получение списка заказов (с разными query-параметрами)

## Вспомогательные файлы
- `helpers.py` — генерация данных и вспомогательные функции для API
- `conftest.py` — фикстуры (`new_courier`)
- `urls.py` — URL эндпоинтов
- `data.py` — наборы данных для параметризованных тестов

## Запуск тестов
```bash
pytest
```

## Запуск с генерацией Allure-результатов
```bash
pytest --alluredir=./allure-results
```

## Просмотр Allure-отчета
```bash
allure serve ./allure-results
```
