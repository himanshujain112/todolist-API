import sqlite3
from flask import jsonify

class TodoModel():

    def __init__(self):
        print("Connecting to database...")
        try:
            self.conn = sqlite3.connect('todo.db', check_same_thread=False)
            self.cursor = self.conn.cursor()
            self.cursor.execute("create table if not exists todos (id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT)")
            print("Database connected successfully!")
            #self.cursor.execute("insert into todos (todo) values ('Go to Market')")
            #self.conn.commit()
        except Exception as e:
            print("Error in connecting to database: ", e)
    
    def get_all_todos(self):
        try:
            self.cursor.execute("select * from todos")
            result = self.cursor.fetchall()
            if not result:
                return jsonify("No Todos Found!")
            return jsonify([{"Todo" : row[1]} for row in result])
        except Exception as e:
            return "Error in fetching Todos!"
    
    def get_todo_by_id(self, todo_id):
        try:
            if not todo_id:
                return "Invalid Id!"
            todo_id = int(todo_id)
            self.cursor.execute("select * from todos where id=?", (todo_id,))
            result = self.cursor.fetchone()
            return jsonify({'Todo' : result[1]})
        except Exception as e:
            return "Todo Not Found!"
    
    def create_new_todo(self, todo):
        try:
            self.cursor.execute("insert into todos (todo) values (?)", (todo,))
            self.conn.commit()
            return "Todo Created successfully!"
        except Exception as e:
            return "Error in creating Todo!"

    def update_todo_by_id(self, todo_id, todo):
        try:
            self.cursor.execute("SELECT * FROM todos WHERE id=?", (todo_id,))
            result = self.cursor.fetchone()
            if result is None:
                return jsonify({"message": "Todo Not Found!"})
            #todo_id = int(todo_id)
            self.cursor.execute("update todos set todo=? where id=?", (todo, todo_id))
            self.conn.commit()
            return "Todo Updated successfully!"
        except Exception as e:
            return "Todo Not Found!"
    
    def delete_todo_by_id(self, todo_id):
        try:
            self.cursor.execute("SELECT * FROM todos WHERE id=?", (todo_id,))
            result = self.cursor.fetchone()
            if result is None:
                return jsonify({"message": "Todo Not Found!"})
            todo_id = int(todo_id)
            self.cursor.execute("delete from todos where id=?", (todo_id,))
            self.conn.commit()
            return "Todo Deleted successfully!"
        except Exception as e:
            return "Todo Not Found!"
    
