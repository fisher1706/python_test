"""
1️⃣ GET Method:
This is the most common method, used for retrieving data from a server. When you enter a URL in your browser,
it sends a GET request to fetch the webpage. GET requests should never modify data on the server.

2️⃣ POST Method:
POST is used to send data to a server to create a new resource. For example, when you submit a form on a website,
the data is typically sent via a POST request. The data is included in the body of the request.

3️⃣ PUT Method:
PUT is used to update an existing resource on the server. It replaces the entire resource with the
new data provided in the request body. If the resource doesn't exist, PUT can also be used to create it.

4️⃣ PATCH Method:
Similar to PUT, PATCH is used to modify an existing resource. However, instead of replacing the
entire resource, PATCH only updates the specified parts of the resource.
This is useful when you only need to make partial updates.

5️⃣ DELETE Method:
As the name suggests, the DELETE method is used to remove a resource from the server.
It permanently deletes the specified resource.

6️⃣ HEAD Method:
HEAD is similar to GET, but it only retrieves the headers of the response, not the body.
This is useful for checking the status of a resource or its metadata without downloading the entire content.

7️⃣ OPTIONS Method:
OPTIONS is used to describe the communication options available for a given resource.
It allows the client to determine the supported HTTP methods, headers, and other capabilities of the server.

8️⃣ TRACE Method:
TRACE is used for diagnostic purposes. It echoes back the received request,
allowing the client to see if any changes or additions were made by intermediate servers.

9️⃣ CONNECT Method:
CONNECT is used to establish a tunnel to the server, typically for secure connections using SSL/TLS protocols.
It is commonly used by proxies to facilitate HTTPS connections.


1. Метод GET.
Это наиболее распространенный метод, используемый для получения данных с сервера. Когда вы вводите URL-адрес в браузере,
он отправляет запрос GET для получения веб-страницы. Запросы GET никогда не должны изменять данные на сервере.

2. Метод POST:
POST используется для отправки данных на сервер для создания нового ресурса. Например, когда вы отправляете форму на
веб-сайте, данные обычно отправляются через запрос POST. Данные включаются в тело запроса.

3. Метод PUT:
PUT используется для обновления существующего ресурса на сервере. Он заменяет весь ресурс новыми данными,
указанными в теле запроса. Если ресурс не существует, для его создания также можно использовать PUT.

4. Метод PATCH.
Подобно PUT, PATCH используется для изменения существующего ресурса. Однако вместо замены всего ресурса PATCH обновляет
только указанные части ресурса. Это полезно, когда вам нужно выполнить только частичные обновления.

5. Метод DELETE.
Как следует из названия, метод DELETE используется для удаления ресурса с сервера.
Он безвозвратно удаляет указанный ресурс.

6. Метод HEAD:
HEAD похож на GET, но извлекает только заголовки ответа, а не тело.
Это полезно для проверки статуса ресурса или его метаданных без загрузки всего контента.

7. Метод OPTIONS:
OPTIONS используется для описания вариантов связи, доступных для данного ресурса.
Это позволяет клиенту определять поддерживаемые методы HTTP, заголовки и другие возможности сервера.

8. Метод TRACE:
TRACE используется в диагностических целях. Он повторяет полученный запрос, позволяя клиенту увидеть,
были ли внесены какие-либо изменения или дополнения промежуточными серверами.

9. Метод CONNECT:
CONNECT используется для установки туннеля к серверу, обычно для безопасных соединений с использованием
протоколов SSL/TLS. Он обычно используется прокси-серверами для облегчения HTTPS-соединений.

"""