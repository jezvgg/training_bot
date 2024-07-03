# Инструкция по запуску

1. Запускаем сборку проекта
```
sudo docker build -t training .
```

2. Проверяем. Должен получиться образ
```
sudo docker images
```

3. Запускаем docker-compose
```
sudo docker-compose up -d
```

База данных, порт: **5432**
PgAdmin, порт: **5050**
Приложение, порт: **5000**

4. Проверка
```
sudo docker ps -a

CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS                  PORTS                                            NAMES
0c107fa91601   dpage/pgadmin4   "/entrypoint.sh"         53 seconds ago   Up 51 seconds           443/tcp, 0.0.0.0:5050->80/tcp, :::5050->80/tcp   pgadmin_container
a9d9623c0a08   training-bot     "python3 main.py"        53 seconds ago   Up Less than a second   5000/tcp                                         training
f6c3f7eeceda   postgres         "docker-entrypoint.s…"   53 seconds ago   Up 52 seconds           0.0.0.0:5432->5432/tcp, :::5432->5432/tcp        postgres_container
```

5. Файл настроек `settings.json` пробрасывается в контейнер. Логин / пароли к базек данных сохранены, как в файле.

