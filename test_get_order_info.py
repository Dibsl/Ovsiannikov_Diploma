# Артем Овсянников, 7-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request
import requests
from configuration import URL_SERVICE


# Проверяется, что по треку заказа можно получить данные о заказе.

def test_get_order_info():
    # Создаем заказ с помощью sender_stand_request
    create_order_response = sender_stand_request.post_new_order(data.order_body)
    assert create_order_response.status_code == 201  # Предполагаем, что успешный код для создания заказа - 201

    # Получаем номер трека из ответа
    track = create_order_response.json()["track"]

    # Получаем данные о заказе по треку с использованием API
    get_order_response = requests.get(f"{URL_SERVICE}/get_order/{track}")

    # Проверяем код ответа
    if get_order_response.status_code == 200:
        print("Test passed: Код 200")
    else:
        print("Test failed: Код ответа не равен 200")


# Вызов теста
test_get_order_info()
