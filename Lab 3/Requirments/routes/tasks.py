from flask import Blueprint, jsonify, request

tasks_bp = Blueprint('tasks', __name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Study how Flask works", "status": "Incomplete"},
    {"id": 2, "title": "Create API", "description": "Build a simple API", "status": "Incomplete"}
]

@tasks_bp.route('/', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@tasks_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@tasks_bp.route('/', methods=['POST'])
def add_task():
    new_task = request.get_json()
    if not new_task or 'title' not in new_task or 'description' not in new_task:
        return jsonify({"error": "Invalid input"}), 400

    new_task['id'] = len(tasks) + 1
    new_task['status'] = "Incomplete"
    tasks.append(new_task)
    return jsonify(new_task), 201

@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    updated_data = request.get_json()
    task.update(updated_data)
    return jsonify(task), 200

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200
