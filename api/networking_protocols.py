"""
HTTP
(Hypertext Transfer Protocol): This is the protocol your web browser uses to request and receive webpages from servers.
When you type a URL into your browser, it sends an HTTP request to the server, which then sends back the webpage as a
response. HTTP is a "stateless" protocol, meaning each request/response pair is independent.

HTTPS (HTTP Secure):
HTTPS is HTTP with an extra layer of security. It encrypts the data exchanged between your browser and the server
using SSL/TLS. This helps protect sensitive information (like passwords or credit card numbers) from being intercepted
by third parties.

FTP (File Transfer Protocol):
As the name suggests, FTP is used to transfer files between computers over a network.
It's commonly used for uploading files to a web server. FTP establishes two connections - a command connection for
sending instructions, and a data connection for actually transferring the files.

TCP (Transmission Control Protocol):
TCP is all about reliable data delivery. When applications (like email clients or web browsers) send data using TCP,
it establishes a connection and ensures that the data arrives intact and in the right order.
If any data is lost along the way, TCP will resend it.

IP (Internet Protocol):
IP is responsible for addressing and routing data packets across the internet. Each device on the internet has a
unique IP address, which is used to send data to the correct destination. IP is an "unreliable" protocol,
meaning it doesn't guarantee that packets will arrive at their destination or in the right order (that's TCP's job).

UDP (User Datagram Protocol):
UDP is a simpler, faster alternative to TCP. It doesn't establish a connection or provide error checking.
This makes it less reliable, but also much quicker - perfect for applications like video streaming
or online gaming where a little data loss is acceptable.

SMTP (Simple Mail Transfer Protocol):
This protocol handles the sending of email. When you send an email,
your email client uses SMTP to send the message to your mail server, which then uses
SMTP to send it to the recipient's mail server.

SSH (Secure Shell):
SSH allows you to securely connect to a remote computer over an unsecured network.
It's often used by system administrators to manage servers remotely. SSH provides encrypted communication
between the two machines, ensuring that sensitive commands and data can't be intercepted.


HTTP (протокол передачи гипертекста).
Это протокол, который ваш веб-браузер использует для запроса и получения веб-страниц с серверов. Когда вы вводите
URL-адрес в свой браузер, он отправляет HTTP-запрос на сервер, который затем отправляет обратно веб-страницу в качестве
ответа. HTTP — это протокол без сохранения состояния, то есть каждая пара запрос/ответ независима.

HTTPS (HTTP Secure):
HTTPS — это HTTP с дополнительным уровнем безопасности. Он шифрует данные, которыми обмениваются ваш браузер и сервер,
используя SSL/TLS. Это помогает защитить конфиденциальную информацию (например, пароли или номера кредитных карт)
от перехвата третьими лицами.

FTP (протокол передачи файлов).
Как следует из названия, FTP используется для передачи файлов между компьютерами по сети. Обычно он используется
для загрузки файлов на веб-сервер. FTP устанавливает два соединения — командное соединение для отправки инструкций и
соединение для передачи данных для фактической передачи файлов.

TCP (протокол управления передачей):
TCP предназначен для надежной доставки данных. Когда приложения (например, почтовые клиенты или веб-браузеры)
отправляют данные с помощью TCP, они устанавливают соединение и гарантируют, что данные будут доставлены в целости
и сохранности и в правильном порядке. Если какие-либо данные будут потеряны по пути, TCP отправит их повторно.

IP (Интернет-протокол):
IP отвечает за адресацию и маршрутизацию пакетов данных через Интернет. Каждое устройство в Интернете имеет уникальный
IP-адрес, который используется для отправки данных в правильный пункт назначения. IP — «ненадежный» протокол,
то есть он не гарантирует, что пакеты прибудут к месту назначения или в правильном порядке (это работа TCP).

UDP (протокол пользовательских дейтаграмм):
 UDP — более простая и быстрая альтернатива TCP. Он не устанавливает соединение и не обеспечивает проверку ошибок.
 Это делает его менее надежным, но при этом намного более быстрым — идеально подходит для таких приложений,
 как потоковое видео или онлайн-игры, где допустима небольшая потеря данных.

SMTP (простой протокол передачи почты):
этот протокол обрабатывает отправку электронной почты. Когда вы отправляете электронное письмо,
ваш почтовый клиент использует SMTP для отправки сообщения на ваш почтовый сервер,
который затем использует SMTP для отправки его на почтовый сервер получателя.

SSH (Secure Shell):
SSH позволяет безопасно подключаться к удаленному компьютеру через незащищенную сеть.
Его часто используют системные администраторы для удаленного управления серверами.
SSH обеспечивает зашифрованную связь между двумя компьютерами,
гарантируя невозможность перехвата конфиденциальных команд и данных.


 DNS:
 The Web's Linguistic Expert, transforming user friendly domain names into machine readable IP addresses,
 facilitating internet traffic routing.

 TCP/IP:
 The Internet's Core Duo, with TCP managing data packet organisation and delivery,
 and IP overseeing addressing and routing.

 HTTPS:
 Enhancing Web Security, this protocol encrypts data transfers and confirms server authenticity,
 vital for cybersecurity.

 SMTP:
 The Backbone of Email Communication, standardising email transmission across servers, ensuring reliable delivery.

 WebSocket:
 Enabling RealTime Interaction by providing persistent, two way communication channels over a single TCP connection.

 DHCP:
 Streamlining Network Connectivity by automatically assigning IP addresses and configurations to network devices.

 UDP:
 The GoTo for Fast Transmissions, perfect for applications where speed is more critical than delivery assurance,
 such as video streaming or online gaming.

 DNS:
 лингвистический эксперт в Интернете, преобразующий удобные для пользователя доменные имена в машиночитаемые IP-адреса,
 облегчающий маршрутизацию интернет-трафика.

 TCP/IP:
 Базовый дуэт Интернета, где TCP управляет организацией и доставкой пакетов данных,
 а IP контролирует адресацию и маршрутизацию.

 HTTPS:
 повышение веб-безопасности. Этот протокол шифрует передачу данных и подтверждает подлинность сервера,
 что крайне важно для кибербезопасности.

 SMTP:
 основа электронной почты, стандартизирующая передачу электронной почты между серверами и
 гарантирующая надежную доставку.

 WebSocket:
 включение взаимодействия в реальном времени путем предоставления постоянных двусторонних каналов
 связи через одно TCP-соединение.

 DHCP:
 оптимизация сетевых подключений за счет автоматического назначения IP-адресов и конфигураций сетевым устройствам.

 UDP:
 GoTo для быстрой передачи, идеально подходит для приложений, где скорость более важна,
 чем гарантия доставки, таких как потоковое видео или онлайн-игры.
"""
