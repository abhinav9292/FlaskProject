
from flask import Flask
from flask_sqlalchemy import SQLAlchemy     #for database connection
#hashing the password import this module
from flask_bcrypt import *
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '2ca4ab5bd16682a91cda17b652e55c3d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

from flaskblog import routes