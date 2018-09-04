import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.1and1.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUB_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')