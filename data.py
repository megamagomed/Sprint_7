ORDER_LIST_DATA = [
    {},
    {"courierId": "{courier_id}"},
    {"nearestStation": '["1", "2"]'},
    {"limit": 10},
    {"page": 1},
    {"courierId": "{courier_id}", "limit": 5, "page": 1, "nearestStation": '["1", "2"]'},
]

ORDER_LIST_IDS = [
    "without_params",
    "with_courier_id",
    "with_nearest_station",
    "with_limit",
    "with_page",
    "with_all_filters",
]

SAME_LOGIN_ERROR = "Этот логин уже используется"
CREATE_ACC_MISSING_REQUIRED_FIELD_ERROR = "Недостаточно данных для создания учетной записи"
LOGIN_MISSING_REQUIRED_FIELD_ERROR = "Недостаточно данных для входа"
WRONG_LOGIN_ERROR = "Учетная запись не найдена"