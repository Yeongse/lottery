FROM python:latest
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app
CMD python3 lottery/manage.py makemigrations && \
    python3 lottery/manage.py migrate && \
    python3 lottery/manage.py runserver 0.0.0.0:8000
