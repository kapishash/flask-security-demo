from flask_restful import Api, Resource, reqparse
from flask_security import auth_required, roles_required, hash_password
from application.models import db
from flask import current_app as app

api = Api()

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')
# parser.add_argument('roles', type=list)

class UserApi(Resource):
    def post(self):
        args = parser.parse_args()
        with app.app_context():
            if not app.security.datastore.find_user(email = args['email']):
                app.security.datastore.create_user(email = args['email'],password = hash_password(args['password']),roles = ['student'])
            

                return {
                    "message": "User created successfully"
                }, 201

            db.session.commit()
            
            

    
api.add_resource(UserApi, '/adduser')