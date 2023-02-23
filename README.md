# Проектная работа 9 спринта | UGC Service

ссылка на репозиторий https://github.com/paQQuete/ugc_sprint_1
участники @paqquete, @alexbravada, @npocbet

Запуск проекта (Kafka, Clickhouse, FastAPI, MongoDB, ETL (Kafka - MongoDB, Kafka - Clickhouse), Jupyter, ELK)

```shell
nohup ./start.sh > start.log 2>&1 &
```
*(запуск стартового скрипта без привязки к терминалу и запись stdout в файл)*

После запуска станут доступны эндпоинты API для добавления сообщений в топики Kafka
*[документация](http://127.0.0.1:8000/api/openapi)*

Теперь можно отправлять на API данные о состоянии просмотра фильмов и через секунду они будут доступны в Clickhouse и MongoDB для аналитики

**Исследование хранилищ**

Доступно  *[тут](https://github.com/paQQuete/ugc_sprint_1/blob/main/db_research/README.md)*

**Кратко о структуре проекта**

Поднимается платформа Confluent с Kafka, в start.sh создаются топики в Kafka, запускаются скрипты настройки Clickhouse, MongoDB,
запись сообщений в Kafka осуществляется через *[api (FastAPI)](http://127.0.0.1:8000/api/openapi)*, в Clickhouse сообщения попадают с помощью
Kafka Table Engine (*[etl/clickhouse.py](https://github.com/paQQuete/ugc_sprint_1/blob/main/etl/clickhouse.py)*), 
в MongoDB - с помощью ETL на Python (*[etl/kafka_mongo](https://github.com/paQQuete/ugc_sprint_1/tree/main/etl/kafka_mongo)*).
*[UML диаграммы](https://github.com/paQQuete/ugc_sprint_1/tree/main/uml)*
