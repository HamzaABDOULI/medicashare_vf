FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /django-app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .