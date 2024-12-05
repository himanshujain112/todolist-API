from flask import Flask, request
from flask_restful import Api, Resource
from controller.todo_controller import todoBP
from error_handler import handle_400_error, handle_404_error, handle_generic_error
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
#from controller.new_controller import testBP

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Superman'
jwt = JWTManager(app)
app.register_blueprint(todoBP)

#register error handlers
app.register_error_handler(400, handle_400_error)
app.register_error_handler(404, handle_404_error)
app.register_error_handler(500, handle_generic_error)
#app.register_blueprint(testBP)

class login(Resource):
    def post(self):
        user = request.json.get('username', None)
        password = request.json.get('password', None)
        if user != 'test' or password != 'test':
            return {"msg": "Bad username or password"}, 401
        accessToken = create_access_token(identity=user, expires_delta=timedelta(minutes=30))
        return {"access_token": accessToken}, 200

class Index(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return f"Hello {current_user}, you are free to access the Todo App!", 200


api = Api(app)
#Routes
api.add_resource(Index, '/')
api.add_resource(login, '/login')

if __name__ == '__main__':
    app.run(port=3000, debug=True)