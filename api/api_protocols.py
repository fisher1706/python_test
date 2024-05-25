"""
This  infographic provides an overview of 8 of the most important API protocols to be aware of:

- REST and GraphQL are two leading approaches for building web APIs.
REST provides a scalable architecture through standard HTTP methods,
while GraphQL enables clients to query for precise data.

- Protocols like gRPC, WebSocket, MQTT and AMQP support specialized use cases such as high-performance
remote procedure calls, realtime browser communication, lightweight IoT device messaging, and reliable message queuing.

Choosing the optimal API protocol depends on factors like performance, scalability, client support,
realtime data needs, and message durability.

As an API developer, it's critical to understand the tradeoffs.

Check out the complete infographic to learn more about when to use SOAP vs REST, how GraphQL differs from REST,
and what MQTT brings to the IoT world


В этой инфографике представлен обзор 8 наиболее важных протоколов API, о которых следует знать:

— REST и GraphQL — два ведущих подхода к созданию веб-API.
REST обеспечивает масштабируемую архитектуру с помощью стандартных методов HTTP.
в то время как GraphQL позволяет клиентам запрашивать точные данные.

- Такие протоколы, как gRPC, WebSocket, MQTT и AMQP, поддерживают специализированные варианты использования,
например высокопроизводительные. Удаленные вызовы процедур, связь с браузером в реальном времени, упрощенный обмен
сообщениями с устройствами Интернета вещей и надежная организация очередей сообщений.

Выбор оптимального протокола API зависит от таких факторов, как производительность, масштабируемость,
поддержка клиентов, потребности в данных в реальном времени и надежность сообщений.

Разработчику API очень важно понимать компромиссы.

Ознакомьтесь с полной инфографикой, чтобы узнать больше о том, когда использовать SOAP или REST,
чем GraphQL отличается от REST и что MQTT приносит в мир Интернета вещей


𝟭. 𝗪𝗲𝗯𝗵𝗼𝗼𝗸𝘀:
- Real-time event notifications for seamless data integration.
- Applications: Ideal for instant updates in applications like messaging platforms and automated workflows.

𝟮. 𝗚𝗿𝗮𝗽𝗵𝗤𝗟:
- A flexible query language for efficient data retrieval.
- Applications: Empowers clients to request only the specific data they need, optimizing API performance.

𝟯. 𝗦𝗢𝗔𝗣:
- A protocol for exchanging structured information in web services.
- Applications: Commonly used in enterprise-level integrations requiring strict security and transactional capabilities.

𝟰. 𝗪𝗲𝗯𝘀𝗼𝗰𝗸𝗲𝘁:
- A communication protocol providing full-duplex communication channels over a single, long-lived connection.
- Applications: Ideal for real-time applications like chat applications, gaming, and financial trading platforms.

𝟱. 𝗴𝗥𝗣𝗖:
- A high-performance RPC (Remote Procedure Call) framework.
- Applications: Efficiently connects services in microservices architecture,
  enhancing communication speed and simplicity.

𝟲. 𝗠𝗤𝗧𝗧:
- A lightweight publish-subscribe messaging protocol for small sensors and mobile devices.
- Applications: Commonly used in IoT and real-time communication scenarios.

𝟳. 𝗔𝗠𝗤𝗣:
- A messaging protocol for message-oriented middleware.
- Applications: Facilitates communication between different systems and services, ensuring reliable message delivery.

𝟴. 𝗦𝗦𝗘 (𝗦𝗲𝗿𝘃𝗲𝗿-𝗦𝗲𝗻𝘁 𝗘𝘃𝗲𝗻𝘁𝘀):
- A simple and efficient communication protocol for one-way communication from server to client.
- Applications: Suitable for scenarios where real-time updates are crucial, such as live feeds and notifications.

𝟵. 𝗘𝗗𝗜 (𝗘𝗹𝗲𝗰𝘁𝗿𝗼𝗻𝗶𝗰 𝗗𝗮𝘁𝗮 𝗜𝗻𝘁𝗲𝗿𝗰𝗵𝗮𝗻𝗴𝗲):
- A protocol for the computer-to-computer exchange of business documents in a standard electronic format.
- Applications: Widely used in business and finance for automating document exchange.

𝟭𝟬. 𝗘𝗗𝗔 (𝗘𝘃𝗲𝗻𝘁-𝗗𝗿𝗶𝘃𝗲𝗻 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲):
- A paradigm promoting the production, detection, consumption, and reaction to events.
- Applications: Enhances real-time responsiveness in systems, particularly in complex, distributed environments.

𝟭𝟭. 𝗥𝗘𝗦𝗧 (𝗥𝗲𝗽𝗿𝗲𝘀𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗦𝘁𝗮𝘁𝗲 𝗧𝗿𝗮𝗻𝘀𝗳𝗲𝗿):
- A software architectural style for designing networked applications.
- Applications: Widely adopted for building scalable and maintainable web services.

𝟭. 𝗪𝗲𝗯𝗵𝗼𝗼𝗸𝘀:
- Уведомления о событиях в режиме реального времени для плавной интеграции данных.
- Приложения: идеально подходит для мгновенных обновлений в таких приложениях,
  как платформы обмена сообщениями и автоматизированные рабочие процессы.

𝟮. 𝗚𝗿𝗮𝗽𝗵𝗤𝗟:
- Гибкий язык запросов для эффективного поиска данных.
- Приложения: позволяет клиентам запрашивать только те данные, которые им нужны, оптимизируя производительность API.

𝟯. 𝗦𝗢𝗔𝗣:
— Протокол обмена структурированной информацией в веб-сервисах.
- Приложения: обычно используются в интеграциях на уровне предприятия, требующих строгой безопасности и
  транзакционных возможностей.

𝟰. 𝗪𝗲𝗯𝘀𝗼𝗰𝗸𝗲𝘁:
- Протокол связи, обеспечивающий полнодуплексные каналы связи по одному долгоживущему соединению.
- Приложения: идеально подходит для приложений реального времени, таких как чат-приложения,
  игры и финансовые торговые платформы.

𝟱. 𝗴𝗥𝗣𝗖:
- Высокопроизводительная структура RPC (удаленный вызов процедур).
- Приложения: эффективно соединяет сервисы в архитектуре микросервисов, повышая скорость и простоту связи.

𝟲. 𝗠𝗤𝗧𝗧:
- Облегченный протокол обмена сообщениями публикации-подписки для небольших датчиков и мобильных устройств.
- Приложения: обычно используются в сценариях Интернета вещей и связи в реальном времени.

𝟳. 𝗔𝗠𝗤𝗣:
- Протокол обмена сообщениями для промежуточного программного обеспечения, ориентированного на сообщения.
- Приложения: облегчает связь между различными системами и службами, обеспечивая надежную доставку сообщений.

𝟴. 𝗦𝗦𝗘 (𝗦𝗲𝗿𝘃𝗲𝗿-𝗦𝗲𝗻𝘁 𝗘𝘃𝗲𝗻𝘁𝘀):
- Простой и эффективный протокол связи для односторонней связи от сервера к клиенту.
- Приложения: подходят для сценариев, где обновления в реальном времени имеют решающее значение, например,
  прямые трансляции и уведомления.

𝟵. 𝗘𝗗𝗜 (𝗘𝗹𝗲𝗰𝘁𝗿𝗼𝗻𝗶𝗰 𝗗𝗮𝘁𝗮 𝗜𝗻𝘁𝗲𝗿𝗰𝗵𝗮𝗻𝗴𝗲):
- Протокол межкомпьютерного обмена деловыми документами в стандартном электронном формате.
- Приложения: Широко используется в бизнесе и финансах для автоматизации обмена документами.

𝟭𝟬. 𝗘𝗗𝗔 (𝗘𝘃𝗲𝗻𝘁-𝗗𝗿𝗶𝘃𝗲𝗻 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲):
- Парадигма, способствующая производству, обнаружению, потреблению и реакции на события.
- Приложения: повышает оперативность работы систем в режиме реального времени, особенно в сложных распределенных средах.

𝟭𝟭. 𝗥𝗘𝗦𝗧 (𝗥𝗲𝗽𝗿𝗲𝘀𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗦𝘁𝗮𝘁𝗲 𝗧𝗿𝗮𝗻𝘀 𝗳𝗲𝗿):
- Архитектурный стиль программного обеспечения для разработки сетевых приложений.
- Приложения: широко используются для создания масштабируемых и обслуживаемых веб-сервисов.
"""
