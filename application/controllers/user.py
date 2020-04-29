from typing import Dict, List
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Response, request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity,
    create_refresh_token
)

from ..models.user import User
from ..validation.user_validation import UserValidation


class UsersApi(Resource):
    # Get all user --> This endpoint return all users
    def get(self) -> Dict:
        users = User.get_all()
        return ({'status': 200, 'message': 'Users successfully retrieved', 'data': {'users': [user.jsons() for user in users]}}), 200
        
class ProtectedApi(Resource):
    
    @jwt_required
    def get(self) -> Dict:
        current_user = get_jwt_identity()
        print(current_user)
        if not current_user:
            return ({'status': 400, 'message': 'You have to provide you token before accessing this endpoint'}), 400 
        return ({'status': 200, 'message': 'This is protected api endpoint', 'data': {
            'current user': current_user
        }})

class UserRegister(Resource):
    parser = UserValidation.validate_register()
    def post(self) -> Dict:
        data = UserRegister.parser.parse_args()

        username = data['username']
        if User.find_by_username(username):
            return {'status': 400, "message": "Username already exist"}, 400

        password = data['password']
        hash_password = generate_password_hash(password)
        email = data['email']
        
        user = User(username=username, password=hash_password, email=email)
        user.save_to_db()

        return ({'status': 201, 'message': 'Your registration was successfull' }), 201


class UserLogin(Resource):
    parser = UserValidation.validate_login()
    def post(self) -> Dict:
        data = UserLogin.parser.parse_args()

        username = data['username']
        password = data['password']

        if not username:
            return ({'status': 400, 'message': 'Username cannot be empty' }), 400
        if not password:
            return ({'status': 400, 'message': 'Password cannot be empty'}), 400

        current_user = User.find_by_username(username=username)
    	
        print(current_user)

        if not current_user or not check_password_hash(current_user.password, password):
            return ({'status': 401, 'message': 'Login credentials are invalid'}), 401

        access_token = create_access_token(identity=username, fresh=True)
        refresh_token = create_refresh_token(username)
        return ({
            'status': 200, 
            'message': 'login successful',
            'tokens': {
                'access_token':access_token, 'refresh_token': refresh_token
            }
        }), 200

 