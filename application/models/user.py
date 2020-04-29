from db import db

class User(db.Model):
    """This class represent the user table"""
    
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def jsons(self):
        return {"id": self.id, "username": self.username, "email": self.email}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        

    @staticmethod
    def get_all():
        return User.query.all()

    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def find_by_id(cls, id):
        user = cls.query.filter_by(id=id)
        return user
