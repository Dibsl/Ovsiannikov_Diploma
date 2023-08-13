import configuration
import requests
import data


# Выполнить запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER_PATH,
                         json=body)


response = post_new_order(body=data.order_body.copy())
print(response.status_code)
print(response.json())


# Выполнить запрос на получения заказа по треку заказа.
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH + str(track))
