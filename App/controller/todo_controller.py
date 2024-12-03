from flask import request, Blueprint
from flask_restful import Resource, Api

todos = {'1': 'Go to Market', '2': 'Buy a car', '3': 'Learn Python'}

class TodoResource(Resource):
#Print todo
    def get(self, todo_id=None):
        if todo_id:
            if todo_id in todos:
                return {todo_id: todos[todo_id]}, 200
            else:
                return {"error": "Todo not found"}, 404
        return todos, 200

#Create new Todo
    def post(self):
        data = request.get_json()
        if not data or "id" not in data or "todo" not in data:
            return {"error": "Invalid data"}, 400
        todo_id = data["id"]
        todo_text = data["todo"]

        if todo_id in todos:
            return {"error": "Todo id already present!"}, 400
        todos[todo_id] = todo_text
        return {"message" : "Todo Created successfully!" , "todo": {todo_id: todo_text}}, 201

#Update a Todo
    def put(self, todo_id):
        if todo_id not in todos:
            return {"error": "Todo not found"}, 404
        data = request.get_json()

        if not data or "todo" not in data:
            return {"error": "Invalid data"}, 400
        todos[todo_id] = data["todo"]
        return {"message" : "Todo Updated successfully!" , "todo": {todo_id: todos[todo_id]}}, 200
    
#Delete a Todo
    def delete(self, todo_id):
        if todo_id not in todos:
            return {"error": "Todo not found"}, 404
        del todos[todo_id]
        return {"message" : "Todo Deleted successfully!"}, 200

todoBP = Blueprint('himan', __name__)
todoAPI = Api(todoBP)
todoAPI.add_resource(TodoResource, '/todo', '/todo/<string:todo_id>')