FROM tiangolo/uwsgi-nginx:python3.5

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

COPY ./app /app