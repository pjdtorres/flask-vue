from flask import Flask
from my_app.config import DevConfig
from my_app.extensions import db

# Inicializamos la aplicación Flask con la configuración de desarrollo
app = Flask(__name__)
app.config.from_object(DevConfig)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# from flask_sqlalchemy import SQLAlchemy
# db=SQLAlchemy(app)
# # db.create_all()
# with app.app_context():
#     db.create_all()
#     print("Tabelas criadas com sucesso!")

# A partir da pasta app, o caminho é my_app -> util -> template_filter
from my_app.util.template_filter import text_to_upper

# E não te esqueças de registar o filtro na tua instância da app Flask
app.add_template_filter(text_to_upper)

# 1. Definimos la ruta básica primero
@app.route("/")
def home():
    return "Servidor Online! Vá para <a href='/tasks'>Lista de Tarefas</a>"

# 2. IMPORTACIÓN Y REGISTRO (Una sola vez y al final)
from my_app.tasks.controllers import taskRoute
app.register_blueprint(taskRoute)