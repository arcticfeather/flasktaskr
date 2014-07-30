import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'c8e88e3032ac40'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)