FROM python:slim-buster
WORKDIR /opt/shrink
RUN python3 -m pip install gunicorn Flask Flask-SQLAlchemy hashids validators
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:80 --workers=4"
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["-m", "gunicorn","wsgi:app"]
