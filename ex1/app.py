from flask import Flask

from my_app.tasks.controllers import taskRoute
from my_app.config import DevConfig

def create_app():
    app = Flask(__name__)

    # Carrega config (somente atributos em MAIÚSCULO)
    app.config.from_object(DevConfig)

    # Registra o blueprint
    app.register_blueprint(taskRoute)

    @app.route("/")
    def hello_world():
        return "Hello Flask"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=app.config["DEBUG"])
