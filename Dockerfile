FROM tiangolo/uwsgi-nginx-flask:flask

RUN pip install -r ./requirements.txt

COPY ./app /app
