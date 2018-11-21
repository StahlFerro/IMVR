from flask import Flask
from config import Config, is_list
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.tests['is_list'] = is_list
app.jinja_env.globals['type'] = type
login = LoginManager(app)
login.login_view = '/login'
db = SQLAlchemy(app)
session = db.session
migrate = Migrate(app, db)

from server import routes, models
