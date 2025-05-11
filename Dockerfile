FROM python:3.12-slim


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libcairo2 libcairo2-dev \
      libpango1.0-0 libpango1.0-dev \
      libgdk-pixbuf2.0-0 libffi-dev \
      shared-mime-info \
      pkg-config && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]