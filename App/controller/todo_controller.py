from flask import request, Blueprint
from flask_restful import Resource, Api
from model.todo_model import TodoModel
todos = {'1': 'Go to Market', '2': 'Buy a car', '3': 'Learn Python'}

obj = TodoModel()

class TodoResource(Resource):
#Print todo
    def get(self, todo_id=None):
        if todo_id:
            return obj.get_todo_by_id(todo_id)
        else:
            return obj.get_all_todos()

#Create new Todo
    def post(self):
        data = request.get_json()
        if not data:
            return {"error": "Invalid data"}, 400
        return obj.create_new_todo(data["todo"])
    
#Update a Todo
    def put(self, todo_id):
        #if todo_id not in todos:
         #   return {"error": "Todo not found"}, 404
        data = request.get_json()
        return obj.update_todo_by_id(todo_id, data["todo"])


        
#Delete a Todo
    def delete(self, todo_id):
        #if todo_id not in todos:
         #   return {"error": "Todo not found"}, 404
        return obj.delete_todo_by_id(todo_id)

todoBP = Blueprint('himan', __name__)
todoAPI = Api(todoBP)
todoAPI.add_resource(TodoResource, '/todo', '/todo/<int:todo_id>')