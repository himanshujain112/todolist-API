from flask import Flask
from flask_restful import Api, Resource
from controller.todo_controller import todoBP
from error_handler import handle_400_error, handle_404_error, handle_generic_error

#from controller.new_controller import testBP

app = Flask(__name__)
app.register_blueprint(todoBP)

#register error handlers
app.register_error_handler(400, handle_400_error)
app.register_error_handler(404, handle_404_error)
app.register_error_handler(500, handle_generic_error)
#app.register_blueprint(testBP)

class Index(Resource):
    def get(self):
        return "Welcome to the Todo List API !", 200


api = Api(app)
#Routes
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)