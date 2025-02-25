from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin


db = SQLAlchemy()

# models, flask security---> user, role(role based auth)
# user, role many to many rel

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    fs_uniquifier = db.Column(db.String(50), unique = True, nullable = False)
    active = db.Column(db.Boolean(), nullable = False)
    roles = db.relationship('Role', backref = 'bearers', secondary = 'users_roles')


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    description = db.Column(db.String(50))

class UsersRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))