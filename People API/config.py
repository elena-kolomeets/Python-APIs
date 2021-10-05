import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# get the dir wher the app runs
basedir = os.path.abspath(os.path.dirname(__file__))
# create flask connexion app
connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app
# configure SQLAlchemy
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# connect SQLAlchemy to the app
db = SQLAlchemy(app)
# init Marshmallow 
ma = Marshmallow(app)
