FROM tiangolo/uwsgi-nginx-flask:flask

RUN pip install boto

COPY ./app /app
