import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from application.routes import initialize_routes
from db import db

from flask_jwt_extended import (
    JWTManager, jwt_required, 
    create_access_token, get_jwt_identity
)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY') or os.urandom(24)
app.config['JWT_SECRET_KEY'] =  os.getenv('JWT_SECRET_KEY') or 'jsonsecretkey_is_secret'

db = SQLAlchemy(app)
jwt = JWTManager(app)


api = Api(app)
initialize_routes(api)


@app.route('/api')
def root():
    return jsonify({'status': 200, 'message': 'Welcome to savvy api\'s'})

@app.route('/')
def other_routes():
    return jsonify({'status': 200, 'message': 'Welcome to savvy application'})

if __name__ == '__main__':
    app.run(port=500, debug=True) 