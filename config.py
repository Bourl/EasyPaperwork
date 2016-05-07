import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI='mysql://chouchou:boubou@localhost/Chouchou'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
