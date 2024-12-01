from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__) 
api = Api(app)

todo = {}

class Home(Resource):
    def get(self):
        return "Welcome to Todo List API!"

class post_Todo(Resource):
    def post(self, newTodo):
        todo[newTodo] = newTodo
        return "Todo added successfully!"

class get_Todo(Resource):
    def get(self, todoId):
        return jsonify(todo[todoId])

class delete_Todo(Resource):
    def delete(self, todoId):
        del todo[todoId]
        return "Todo deleted successfully!"

class update_Todo(Resource):
    def put(self, todoId):
        todo[todoId] = request.json['newTodo']
        return "Todo updated successfully!"

class listTodo(Resource):
    def get(self):
        return jsonify(todo)    

api.add_resource(Home, '/')
api.add_resource(post_Todo, '/addTodo/<string:newTodo>')
api.add_resource(get_Todo, '/getTodo/<string:todoId>')
api.add_resource(delete_Todo, '/deleteTodo/<string:todoId>')
api.add_resource(update_Todo, '/updateTodo/<string:todoId>')
api.add_resource(listTodo, "/todo")

if __name__ == '__main__':
    app.run(debug=True)