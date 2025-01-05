from flask import Flask, request, jsonify

app = Flask(__name__)

todo_list = []

@app.route("/todo/create", methods=["POST"])
def createToDo():
    task = request.json
    todo_list.append(task)
    return jsonify({'message': 'Task created successfully', 'Data': task }), 201

@app.route('/todo_list', methods=["GET"])
def getToDoList():
    return jsonify(todo_list), 200

@app.route('/todo/markAsDone/<item_id>', methods=['PUT'])
def markAsDone(item_id):
    updated = False
    for task in todo_list:
        if str(task['id']) == item_id:
            task['completed'] = True
            updated = True
            return jsonify({'message': 'Task updated successfully'}), 200
    return jsonify({'message': 'Task not found'}), 404

@app.route('/todo/<item_id>', methods=['Delete'])
def deleteTask(item_id):
    deleted = False
    for task in todo_list:
        if str(task['id']) == item_id:
            todo_list.remove(task)
            deleted = True
            return jsonify({'message': 'Task deleted successfully'}), 200
    return jsonify({'message': 'Task not found'}), 404 
        
if __name__ == '__main__':
    app.run(debug=True)
    
