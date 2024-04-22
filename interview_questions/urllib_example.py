"""
urllib — это модуль, который предоставляет различные инструменты для работы с URL-адресами и сетевыми запросами.
С его помощью вы можете выполнять операции, такие как отправка HTTP-запросов, получение данных из
URL-адресов и работа с различными протоколами сети.
"""

import urllib.request


def opener_example(url: str):
    opener = urllib.request.FancyURLopener({})
    f = opener.open(url)
    content = f.read()
    return content
