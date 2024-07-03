FROM python:3.10-bookworm as base:
WORKDIR /app
EXPOSE 5000

COPY ./Src /app/Src
COPY ./DB /app/DB
COPY ./gpt_request.json /app/gpt_request.json
COPY ./main.py /app/main.py
COPY ./telegram.py /app/telegram.py

RUN pip install -r requirments.txt
CMD ["python3", "main.py"]