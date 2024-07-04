FROM python:3.10-bookworm AS base
WORKDIR /app
EXPOSE 5000

# Копируем исходный код
COPY ./Src /app/Src
COPY ./DB /app/DB
COPY ./gpt_request.json /app/gpt_request.json
COPY ./main.py /app/main.py
COPY ./telegram.py /app/telegram.py
COPY ./requirments.txt /app/requirments.txt
# Почему то приложение просит файл, хотя я Environment закидываю в образ!
#'subscribe_event':subscribe_event(db),
#File "/app/Src/Events/subcribe_event.py", line 29, in __init__
#  self.__settings=settings.from_json()
#File "/app/Src/settings.py", line 41, in from_json
#  with open(path) as json_file:
#FileNotFoundError: [Errno 2] No such file or directory: 'settings.json'
COPY ./settings.json /app/settings.json

RUN pip install -r requirments.txt
CMD ["python3", "main.py"]