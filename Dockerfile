FROM python:3.12.0-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY dependecy.txt dependecy.txt
RUN pip install --upgrade pip && pip install -r dependecy.txt 

COPY . .

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000

CMD ["python","manage.py", "runserver","0.0.0.0:8000"]