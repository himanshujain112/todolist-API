from flask import Flask
from flask_restful import Api, Resource
from controller.todo_controller import todoBP
#from controller.new_controller import testBP

app = Flask(__name__)
app.register_blueprint(todoBP)
#app.register_blueprint(testBP)

class Index(Resource):
    def get(self):
        return "Welcome to the Todo List API !", 200


api = Api(app)
#Routes
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(port=3000, debug=True)