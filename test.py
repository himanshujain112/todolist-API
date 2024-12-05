from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Superman'
jwt = JWTManager(app)
api = Api(app)

class Login(Resource):
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username != 'test' or password != 'test':
            return {"msg": "Bad username or password"}, 401

        access_token = create_access_token(identity=username)
        return {"access_token": access_token}, 200
    
class Protected(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"logged_in_as": current_user}, 200

api.add_resource(Login, '/login')
api.add_resource(Protected, '/protected')


if __name__ == '__main__':
    app.run(port=3000, debug=True)