from datetime import datetime
import uuid
from sqlalchemy import BOOLEAN, INTEGER, Column, ForeignKey, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.db import db, BaseModelMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import column_property

class User(db.Model, BaseModelMixin):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True)
    
    # An ID to use as a reference when sending email.
    external_id = Column(
        String(255), default=lambda: str(uuid.uuid4()), nullable=False, unique=True
    )
    
    social_id = Column(String(255), nullable=True, unique=True)
    social_type = Column(String(255))
    activated = Column(BOOLEAN, default=False, nullable=False) # type: ignore

    # When the user chooses to set up an account directly with the app.
    _password = Column(String(255))

    fullname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True, unique=True)
    picture = Column(String(255), nullable=True)

    created_at = Column(db.DateTime, default=lambda: datetime.now(), nullable=True)
    last_login = Column(db.DateTime, nullable=True)
    last_token = Column(Text, nullable=True)

    groups = association_proxy("members", "group")

    @property
    def password(self):
        raise AttributeError("Can't read password")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self._password, password)  # type: ignore
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_social_id(cls, social_id, social_type):
        return cls.query.filter_by(social_id=social_id, social_type=social_type).first()

class Category(db.Model, BaseModelMixin):
    __tablename__ = "categories"
    id = Column(INTEGER, primary_key=True)
    icons = Column(String(255))
    name = Column(String(255))
    member_id = Column(ForeignKey('members.id'))

class Currency(db.Model, BaseModelMixin):
    __tablename__= "currencies"
    id = Column(INTEGER, primary_key=True)
    symbol = Column(String(255))
    name = Column(String(255))

class Config(db.Model, BaseModelMixin):
    __tablename__ = "configs"
    id = Column(INTEGER, primary_key=True)
    currency_default_id = Column(ForeignKey('currencies.id'))
    member_id = Column(ForeignKey('members.id'))

class Group(db.Model, BaseModelMixin):
    __tablename__ = "groups"
    id = Column(INTEGER, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    members = association_proxy("member", "user")

class Member(db.Model, BaseModelMixin):
    __tablename__ = "members"
    id = Column(INTEGER, primary_key=True)
    user_id = Column(ForeignKey('users.id'))
    group_id = Column(ForeignKey('groups.id'))
    active = Column(BOOLEAN)

    user = db.relationship("User", backref=db.backref('members'))
    group = db.relationship("Group", backref=db.backref('member'))

class Transaction(db.Model, BaseModelMixin):
    __tablename__ = "transactions"
    id = Column(INTEGER, primary_key=True)
    type = Column(String(255))
    value = Column(INTEGER)
    category_id = Column(ForeignKey('categories.id'))
    currency_id = Column(ForeignKey('currencies.id'))
    user_id = Column(ForeignKey('users.id'))
    group_id = Column(ForeignKey('groups.id'))

