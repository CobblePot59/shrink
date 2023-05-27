from datetime import timedelta

SECRET_KEY = '21359bb385cfb332aaedad6bee7cfc67983dde66143ee9c7ac0cdda204d4474d'
PERMANENT_SESSION_LIFETIME =  timedelta(minutes=15)
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/shrink/db/urls.db'
