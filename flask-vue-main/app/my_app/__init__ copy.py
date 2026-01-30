from flask import Flask, render_template, request
from my_app.tasks.controllers import taskRoute
from my_app.config import DevConfig

# 1. Inicializa a app apenas UMA vez
app = Flask(__name__, template_folder="templates")

# 2. Carrega as configurações (Debug, etc.) do seu ficheiro de config
app.config.from_object(DevConfig)

# 3. Regista o Blueprint apenas UMA vez
app.register_blueprint(taskRoute)

# Debugging de pastas (Opcional, pode manter para verificar o CSS)
print("STATIC_FOLDER =", app.static_folder)

@app.route("/")
def hello_world():
    # Esta versão é melhor porque permite passar o nome via URL (?name=João)
    name = request.args.get("name")
    return render_template("index.html", task=name, name=name)