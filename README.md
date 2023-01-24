# Проектная работа 8 спринта | UGC Service

ссылка на репозиторий https://github.com/paQQuete/ugc_sprint_1
участники @paqquete, @alexbravada, @npocbet

**Python 3.8**

Запуск проекта (Kafka, Clickhouse, FastAPI)
```shell
docker compose up
```

После запуска станет доступен эндпоинт API для добавления сообщений в топик Kafka
*[документация](http://127.0.0.1:8000/api/openapi)*
 
 
После, нужно запустить файл с запросами к clickhouse для подписки на топик Kafka и представления полученных сообщений в таблицу 'views' в БД 
```shell
python3 etl/process.py
```

*PROFIT!* Теперь можно отправлять на API данные о состоянии просмотра фильмов и через секунду они будут доступны в Clickhouse для аналитики

**Исследование аналитиических хранилищ**

Доступно  *[тут](https://github.com/paQQuete/ugc_sprint_1/blob/main/db_research/RESEARCH.md)*