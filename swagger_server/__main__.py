#!/usr/bin/env python3

import connexion
import os
import sqlalchemy
from swagger_server import encoder
from swagger_server.models.db_model import engine, Base


Base.metadata.create_all(engine)
basedir = os.path.abspath(os.path.dirname(__file__))
application = connexion.FlaskApp(__name__, specification_dir='./swagger/')
application.app.json_encoder = encoder.JSONEncoder
application.add_api('swagger.yaml', arguments={'title': 'Notify'})
app = application.app
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'db.sqlite')

app.run(port=8080)
