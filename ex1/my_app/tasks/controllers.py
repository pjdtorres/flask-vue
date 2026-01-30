from flask import Blueprint, jsonify, request

taskRoute = Blueprint("tasks", __name__, url_prefix="/tasks")

# “banco” em memória só pra exemplo
TASKS = [
    {"id": 1, "title": "Estudar Flask", "done": False},
    {"id": 2, "title": "Criar API", "done": True},
]

@taskRoute.get("/")
def list_tasks():
    return jsonify(TASKS)

@taskRoute.get("/<int:task_id>")
def get_task(task_id: int):
    task = next((t for t in TASKS if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@taskRoute.post("/")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400

    new_id = (max([t["id"] for t in TASKS]) + 1) if TASKS else 1
    task = {"id": new_id, "title": title, "done": False}
    TASKS.append(task)
    return jsonify(task), 201

@taskRoute.patch("/<int:task_id>")
def update_task(task_id: int):
    task = next((t for t in TASKS if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True) or {}
    if "title" in data:
        task["title"] = data["title"]
    if "done" in data:
        task["done"] = bool(data["done"])

    return jsonify(task)

@taskRoute.delete("/<int:task_id>")
def delete_task(task_id: int):
    idx = next((i for i, t in enumerate(TASKS) if t["id"] == task_id), None)
    if idx is None:
        return jsonify({"error": "Task not found"}), 404

    removed = TASKS.pop(idx)
    return jsonify(removed)
