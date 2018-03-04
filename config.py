import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = '*%oq*1ucsmicb52$h_$t=in2$*mo1_&2(y4bzk9&r!$+_aa^zc'

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025
    MAIL_USE_TLS = False
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    ADMINS = ['vs@yopmail.com', ]