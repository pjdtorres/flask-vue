from flask import Flask
# Certifique-se de que está a importar a variável 'taskRoute' correta
from my_app.tasks.controllers import taskRoute

app = Flask(__name__)

# O Flask usa o objeto que importou acima
app.register_blueprint(taskRoute)

@app.route("/")
def home():
    return "Servidor Online! Vá para <a href='/tasks/'>Lista de Tarefas</a>"