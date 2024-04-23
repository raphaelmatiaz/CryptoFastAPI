FROM python:3.12-slim

RUN pip install poetry

WORKDIR /workspace

COPY . .

EXPOSE 8000

RUN poetry install

CMD poetry run python main.py

