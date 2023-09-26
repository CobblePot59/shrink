FROM python:slim-buster
WORKDIR /opt/shrink
RUN python3 -m pip install --no-cache-dir gunicorn flask flask-sqlalchemy hashids validators flask-toastr
EXPOSE 80
CMD ["gunicorn", "wsgi:app", "--bind=0.0.0.0:80", "--workers=4", "--reload"]
