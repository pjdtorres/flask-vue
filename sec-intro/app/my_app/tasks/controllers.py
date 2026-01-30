from flask import Blueprint

taskRoute = Blueprint("task", __name__, url_prefix="/tasks")
# http://127.0.0.1:5000/tasks/
# http://127.0.0.1:5000


@taskRoute.route("/")
def index():
    return "Index"


@taskRoute.route("/<int:id>")
def show(id: int):
    return "Show " + str(id)


# @app.route(<URI>, methods=('GET'))
# @app.route(<URI>, methods=('POST'))
# @app.route(<URI>, methods=('PUT'))
# @app.route(<URI>, methods=('PATCH'))
# @app.route(<URI>, methods=('DELETE'))
@taskRoute.route("/delete/<int:id>")
def delete(id: int):
    return "Delete " + str(id)


@taskRoute.route("/create", methods=("GET", "POST"))
def create():
    return "Create "


@taskRoute.route("/update/<int:id>", methods=["GET", "POST"])
def update(id: int):
    return "Update " + str(id)
