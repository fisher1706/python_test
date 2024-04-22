"""
The diagram below shows how data is encapsulated and de-encapsulated when transmitting over the network.

🔹 Step 1:
   When Device A sends data to Device B over the network via the HTTP protocol,
   it is first added an HTTP header at the application layer.

🔹 Step 2:
   Then a TCP or a UDP header is added to the data. It is encapsulated into TCP segments at the transport layer.
   The header contains the source port, destination port, and sequence number.

🔹 Step 3:
   The segments are then encapsulated with an IP header at the network layer.
   The IP header contains the source/destination IP addresses.

🔹 Step 4:
   The IP datagram is added a MAC header at the data link layer, with source/destination MAC addresses.

🔹 Step 5:
   The encapsulated frames are sent to the physical layer and sent over the network in binary bits.

🔹 Steps 6-10:
   When Device B receives the bits from the network, it performs the de-encapsulation process, which is a
   reverse processing of the encapsulation process. The headers are removed layer by layer, and eventually,
   Device B can read the data.

We need layers in the network model because each layer focuses on its own responsibilities.
Each layer can rely on the headers for processing instructions and does not need to know the
meaning of the data from the last layer.


На диаграмме ниже показано, как данные инкапсулируются и деинкапсулируются при передаче по сети.

🔹Шаг 1.
  Когда устройство A отправляет данные на устройство B по сети через протокол HTTP, к нему сначала
  добавляется HTTP-заголовок на уровне приложения.

🔹Шаг 2:
  Затем к данным добавляется заголовок TCP или UDP. Он инкапсулируется в сегменты TCP на
  транспортном уровне. Заголовок содержит порт источника, порт назначения и порядковый номер.

🔹Шаг 3.
  Затем сегменты инкапсулируются с помощью IP-заголовка на сетевом уровне. Заголовок IP содержит
  IP-адреса источника/назначения.

🔹 Шаг 4.
   К IP-дейтаграмме добавляется MAC-заголовок на уровне канала передачи данных с MAC-адресами источника/назначения.

🔹Шаг 5:
  Инкапсулированные кадры отправляются на физический уровень и передаются по сети в двоичных битах.

🔹Шаги 6–10:
  Когда устройство Б получает биты из сети, оно выполняет процесс деинкапсуляции, который представляет собой
  обратную обработку процесса инкапсуляции. Заголовки удаляются слой за слоем, и в конечном итоге
  Устройство Б может прочитать данные.

Нам нужны уровни в сетевой модели, потому что каждый уровень ориентирован на свои обязанности. Каждый уровень может
полагаться на заголовки для инструкций обработки и не обязан знать значение данных последнего уровня.
"""