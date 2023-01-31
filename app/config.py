from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
from flask_redmail import RedMail
from redmail import gmail

load_dotenv()

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# secret key
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")



# initialize the app with the extension



db.init_app(app)
app.config["EMAIL_HOST"] = gmail.host
app.config["EMAIL_PORT"] = gmail.port
app.config["EMAIL_USERNAME"] = os.getenv('MAIL_USERNAME')
app.config["EMAIL_PASSWORD"] = os.getenv('MAIL_PASSWORD')
app.config["EMAIL_SENDER"] = os.getenv('MAIL_USERNAME')


email = RedMail(app)
# Bootstrap
bootstrap = Bootstrap5(app)
