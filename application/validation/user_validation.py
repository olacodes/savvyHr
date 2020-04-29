from flask_restful import Resource, reqparse

class UserValidation:
    @classmethod
    def validate_register(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str, required=True,
            help='This field cannot be blank'
        )
        parser.add_argument('password', 
            type=str, required=True,
            help='This field cannot be blank'
        )
        parser.add_argument('email', 
            type=str, required=True,
            help='This field cannot be blank'
        )
        return parser

    @classmethod
    def validate_login(cls):    
        parser = reqparse.RequestParser()
        parser.add_argument('username', 
            type=str, required=True,
            help='This field cannot be blank'
        )
        parser.add_argument('password', 
            type=str, required=True,
            help='This field cannot be blank'
        )
        return parser
    
