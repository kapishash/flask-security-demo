from flask import Flask
from application.config import DevelopmentConfig
from application.models import db, User, Role
from application.resources import api
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import hash_password

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    api.init_app(app)

    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, datastore)
    app.app_context().push()

    return app

app = create_app()

with app.app_context():
    db.create_all()
    app.security.datastore.find_or_create_role(name = 'admin', description = "This is super user")
    app.security.datastore.find_or_create_role(name = 'instructor', description = "This is instructor")
    app.security.datastore.find_or_create_role(name = 'student', description = "This is general student")

    if not app.security.datastore.find_user(email = "test1@admin.com"):
        app.security.datastore.create_user(email = "test1@admin.com",
                                           password = hash_password('1234'),
                                           roles = ['admin', 'instructor', 'student']
                                           )
        
    db.session.commit()

if __name__ == "__main__":
    app.run()

    