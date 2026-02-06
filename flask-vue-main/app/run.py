from my_app import app
from my_app.extensions import db

if __name__ == "__main__":
    # Configuraciones de desarrollo
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.auto_reload = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

    with app.app_context():
        # IMPORTA os models antes do create_all
        from my_app.tasks.models import Task  # ou: from my_app.tasks import models
        db.create_all()

        print("--- MAPA DE RUTAS ---")
        print(app.url_map)
        print("---------------------")

    app.run(host="127.0.0.1", port=5000, debug=True)
