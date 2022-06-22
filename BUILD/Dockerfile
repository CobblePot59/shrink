FROM python:slim-buster
WORKDIR /opt/shrink
RUN python3 -m pip install gunicorn Flask Flask-SQLAlchemy hashids validators
ENV GUNICORN_CMD_ARGS="-b 0.0.0.0:80 -w 4"
EXPOSE 80
CMD ["gunicorn", "wsgi:app"]
