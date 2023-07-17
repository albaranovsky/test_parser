# test_parser

Задача:
- Создать парсер excel файла (во вложении) на Python.
- Создать таблицу согласно нормам реляционных баз данных (внести все значения в одну таблицу)
- Добавить расчетный тотал по Qoil, Qliq, сгруппированный по датам (даты можете указать свои, добавив программно, не изменяя исходный файл, при условии, что дни будут разные, а месяц и год одинаковые)

Развёрнутый проект (при первом открытии ссылки возможна задержка до 60 секунд): [https://test-parser.onrender.com](https://test-parser.onrender.com)

[![Create and publish a Docker image](https://github.com/albaranovsky/test_parser/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/albaranovsky/test_parser/actions/workflows/docker-publish.yml)

## Запуск проекта в контейнере Docker
Скачать образ и запустить контейнер:

```shell
docker run --rm -p 8000:8000 ghcr.io/albaranovsky/test_parser:main
```

Открыть в браузере ссылку: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Запуск проекта локально
Клонировать репозиторий и перейти в него в командной строке:

```shell
git clone https://github.com/albaranovsky/test_parser.git
```

```shell
cd test_parser
```

Создать и активировать виртуальное окружение:

```shell
python3 -m venv .venv
```

```shell
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```shell
python3 -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

Запустить сервер:

```shell
gunicorn test_parser.wsgi
```

Открыть в браузере ссылку: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
