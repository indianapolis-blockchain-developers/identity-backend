from typing import Optional, List
from identity_app.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)


    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email


    @classmethod
    def user_by_id(cls, id: int) -> Optional['UserModel']:
        return cls.query.filter_by(id=id).first()


    @classmethod
    def all_users(cls) -> List['UserModel']:
        return cls.query.all()


    def as_dict(self) -> dict:
        return {'name': self.name,
                'email': self.email}


    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
