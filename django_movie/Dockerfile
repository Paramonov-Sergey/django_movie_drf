FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/django_movie_drf

COPY ./requerements.txt /usr/src/requerements.txt
RUN pip install -r /usr/src/requerements.txt

COPY . /usr/src/django_movie_drf

EXPOSE 8000

#CMD ["python","manage.py","migrate"]
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]


