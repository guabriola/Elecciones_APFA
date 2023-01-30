from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os

load_dotenv()

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# secret key
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")


#####Configuracion del Correo#####
SECRET_KEY = os.getenv("SECRET_KEY")
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# gmail authentication
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
#pass provisto por Gmail
# mail accounts
MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")

# initialize the app with the extension
db.init_app(app)

#Bootstrap
bootstrap = Bootstrap5(app)