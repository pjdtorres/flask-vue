from flask import Blueprint, render_template, request, redirect, url_for, abort

# Blueprint no plural
taskRoute = Blueprint("tasks", __name__, url_prefix="/tasks")

task_list = []

@taskRoute.route("/")
def index():
    return render_template("dashboard/tasks/index.html", tasks=task_list)

@taskRoute.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            task_list.append(task)
            return redirect(url_for("tasks.index"))
    return render_template("dashboard/tasks/create.html", lista=task_list)

@taskRoute.route("/delete/<int:id>", methods=["POST"])
def delete_task_action(id):
    if 0 <= id < len(task_list):
        task_list.pop(id)
    return redirect(url_for("tasks.index"))

@taskRoute.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if not (0 <= id < len(task_list)):
        abort(404)
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            task_list[id] = task
            return redirect(url_for("tasks.index"))
    return render_template("dashboard/tasks/update.html", id=id, task=task_list[id])