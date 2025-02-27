# https://www.youtube.com/watch?v=3Tm34b7p_cM&t=6s

"""
API (Application Programming Interface — программный интерфейс приложения, или интерфейс программирования приложений) —
специальный протокол для взаимодействия компьютерных программ, который позволяет использовать функции
одного приложения внутри другого

API отвечает на вопрос “Как ко мне, к моей системе можно обратиться?”, и включает в себя:
- саму операцию, которую мы можем выполнить
- данные, которые поступают на вход
- данные, которые оказываются на выходе (контент данных или сообщение об ошибке)

API — это набор функций. Это может быть одна функция, а может быть много

Вызов АПИ
    Напрямую:
    - Система вызывает функции внутри себя
    - Система вызывает метод другой систем
    - Человек вызывает метод
    - Автотесты дергают методы

    Косвенно:
    - Пользователь работает с GUI


Удаленный вызов процедур (RPC) – это метод межпроцессного взаимодействия. Используется для клиент-серверных приложений.
Механизмы RPC используются, когда компьютерная программа вызывает выполнение процедуры или подпрограммы в другом
адресном пространстве, которое закодировано как обычный вызов процедуры, при этом программист специально не кодирует
детали для удаленного взаимодействия. Этот вызов процедуры также управляет транспортным протоколом низкого уровня,
таким как протокол пользовательских дейтаграмм, протокол управления передачей / Интернет-протокол и т. Д.
Он используется для передачи данных сообщения между программами.

Самый большой недостаток метода RPC заключается в том, что он очень уязвим к сбоям, поскольку в нем задействованы
система связи, другая машина и другой процесс.

REST — это архитектурный стиль. SOAP — это формат обмена сообщениями.

REST и SOAP
- Специфика SOAP — это формат обмена данными. С SOAP это всегда SOAP-XML, который представляет собой XML.
- Специфика REST — использование HTTP в качестве транспортного протокола. Он подразумевает наилучшее использование
  функций, предоставляемых HTTP — методы запросов, заголовки запросов, ответы, заголовки ответов и т. д.

Формат обмена сообщениями
- В SOAP вы используете формат SOAP XML для запросов и ответов
- В REST такого фиксированного формата нет. Вы можете обмениваться сообщениями на основе XML, JSON или любого другого
  удобного формата. JSON является самым популярным среди используемых форматов

Определения услуг
- SOAP использует WSDL (Web Services Description Language) — язык описания веб-сервисов и доступа к ним,
  основанный на языке XML
- REST не имеет стандартного языка определения сервиса. Несмотря на то, что WADL был одним из первых предложенных
  стандартов, он не очень популярен. Более популярно использование Swagger или Open API

Транспорт
- SOAP не накладывает никаких ограничений на тип транспортного протокола.
  Вы можете использовать либо Web протокол HTTP, либо MQ
- REST подразумевает наилучшее использование транспортного протокола HTTP

Простота реализации
- REST обычно использует JSON, который легче анализировать и обрабатывать. В дополнение к этому, REST не требует
  наличия определения службы для предоставления веб-службы
- Однако в случае SOAP вам необходимо определить свой сервис с использованием WSDL, и при обработке и анализе сообщений
  SOAP-XML возникают большие накладные расходы

Плюсы SOAP
- Независимость от языка и платформы. Встроенная функциональность для создания веб-сервисов позволяет SOAP
  обрабатывать сообщения и делать ответы независимыми от языка и платформы
- Связанность с различными транспортными протоколами. SOAP гибок с точки зрения протоколов передачи и приспосабливается
  к более чем одному сценарию
- Встроенная обработка ошибок. Спецификация SOAP API позволяет возвращать XML-сообщение Retry с кодом ошибки и ее
  объяснением
- Ряд расширений безопасности. Благодаря интеграции с протоколами WS-Security качество транзакций SOAP соответствует
  корпоративным стандартам. SOAP гарантирует конфиденциальность и целостность внутри транзакций, обеспечивая
  при этом шифрование на уровне сообщений

Минусы SOAP
- Только XML. SOAP-сообщения содержат много метаданных и поддерживают только подробные
  XML-структуры для запросов и ответов
- Тяжеловесность. Из-за большого размера XML-файлов SOAP-сервисы требуют большой пропускной способности
- Узкоспециализированные знания. Создание серверов SOAP API требует глубокого понимания всех задействованных
  протоколов и их строгих правил
- Утомительное обновление сообщений. Требуются дополнительные усилия для добавления или удаления
  свойств сообщения жесткая схема SOAP замедляет принятие

SOAP это хлопотно, но его обширный функционал в плане безопасности по-прежнему незаменим для биллинговых операций,
систем бронирования и платежей.

Плюсы REST
- Разделение клиента и сервера. По возможности разделяя клиент и сервер, REST обеспечивает лучшую абстракцию по
  сравнению с RPC. Система с уровнями абстракции способна инкапсулировать свои детали, чтобы лучше идентифицировать и
  поддерживать свои свойства. Поэтому REST API достаточно гибок, чтобы развиваться с течением
  времени и при этом оставаться стабильной системой
- Открытость. Все описывается связью между клиентом и сервером, так что для понимания, как взаимодействовать с REST API,
  не требуется никакая внешняя документация
- Дружественность к кэшу. REST единственный стиль, который позволяет кэшировать данные на уровне HTTP благодаря
  повторному использованию множества HTTP-инструментов. В то же время, реализация кэширования в любом другом API
  потребует настройки дополнительного модуля кэширования
- Поддержка нескольких форматов. Возможность поддержки нескольких форматов хранения и обмена данными одна из причин,
  по которым REST в настоящее время преобладает в сфере создания общедоступных API

Минусы REST
- Нет единой структуры REST. Нет точного правильного способа создания REST API. Как моделировать ресурсы и какие
  ресурсы моделировать, будет зависеть от каждого сценария. Это делает REST простым в теории, но трудным на практике
- Большие полезные нагрузки. REST возвращает много богатых метаданных, так что клиент может понять все необходимое о
  состоянии приложения только из его ответов. И эта болтливость не имеет большого значения для большой сетевой трубы с
  большой пропускной способностью. Но это не всегда так. Это стало ключевым движущим фактором для Facebook,
  придумавшего описание стиля GraphQL в 2012 году
- Проблемы чрезмерных или недостаточных данных. Ответы REST зачастую содержат либо слишком много данных,
  либо их недостаточное количество, и создают необходимость в дополнительном запросе


GraphQL это синтаксис, который описывает, как сделать точный запрос данных. Реализация GraphQL стоит того,
если задействована модель данных приложения с большим количеством сложных сущностей, ссылающихся друг на друга.

Плюсы GraphQL
- Типизированная схема. GraphQL заранее публикует то, что он может осуществить, что улучшает обнаруживаемость.
  Указывая клиенту на API GraphQL, мы можем узнать, какие запросы доступны
- Хорошо подходит для графических данных. Данные, которые находятся в глубоких отношениях связанности, но не
  годятся для плоских данных
- Никаких версий. Лучшая практика управления версиями это вообще не версионировать API. В то время как REST
  предлагает несколько версий API, GraphQL использует единую развивающуюся версию, которая обеспечивает непрерывный
  доступ к новым функциям и способствует более чистому и удобному в обслуживании серверному код
- Подробные сообщения об ошибках. Подобно SOAP, GraphQL предоставляет подробную информацию о возникших ошибках.
  Сообщение об ошибке включает в себя все резольверы и ссылается на конкретную часть запроса,
  на которой лежит ответственность
- Гибкие разрешения. GraphQL позволяет выборочно раскрывать определенные функции, сохраняя при этом личную информацию.
  Между тем архитектура REST не раскрывает данные порциями: либо все, либо ничего

Минусы GraphQL
- Проблемы производительности. GraphQL выторговывает сложность в обмен на действенность. Слишком большое количество
  вложенных полей в одном запросе может привести к перегрузке системы. Таким образом,
  для сложных запросов лучшим вариантом остается REST
- Сложность кэширования. Поскольку GraphQL не переиспользует семантику кэширования HTTP,
  кэширование требует приложения дополнительных усилий
- Много самообразования перед разработкой. Когда у них недостаточно времени, чтобы разобраться в нишевых операциях
  GraphQL и SDL, многие проекты решают пойти по известному пути REST

GraphQL большой шаг вперед с точки зрения извлечения данных, но не у всех достаточно времени и возможностей,
чтобы его осваивать.


Безопасные и идемпотентные методы
Безопасный запрос — это запрос, который не меняет состояние приложения.
Идемпотентный запрос — это запрос, эффект которого от многократного выполнения равен эффекту от однократного выполнения.

Безопасные методы
- GET
- HEAD
- OPTIONS

Идемпотентные методы
- GET
- HEAD
- OPTIONS
- PUT
- DELETE

Небезопасный и неидемпотентный метод
- POST


Основные принципы REST
- единый интерфейс
- разграничение клиента и сервера
- нет сохранения состояния
- кэширование всегда разрешено
- многоуровневая система
- код предоставляется по запросу


REST обладает самой высокой абстракцией и лучшим моделированием API. Но он, как правило, тяжелее в плане
нагрузки на сеть и многословнее недостаток, если вы работаете на мобильных устройствах.

1️⃣ GET: Запрашивает представление ресурса. GET-запросы обычно используются для получения данных от сервера.
Они могут быть кэшированы и остаются в истории браузера. Они ограничены в размере.

2️⃣ POST: Отправляет данные для обработки на сервере. POST-запросы часто используются для отправки данных
HTML-формы на сервер для обработки. Они не кэшируются и не остаются в истории браузера.
Они могут отправлять большие объемы данных.

3️⃣ PUT: Загружает содержимое запроса на указанный URI. Если ресурс существует, он перезаписывается.
Если ресурс не существует, сервер может создать его с использованием предоставленных данных.

4️⃣ DELETE: Удаляет указанный ресурс.

5️⃣ PATCH: Применяет частичные модификации к ресурсу. Обычно используется для обновления ресурса с частичными данными.

6️⃣ HEAD: Запрашивает заголовки, которые будут возвращены, как если бы был сделан запрос GET, но без тела ответа.

7️⃣ OPTIONS: Используется для запроса возможностей и параметров коммуникации для указанного ресурса.

8️⃣ TRACE: Используется для тестирования соединения по маршруту к ресурсу. Он выполняет циклический обход маршрутизации,
который включает в себя передачу запроса через все узлы маршрута.
"""
from pprint import pprint

import requests

URL_GET = "https://httpbin.org/get"
URL_POST = "https://httpbin.org/post"

headers = {"User-Agent": "zapel"}

"""
GET
"""

resp_get = requests.get(url=URL_GET, headers=headers, params={"a": "b", "c": "d"})

"""
POST
"""

resp_post = requests.post(
    url=URL_POST, headers=headers, params={"a": "b"}, json={"username": "supersecret"}
)

if __name__ == "__main__":
    # if resp_get.status_code == 200:
    #     print("ok")
    #
    # if resp_get.ok:
    #     print("ok")
    #
    # print(resp_get.raise_for_status())
    # print(resp_get.text)
    # print(resp_get.json()["headers"]["Host"])
    # print(resp_get.json()["headers"])
    #
    # print(resp_post.json())

    pprint(resp_get.content)
