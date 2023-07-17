FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python manage.py migrate

EXPOSE 8000/tcp

CMD ["gunicorn", "--bind", ":8000", "--access-logfile", "-", "test_parser.wsgi"]
