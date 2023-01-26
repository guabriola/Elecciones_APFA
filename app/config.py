from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# secret key
app.config['SECRET_KEY'] = 'dsfpodsfsd fdsifhdspifhdshfidshio'
# mail
app.config["USER_EMAIL_SENDER_EMAIL"] = "test@mail.com"
# initialize the app with the extension
db.init_app(app)

bootstrap = Bootstrap5(app)