from flask import request, Blueprint, jsonify
from flask_restful import Resource, Api
from model.todo_model import TodoModel
from marshmallow import Schema, fields, ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
#todos = {'1': 'Go to Market', '2': 'Buy a car', '3': 'Learn Python'}

class itemSchema(Schema):
    id = fields.Int(required=True)
    todo = fields.Str(load_default="No description provided")

item_Schema = itemSchema()
obj = TodoModel()

class TodoResource(Resource):
#Print todo
    @jwt_required()
    def get(self, todo_id=None):
        if todo_id:
            return obj.get_todo_by_id(todo_id)
        else:
            return obj.get_all_todos()

#Create new Todo
    @jwt_required()
    def post(self):
        try:
            data = item_Schema.load(request.json)
            
        #if not data:
          #  return {"error": "Invalid data"}, 400
            return obj.create_new_todo(data["todo"]), 201
        except ValidationError as err:
            return ({"error message" : err.messages}), 400
    
#Update a Todo
    @jwt_required()
    def put(self, todo_id):
        #if todo_id not in todos:
         #   return {"error": "Todo not found"}, 404
        data = request.get_json()
        return obj.update_todo_by_id(todo_id, data["todo"])


        
#Delete a Todo
    @jwt_required()
    def delete(self, todo_id):
        #if todo_id not in todos:
         #   return {"error": "Todo not found"}, 404
        return obj.delete_todo_by_id(todo_id)

todoBP = Blueprint('himan', __name__)
todoAPI = Api(todoBP)
todoAPI.add_resource(TodoResource, '/todo', '/todo/<int:todo_id>')