from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# In-memory storage for todos
todos = {}

# Home resource
class Home(Resource):
    def get(self):
        return {"message": "Welcome to Todo List API!"}, 200

# Todo resource for all CRUD operations
class TodoResource(Resource):
    def get(self, todo_id=None):
        if todo_id:
            # Retrieve a specific todo
            if todo_id in todos:
                return {todo_id: todos[todo_id]}, 200
            return {"error": "Todo not found"}, 404
        # List all todos
        return todos, 200

    def post(self):
        # Create a new todo
        data = request.json
        if not data or "id" not in data or "todo" not in data:
            return {"error": "Invalid data, 'id' and 'todo' are required"}, 400
        todo_id = data["id"]
        todo_text = data["todo"]
        if todo_id in todos:
            return {"error": "Todo with this ID already exists"}, 400
        todos[todo_id] = todo_text
        return {"message": "Todo added successfully", "todo": {todo_id: todo_text}}, 201

    def put(self, todo_id):
        # Update an existing todo
        if todo_id not in todos:
            return {"error": "Todo not found"}, 404
        data = request.json
        if not data or "todo" not in data:
            return {"error": "Invalid data, 'todo' is required"}, 400
        todos[todo_id] = data["todo"]
        return {"message": "Todo updated successfully", "todo": {todo_id: todos[todo_id]}}, 200

    def delete(self, todo_id):
        # Delete a todo
        if todo_id not in todos:
            return {"error": "Todo not found"}, 404
        del todos[todo_id]
        return {"message": "Todo deleted successfully"}, 204

# Routes
api.add_resource(Home, '/')
api.add_resource(TodoResource, '/todos', '/todos/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
