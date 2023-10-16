FROM python:3.10

COPY . /RESTful_API_Flask_MongoDB
WORKDIR /RESTful_API_Flask_MongoDB
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_HOST='0.0.0.0'
ENV FLASK_PORT=5000
ENV DB_HOST='mongodb'
ENV DB_PORT='27017'
ENV DB_NAME='db'
ENV COLLECTION_NAME='collection'

CMD [ "python", "main.py" ]