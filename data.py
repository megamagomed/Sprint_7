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

