FROM tiangolo/uwsgi-nginx:python3.5

RUN pip install flask

COPY ./app /app
